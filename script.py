"""
КОСМИЧЕСКИЙ СИМУЛЯТОР NASA + АКВТ - 3D ВЕРСИЯ
Астраханский колледж вычислительной техники
КРАСИВЫЕ ПЛАНЕТЫ + РАБОЧАЯ АНИМАЦИЯ + КНОПКИ
"""

import pygame
import sys
import math
import random

pygame.init()

# ==================================================
# НАСТРОЙКИ ЭКРАНА
# ==================================================

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("АКВТ — Космический центр управления")
clock = pygame.time.Clock()

# ==================================================
# ЦВЕТА
# ==================================================

BLACK = (5, 10, 20)
DEEP_SPACE = (8, 15, 30)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 210)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
YELLOW = (255, 230, 80)
ORANGE = (255, 150, 50)
GOLD = (255, 200, 50)
PURPLE = (150, 50, 255)
DARK_GRAY = (40, 40, 60)
CYAN = (0, 255, 255)
NEON_BLUE = (0, 150, 255)
BLUE = (30, 100, 200)
LIGHT_BLUE = (100, 150, 255)
OCEAN_BLUE = (30, 80, 180)
LAND_GREEN = (60, 180, 80)
MOON_GRAY = (180, 180, 190)
MOON_CRATER = (120, 120, 130)
PINK = (255, 100, 150)
MAGIC_PURPLE = (180, 100, 255)
DARK_GREEN = (30, 100, 50)
SAND = (210, 180, 140)
CLOUD = (220, 220, 240)

# Шрифты
font_small = pygame.font.Font(None, 16)
font_medium = pygame.font.Font(None, 20)
font_large = pygame.font.Font(None, 26)
font_title = pygame.font.Font(None, 28)
font_big = pygame.font.Font(None, 48)
font_coord = pygame.font.Font(None, 14)
font_magic = pygame.font.Font(None, 60)
font_info_title = pygame.font.Font(None, 24)
font_info = pygame.font.Font(None, 16)

# ==================================================
# ДАННЫЕ ПЛАНЕТ
# ==================================================

PLANETS_FULL_DATA = {
    "Солнце": {
        "🌡 Температура": "5,500°C",
        "⭐ Тип": "Жёлтый карлик",
        "📏 Диаметр": "1,392,700 км",
        "⚖ Масса": "1.989 × 10³⁰ кг",
    },
    "Земля": {
        "🌡 Температура": "15°C",
        "⭐ Тип": "Каменная планета",
        "📏 Диаметр": "12,742 км",
        "⚖ Масса": "5.97 × 10²⁴ кг",
        "🛰 Спутники": "1 (Луна)",
    },
    "Луна": {
        "🌡 Температура": "-173°C до 127°C",
        "⭐ Тип": "Спутник",
        "📏 Диаметр": "3,474 км",
        "⚖ Масса": "7.35 × 10²² кг",
    },
    "Марс": {
        "🌡 Температура": "-65°C",
        "⭐ Тип": "Каменная планета",
        "📏 Диаметр": "6,779 км",
        "⚖ Масса": "6.39 × 10²³ кг",
    },
    "Юпитер": {
        "🌡 Температура": "-110°C",
        "⭐ Тип": "Газовый гигант",
        "📏 Диаметр": "139,820 км",
        "⚖ Масса": "1.898 × 10²⁷ кг",
    },
    "Венера": {
        "🌡 Температура": "462°C",
        "⭐ Тип": "Каменная планета",
        "📏 Диаметр": "12,104 км",
        "⚖ Масса": "4.87 × 10²⁴ кг",
    },
    "Сатурн": {
        "🌡 Температура": "-140°C",
        "⭐ Тип": "Газовый гигант",
        "📏 Диаметр": "116,460 км",
        "⚖ Масса": "5.68 × 10²⁶ кг",
        "💍 Кольца": "Есть",
    },
}


# ==================================================
# КНОПКА
# ==================================================

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        if self.is_hovered:
            return True
        return False

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=8)
        text_surface = font_medium.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


# ==================================================
# ПАНЕЛЬ УПРАВЛЕНИЯ
# ==================================================

class ControlPanel:
    def __init__(self):
        self.speed = 1.0
        self.paused = False
        self.show_trails = True
        self.show_stars = True

        # Кнопки
        self.btn_y = HEIGHT - 55
        self.speed_up_btn = Button(30, self.btn_y, 45, 38, "+", GREEN, (80, 255, 80))
        self.speed_down_btn = Button(85, self.btn_y, 45, 38, "-", RED, (255, 100, 100))
        self.reset_btn = Button(145, self.btn_y, 75, 38, "СБРОС", PURPLE, (180, 100, 255))
        self.pause_btn = Button(235, self.btn_y, 90, 38, "ПАУЗА", ORANGE, (255, 200, 80))
        self.trails_btn = Button(340, self.btn_y, 90, 38, "ТРЕКИ", CYAN, (100, 255, 255))
        self.stars_btn = Button(445, self.btn_y, 100, 38, "ЗВЁЗДЫ", (80, 80, 180), (130, 130, 230))

        self.buttons = [self.speed_up_btn, self.speed_down_btn, self.reset_btn,
                        self.pause_btn, self.trails_btn, self.stars_btn]

        self.alerts = []
        self.alert_timer = 0

    def update(self, mouse_pos):
        for btn in self.buttons:
            btn.update(mouse_pos)

    def handle_click(self, pos):
        if self.speed_up_btn.check_click(pos):
            self.speed = min(2.0, self.speed + 0.1)
            return "speed"
        if self.speed_down_btn.check_click(pos):
            self.speed = max(0.2, self.speed - 0.1)
            return "speed"
        if self.reset_btn.check_click(pos):
            self.speed = 1.0
            self.paused = False
            self.pause_btn.text = "ПАУЗА"
            return "reset"
        if self.pause_btn.check_click(pos):
            self.paused = not self.paused
            self.pause_btn.text = "СТАРТ" if self.paused else "ПАУЗА"
            return "pause"
        if self.trails_btn.check_click(pos):
            self.show_trails = not self.show_trails
            return "trails"
        if self.stars_btn.check_click(pos):
            self.show_stars = not self.show_stars
            return "stars"
        return None

    def add_alert(self, message):
        self.alerts.insert(0, message)
        if len(self.alerts) > 2:
            self.alerts.pop()
        self.alert_timer = 40

    def draw(self, screen):
        # Панель
        panel_rect = pygame.Rect(10, HEIGHT - 110, WIDTH - 20, 95)
        panel_surface = pygame.Surface((panel_rect.width, panel_rect.height), pygame.SRCALPHA)
        panel_surface.fill((0, 0, 30, 220))
        screen.blit(panel_surface, panel_rect)
        pygame.draw.rect(screen, NEON_BLUE, panel_rect, 2, border_radius=12)

        # Заголовок
        title = font_title.render("🚀 ЦЕНТР УПРАВЛЕНИЯ", True, NEON_BLUE)
        screen.blit(title, (panel_rect.x + 15, panel_rect.y + 8))

        # Кнопки
        for btn in self.buttons:
            btn.draw(screen)

        # Скорость
        speed_text = font_medium.render(f"⚡ СКОРОСТЬ: {self.speed:.1f}x", True, YELLOW)
        screen.blit(speed_text, (570, HEIGHT - 85))

        # Статус
        status = "⏸ ПАУЗА" if self.paused else "▶ РАБОТА"
        status_color = ORANGE if self.paused else GREEN
        status_text = font_medium.render(status, True, status_color)
        screen.blit(status_text, (570, HEIGHT - 60))

        # Предупреждения
        if self.alert_timer > 0:
            self.alert_timer -= 1
            for i, alert in enumerate(self.alerts):
                color = RED if self.alert_timer % 10 < 5 else YELLOW
                alert_text = font_small.render(alert, True, color)
                screen.blit(alert_text, (panel_rect.right - 200, panel_rect.y + 35 + i * 20))


# ==================================================
# ИНФОРМАЦИОННОЕ ОКНО ПЛАНЕТЫ
# ==================================================

class PlanetInfoWindow:
    def __init__(self):
        self.visible = False
        self.planet_name = None
        self.planet_data = None
        self.width = 320
        self.height = 280
        self.x = WIDTH - self.width - 20
        self.y = 80

    def show(self, planet_name):
        if planet_name in PLANETS_FULL_DATA:
            self.planet_name = planet_name
            self.planet_data = PLANETS_FULL_DATA[planet_name]
            self.visible = True

    def hide(self):
        self.visible = False
        self.planet_name = None
        self.planet_data = None

    def handle_click(self, pos):
        if not self.visible:
            return False

        # Кнопка закрытия
        close_rect = pygame.Rect(self.x + self.width - 30, self.y + 8, 22, 22)
        if close_rect.collidepoint(pos):
            self.hide()
            return True
        return False

    def draw(self, screen):
        if not self.visible:
            return

        # Окно
        window_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        window_surface.fill((10, 15, 40, 240))
        pygame.draw.rect(window_surface, NEON_BLUE, (0, 0, self.width, self.height), 2, border_radius=12)

        # Заголовок
        emoji = {"Солнце": "☀️", "Земля": "🌍", "Луна": "🌙", "Марс": "🔴",
                 "Юпитер": "🪐", "Венера": "🟡", "Сатурн": "💍"}.get(self.planet_name, "🪐")
        title = font_info_title.render(f"{emoji} {self.planet_name}", True, YELLOW)
        window_surface.blit(title, (15, 12))

        # Кнопка закрытия
        pygame.draw.circle(window_surface, RED, (self.width - 19, 19), 11)
        pygame.draw.circle(window_surface, WHITE, (self.width - 19, 19), 11, 2)
        close_text = font_small.render("✕", True, WHITE)
        window_surface.blit(close_text, (self.width - 23, 14))

        # Разделитель
        pygame.draw.line(window_surface, NEON_BLUE, (15, 45), (self.width - 15, 45), 2)

        # Характеристики
        y_offset = 58
        for key, value in self.planet_data.items():
            label = font_info.render(key, True, CYAN)
            window_surface.blit(label, (15, y_offset))
            value_text = font_info.render(str(value), True, WHITE)
            window_surface.blit(value_text, (15, y_offset + 20))
            y_offset += 42

            if y_offset > self.height - 40:
                break

        screen.blit(window_surface, (self.x, self.y))


# ==================================================
# ДАННЫЕ ЗЕМЛИ (ВРЕМЯ)
# ==================================================

class EarthTimeDisplay:
    def __init__(self):
        self.total_seconds = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def update(self, speed_multiplier, paused):
        if not paused:
            self.total_seconds += 0.1 * speed_multiplier
            if self.total_seconds >= 86400:
                self.total_seconds -= 86400
                self.days += 1

            self.hours = int(self.total_seconds // 3600)
            self.minutes = int((self.total_seconds % 3600) // 60)
            self.seconds = int(self.total_seconds % 60)

    def draw(self, screen):
        window_x = WIDTH - 300
        window_y = HEIGHT - 220
        window_w = 280
        window_h = 105

        window_surface = pygame.Surface((window_w, window_h), pygame.SRCALPHA)
        window_surface.fill((10, 15, 40, 230))
        pygame.draw.rect(window_surface, NEON_BLUE, (0, 0, window_w, window_h), 2, border_radius=10)

        title = font_medium.render("🌍 ДАННЫЕ ЗЕМЛИ", True, YELLOW)
        window_surface.blit(title, (10, 8))

        time_str = f"⏱ ВРЕМЯ: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        time_text = font_small.render(time_str, True, LIGHT_BLUE)
        window_surface.blit(time_text, (10, 35))

        days_text = font_small.render(f"📅 ДНЕЙ ПРОШЛО: {self.days}", True, LIGHT_BLUE)
        window_surface.blit(days_text, (10, 55))

        orbit_speed = "29.78 км/с"
        speed_text = font_small.render(f"🚀 ОРБИТАЛЬНАЯ СКОРОСТЬ: {orbit_speed}", True, CYAN)
        window_surface.blit(speed_text, (10, 75))

        screen.blit(window_surface, (window_x, window_y))


# ==================================================
# 3D КАМЕРА
# ==================================================

class Camera3D:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = math.radians(30)
        self.distance = 550

    def rotate(self, dx, dy):
        self.angle_x += dx * 0.006
        self.angle_y += dy * 0.006
        self.angle_y = max(-math.pi / 2.2, min(math.pi / 2.2, self.angle_y))

    def zoom(self, delta):
        self.distance = max(300, min(800, self.distance - delta))

    def project(self, x, y, z):
        cos_y = math.cos(self.angle_x)
        sin_y = math.sin(self.angle_x)
        x1 = x * cos_y + z * sin_y
        z1 = z * cos_y - x * sin_y

        cos_x = math.cos(self.angle_y)
        sin_x = math.sin(self.angle_y)
        y1 = y * cos_x - z1 * sin_x
        z2 = z1 * cos_x + y * sin_x

        scale = 500 / (self.distance + z2)
        sx = WIDTH // 2 + int(x1 * scale)
        sy = HEIGHT // 2 - int(y1 * scale)

        return sx, sy, scale


# ==================================================
# ЗВЁЗДНОЕ ПОЛЕ
# ==================================================

class StarField:
    def __init__(self, num_stars=400):
        self.stars = []
        for _ in range(num_stars):
            self.stars.append({
                'x': random.randint(0, WIDTH),
                'y': random.randint(0, HEIGHT),
                'size': random.randint(1, 2),
                'twinkle': random.uniform(0, 2 * math.pi),
            })

    def update(self, time):
        for star in self.stars:
            star['twinkle'] += 0.03

    def draw(self, screen):
        for star in self.stars:
            brightness = 100 + int(100 * math.sin(star['twinkle']))
            color = (brightness, brightness, brightness)
            pygame.draw.circle(screen, color, (star['x'], star['y']), star['size'])


# ==================================================
# ЛУЧИ СОЛНЦА
# ==================================================

class SunRays:
    def __init__(self):
        self.angle = 0

    def update(self):
        self.angle += 0.01

    def draw(self, screen, cx, cy, radius):
        num_rays = 16
        for i in range(num_rays):
            angle = self.angle + (i * 2 * math.pi / num_rays)
            start_x = cx + radius * math.cos(angle)
            start_y = cy + radius * math.sin(angle)
            end_x = cx + (radius + 50) * math.cos(angle)
            end_y = cy + (radius + 50) * math.sin(angle)

            for step in range(3):
                alpha = 80 - step * 20
                step_pos = step / 2
                x = start_x + (end_x - start_x) * step_pos
                y = start_y + (end_y - start_y) * step_pos
                pygame.draw.line(screen, (255, 200, 80),
                                 (int(start_x), int(start_y)), (int(x), int(y)), 3 - step)


# ==================================================
# КРАСИВАЯ ПЛАНЕТА
# ==================================================

class BeautifulPlanet:
    def __init__(self, name, size, orbit_radius, speed, parent=None, planet_type="rocky"):
        self.name = name
        self.size = size
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.parent = parent
        self.planet_type = planet_type
        self.angle = random.uniform(0, 2 * math.pi)
        self.x = 0
        self.y = 0
        self.z = 0
        self.trail = []
        self.max_trail = 30
        self.rotation = 0

        # Цвета для разных типов планет
        self.colors = {
            "sun": (255, 220, 80),
            "earth": (50, 120, 200),
            "mars": (200, 80, 50),
            "jupiter": (180, 140, 100),
            "venus": (230, 190, 120),
            "moon": (180, 180, 190),
            "saturn": (200, 180, 120),
        }

    def update(self, speed_multiplier):
        self.angle += self.speed * speed_multiplier
        self.rotation += 0.02 * speed_multiplier
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

        if self.parent:
            self.x = self.parent.x + self.orbit_radius * math.cos(self.angle)
            self.z = self.parent.z + self.orbit_radius * math.sin(self.angle)
            self.y = self.parent.y + math.sin(self.angle * 2) * 3
        else:
            self.x = self.orbit_radius * math.cos(self.angle)
            self.z = self.orbit_radius * math.sin(self.angle)
            self.y = 0

        self.trail.append((self.x, self.y, self.z))
        if len(self.trail) > self.max_trail:
            self.trail.pop(0)

    def draw_earth(self, screen, cx, cy, radius):
        # Атмосфера
        for r in range(radius + 2, radius + 10, 2):
            alpha = max(0, 60 - r * 2)
            glow = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow, (80, 120, 200, alpha), (r, r), r)
            screen.blit(glow, (cx - r, cy - r))

        # Океан
        pygame.draw.circle(screen, self.colors["earth"], (cx, cy), radius)

        # Континенты
        continents = [
            (0.35, 0.25, 0.22, 0.18), (0.55, 0.55, 0.18, 0.14), (0.72, 0.32, 0.17, 0.11),
            (0.25, 0.68, 0.15, 0.11), (0.78, 0.68, 0.13, 0.09), (0.45, 0.40, 0.10, 0.08)
        ]
        for x_off, y_off, w, h in continents:
            px = cx + int((x_off - 0.5) * radius * 2)
            py = cy + int((y_off - 0.5) * radius * 2)
            pygame.draw.ellipse(screen, LAND_GREEN, (px - int(w * radius), py - int(h * radius),
                                                     int(w * radius * 2), int(h * radius * 2)))

        # Облака
        clouds = [(0.2, 0.3, 0.10), (0.6, 0.2, 0.08), (0.4, 0.7, 0.12), (0.8, 0.5, 0.07)]
        for x_off, y_off, size in clouds:
            cloud = pygame.Surface((int(size * radius * 2), int(size * radius * 2)), pygame.SRCALPHA)
            pygame.draw.ellipse(cloud, (255, 255, 255, 100), cloud.get_rect())
            screen.blit(cloud, (cx + int((x_off - 0.5) * radius * 2) - int(size * radius),
                                cy + int((y_off - 0.5) * radius * 2) - int(size * radius)))

        # Блик
        pygame.draw.circle(screen, WHITE, (cx - radius // 3, cy - radius // 3), max(2, radius // 6))

    def draw_jupiter(self, screen, cx, cy, radius):
        # Полосы Юпитера
        pygame.draw.circle(screen, self.colors["jupiter"], (cx, cy), radius)
        for i in range(3):
            y_offset = cy - radius // 2 + i * radius // 3
            pygame.draw.ellipse(screen, (140, 100, 70), (cx - radius, y_offset, radius * 2, radius // 4))

        # Большое красное пятно
        pygame.draw.ellipse(screen, (180, 60, 50), (cx + radius // 4, cy + radius // 6, radius // 3, radius // 5))
        pygame.draw.circle(screen, WHITE, (cx - radius // 3, cy - radius // 3), max(2, radius // 6))

    def draw_saturn(self, screen, cx, cy, radius):
        pygame.draw.circle(screen, self.colors["saturn"], (cx, cy), radius)
        # Кольца
        for offset in [-2, 0, 2]:
            pygame.draw.ellipse(screen, (180, 160, 100),
                                (cx - radius * 1.6, cy - radius // 3 + offset, radius * 3.2, radius // 2 + 5), 2)
        pygame.draw.circle(screen, WHITE, (cx - radius // 3, cy - radius // 3), max(2, radius // 6))

    def draw_mars(self, screen, cx, cy, radius):
        pygame.draw.circle(screen, self.colors["mars"], (cx, cy), radius)
        # Темные области
        for i in range(3):
            spot_x = cx + random.randint(-radius // 2, radius // 2)
            spot_y = cy + random.randint(-radius // 2, radius // 2)
            pygame.draw.circle(screen, (120, 50, 30), (spot_x, spot_y), radius // 5)
        pygame.draw.circle(screen, WHITE, (cx - radius // 3, cy - radius // 3), max(2, radius // 6))

    def draw_venus(self, screen, cx, cy, radius):
        pygame.draw.circle(screen, self.colors["venus"], (cx, cy), radius)
        # Облака Венеры (вихревые узоры)
        for i in range(4):
            angle = i * math.pi / 2
            x1 = cx + int(radius * 0.6 * math.cos(angle))
            y1 = cy + int(radius * 0.6 * math.sin(angle))
            pygame.draw.ellipse(screen, (200, 160, 100), (x1 - radius // 4, y1 - radius // 8, radius // 2, radius // 4))
        pygame.draw.circle(screen, WHITE, (cx - radius // 3, cy - radius // 3), max(2, radius // 6))

    def draw_moon(self, screen, cx, cy, radius):
        pygame.draw.circle(screen, self.colors["moon"], (cx, cy), radius)
        # Кратеры
        for i in range(6):
            crater_x = cx + random.randint(-radius // 2, radius // 2)
            crater_y = cy + random.randint(-radius // 2, radius // 2)
            crater_r = max(2, radius // 6)
            pygame.draw.circle(screen, MOON_CRATER, (crater_x, crater_y), crater_r)
            pygame.draw.circle(screen, (200, 200, 210), (crater_x - 1, crater_y - 1), crater_r - 1, 1)
        pygame.draw.circle(screen, WHITE, (cx - radius // 4, cy - radius // 4), max(2, radius // 8))

    def draw_sun(self, screen, cx, cy, radius):
        # Солнце с градиентом
        for r in range(radius, 0, -5):
            intensity = 255 - (radius - r) * 3
            intensity = max(100, min(255, intensity))
            color = (255, min(200, intensity), min(100, intensity // 2))
            pygame.draw.circle(screen, color, (cx, cy), r)

    def draw(self, screen, camera, show_trail=True):
        sx, sy, scale = camera.project(self.x, self.y, self.z)
        radius = int(self.size * scale)

        if radius < 2:
            return None

        # Рисуем в зависимости от типа
        if self.planet_type == "sun":
            self.draw_sun(screen, sx, sy, radius)
        elif self.planet_type == "earth":
            self.draw_earth(screen, sx, sy, radius)
        elif self.planet_type == "mars":
            self.draw_mars(screen, sx, sy, radius)
        elif self.planet_type == "jupiter":
            self.draw_jupiter(screen, sx, sy, radius)
        elif self.planet_type == "venus":
            self.draw_venus(screen, sx, sy, radius)
        elif self.planet_type == "moon":
            self.draw_moon(screen, sx, sy, radius)
        elif self.planet_type == "saturn":
            self.draw_saturn(screen, sx, sy, radius)
        else:
            pygame.draw.circle(screen, (100, 100, 150), (sx, sy), radius)

        # Трек
        if show_trail and len(self.trail) > 1:
            for i in range(1, len(self.trail)):
                x1, y1, z1 = self.trail[i - 1]
                x2, y2, z2 = self.trail[i]
                sx1, sy1, _ = camera.project(x1, y1, z1)
                sx2, sy2, _ = camera.project(x2, y2, z2)
                alpha = int(100 * i / len(self.trail))
                pygame.draw.line(screen, (200, 200, 200), (sx1, sy1), (sx2, sy2), 1)

        return (sx, sy, radius, self.x, self.y, self.z)


# ==================================================
# СОЛНЕЧНАЯ СИСТЕМА
# ==================================================

class SolarSystem:
    def __init__(self):
        self.sun = BeautifulPlanet("Солнце", 45, 0, 0, planet_type="sun")
        self.earth = BeautifulPlanet("Земля", 18, 240, 0.08, self.sun, "earth")
        self.moon = BeautifulPlanet("Луна", 7, 70, 0.6, self.earth, "moon")
        self.mars = BeautifulPlanet("Марс", 14, 320, 0.06, self.sun, "mars")
        self.jupiter = BeautifulPlanet("Юпитер", 30, 430, 0.04, self.sun, "jupiter")
        self.venus = BeautifulPlanet("Венера", 16, 170, 0.1, self.sun, "venus")
        self.saturn = BeautifulPlanet("Сатурн", 26, 530, 0.03, self.sun, "saturn")

        self.planets = [self.sun, self.earth, self.moon, self.mars, self.jupiter, self.venus, self.saturn]
        self.sun_rays = SunRays()

    def update(self, speed_multiplier, paused):
        if not paused:
            for planet in self.planets:
                planet.update(speed_multiplier)
        self.sun_rays.update()

    def reset(self):
        for planet in self.planets:
            planet.angle = 0
            planet.trail = []

    def check_click(self, pos, camera):
        for planet in self.planets:
            result = planet.draw(screen, camera, False)
            if result:
                sx, sy, radius, _, _, _ = result
                dx = pos[0] - sx
                dy = pos[1] - sy
                if dx * dx + dy * dy <= radius * radius:
                    return planet.name
        return None

    def draw(self, screen, camera, show_trails):
        # Солнце со свечением
        sun_info = self.sun.draw(screen, camera, False)
        if sun_info:
            sx, sy, radius, _, _, _ = sun_info
            self.sun_rays.draw(screen, sx, sy, radius)

        # Планеты
        infos = []
        for planet in self.planets:
            info = planet.draw(screen, camera, show_trails)
            infos.append(info)

        # Орбиты
        for planet in [self.earth, self.mars, self.jupiter, self.venus, self.saturn]:
            if planet.orbit_radius > 0:
                orbit_points = []
                for angle in range(0, 360, 20):
                    rad = math.radians(angle)
                    x = planet.orbit_radius * math.cos(rad)
                    z = planet.orbit_radius * math.sin(rad)
                    sx, sy, _ = camera.project(x, 0, z)
                    orbit_points.append((sx, sy))
                if len(orbit_points) > 1:
                    pygame.draw.lines(screen, (60, 60, 80), True, orbit_points, 1)

        return infos


# ==================================================
# КООРДИНАТЫ
# ==================================================

def draw_coordinates(screen, planet_infos):
    y_offset = 10
    title = font_coord.render("КООРДИНАТЫ (X, Y, Z)", True, CYAN)
    screen.blit(title, (10, y_offset))
    y_offset += 18

    names = ["☀️ Солнце", "🌍 Земля", "🌙 Луна", "🔴 Марс", "🪐 Юпитер", "🟡 Венера"]
    for i, info in enumerate(planet_infos[:6]):
        if info:
            _, _, _, x, y, z = info
            if abs(x) < 1000:
                text = font_coord.render(f"{names[i]}: X={int(x):4d} Y={int(y):4d} Z={int(z):4d}", True, LIGHT_BLUE)
                screen.blit(text, (10, y_offset))
                y_offset += 16
                if y_offset > 150:
                    break

    pygame.draw.rect(screen, NEON_BLUE, (5, 5, 320, y_offset + 5), 1, border_radius=5)


# ==================================================
# АНИМАЦИЯ ВХОДА
# ==================================================

class IntroAnimation:
    def __init__(self):
        self.stars = []
        self.alpha = 0
        self.phase = 0  # 0: появление, 1: ожидание, 2: исчезновение

        for _ in range(150):
            self.stars.append({
                'x': random.randint(0, WIDTH),
                'y': random.randint(0, HEIGHT),
                'size': random.randint(1, 3),
                'twinkle': random.uniform(0, 2 * math.pi)
            })

        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.start_time

        if elapsed < 1500:
            self.alpha = min(255, int(elapsed / 1500 * 255))
            self.phase = 0
        elif elapsed < 3000:
            self.alpha = 255
            self.phase = 1
        else:
            self.alpha = max(0, 255 - int((elapsed - 3000) / 1000 * 255))
            self.phase = 2

        # Мерцание звёзд
        for star in self.stars:
            star['twinkle'] += 0.03

        return elapsed > 4000

    def draw(self, screen):
        screen.fill(DEEP_SPACE)

        # Звёзды
        for star in self.stars:
            brightness = 100 + int(100 * math.sin(star['twinkle']))
            color = (brightness, brightness, brightness)
            pygame.draw.circle(screen, color, (star['x'], star['y']), star['size'])

        # Логотип
        title = font_magic.render("АКВТ", True, (255, 215, 0))
        title.set_alpha(self.alpha)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(title, title_rect)

        subtitle = font_large.render("КОСМИЧЕСКИЙ ЦЕНТР УПРАВЛЕНИЯ", True, NEON_BLUE)
        subtitle.set_alpha(self.alpha)
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(subtitle, subtitle_rect)

        footer = font_small.render("Астраханский колледж вычислительной техники", True, GRAY)
        footer.set_alpha(self.alpha)
        footer_rect = footer.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(footer, footer_rect)

        # Прогресс
        if self.phase == 0:
            progress = self.alpha / 255
            bar_width = int(WIDTH * progress)
            pygame.draw.rect(screen, NEON_BLUE, (0, HEIGHT - 3, bar_width, 3))


# ==================================================
# ОСНОВНАЯ СИМУЛЯЦИЯ
# ==================================================

def run_simulation():
    stars = StarField(400)
    solar_system = SolarSystem()
    control_panel = ControlPanel()
    earth_time = EarthTimeDisplay()
    planet_info = PlanetInfoWindow()
    camera = Camera3D()

    running = True
    time_var = 0

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    control_panel.paused = not control_panel.paused
                    control_panel.pause_btn.text = "СТАРТ" if control_panel.paused else "ПАУЗА"
                if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                    control_panel.speed = min(2.0, control_panel.speed + 0.1)
                if event.key == pygame.K_MINUS:
                    control_panel.speed = max(0.2, control_panel.speed - 0.1)
                if event.key == pygame.K_r:
                    solar_system.reset()
                    control_panel.speed = 1.0
                    control_panel.paused = False
                    control_panel.pause_btn.text = "ПАУЗА"
                if event.key == pygame.K_t:
                    control_panel.show_trails = not control_panel.show_trails
                if event.key == pygame.K_s:
                    control_panel.show_stars = not control_panel.show_stars
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    camera.rotate(event.rel[0], event.rel[1])
            elif event.type == pygame.MOUSEWHEEL:
                camera.zoom(event.y * 30)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not planet_info.handle_click(event.pos):
                        result = control_panel.handle_click(event.pos)
                        if result == "reset":
                            solar_system.reset()
                            control_panel.speed = 1.0
                            control_panel.paused = False
                            control_panel.pause_btn.text = "ПАУЗА"
                        elif result is None:
                            planet_name = solar_system.check_click(event.pos, camera)
                            if planet_name:
                                planet_info.show(planet_name)

        # Обновление панели
        control_panel.update(mouse_pos)

        # Обновление системы
        solar_system.update(control_panel.speed, control_panel.paused)
        earth_time.update(control_panel.speed, control_panel.paused)

        # Отрисовка
        screen.fill(DEEP_SPACE)

        if control_panel.show_stars:
            stars.update(time_var)
            stars.draw(screen)

        planet_infos = solar_system.draw(screen, camera, control_panel.show_trails)
        control_panel.draw(screen)
        earth_time.draw(screen)
        planet_info.draw(screen)
        draw_coordinates(screen, planet_infos)

        # Подсказки
        help_text = font_small.render("ЛКМ+Мышь - вращать | Колёсико - зум | Клик по планете - инфо | ESC - выход",
                                      True, DARK_GRAY)
        screen.blit(help_text, (10, HEIGHT - 20))

        # Горячие клавиши
        hotkeys = font_small.render("Пробел - пауза | +/- - скорость | R - сброс | T - треки | S - звёзды", True,
                                    DARK_GRAY)
        screen.blit(hotkeys, (10, HEIGHT - 35))

        fps = font_small.render(f"FPS: {int(clock.get_fps())}", True, DARK_GRAY)
        screen.blit(fps, (WIDTH - 60, 10))

        pygame.display.flip()
        time_var += 0.05
        clock.tick(60)

    return running


# ==================================================
# ЗАПУСК
# ==================================================

if __name__ == "__main__":
    # Анимация входа
    intro = IntroAnimation()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    intro.start_time = 0
                    intro.phase = 2

        completed = intro.update()
        intro.draw(screen)
        pygame.display.flip()
        clock.tick(60)

        if completed:
            break

    # Запуск симуляции
    run_simulation()
    pygame.quit()
    sys.exit()
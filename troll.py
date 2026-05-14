import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

products = [
    {"id": 1, "name": "AK-47 | Тактическая", "price": 45990, "category": "Штурмовые винтовки", "damage": 48,
     "desc": "Легендарный автомат Калашникова"},
    {"id": 2, "name": "M4A1 | Коммандос", "price": 38990, "category": "Штурмовые винтовки", "damage": 42,
     "desc": "Американская штурмовая винтовка"},
    {"id": 3, "name": "SCAR-H", "price": 52990, "category": "Штурмовые винтовки", "damage": 52,
     "desc": "Бельгийская разработка для спецназа"},
    {"id": 4, "name": "AUG A3", "price": 34990, "category": "Штурмовые винтовки", "damage": 40,
     "desc": "Австрийская винтовка булл-пап"},
    {"id": 5, "name": "FAMAS", "price": 39990, "category": "Штурмовые винтовки", "damage": 41,
     "desc": "Французская штурмовая винтовка"},
    {"id": 6, "name": "G36C", "price": 37990, "category": "Штурмовые винтовки", "damage": 40,
     "desc": "Немецкая компактная винтовка"},
    {"id": 7, "name": "AN-94", "price": 49990, "category": "Штурмовые винтовки", "damage": 44,
     "desc": "Российская винтовка с отложенным импульсом"},
    {"id": 8, "name": "Glock 18C", "price": 12990, "category": "Пистолеты", "damage": 28,
     "desc": "Автоматический пистолет"},
    {"id": 9, "name": "Desert Eagle", "price": 24990, "category": "Пистолеты", "damage": 65,
     "desc": "Магнум .50 калибра"},
    {"id": 10, "name": "Beretta 92FS", "price": 9990, "category": "Пистолеты", "damage": 32,
     "desc": "Армейский пистолет США"},
    {"id": 11, "name": "FN Five-Seven", "price": 14990, "category": "Пистолеты", "damage": 35,
     "desc": "Бронебойные патроны"},
    {"id": 12, "name": "Sig Sauer P320", "price": 11990, "category": "Пистолеты", "damage": 30,
     "desc": "Модульный пистолет армии США"},
    {"id": 13, "name": "CZ-75", "price": 10990, "category": "Пистолеты", "damage": 31, "desc": "Чешский пистолет"},
    {"id": 14, "name": "Makarov PM", "price": 7990, "category": "Пистолеты", "damage": 29,
     "desc": "Советский компактный пистолет"},
    {"id": 15, "name": "AWM", "price": 89990, "category": "Снайперские винтовки", "damage": 95,
     "desc": "Британская снайперская винтовка"},
    {"id": 16, "name": "SVD", "price": 67990, "category": "Снайперские винтовки", "damage": 72,
     "desc": "Снайперская винтовка Драгунова"},
    {"id": 17, "name": "M24", "price": 54990, "category": "Снайперские винтовки", "damage": 85,
     "desc": "Американская винтовка"},
    {"id": 18, "name": "Barrett M82", "price": 129990, "category": "Снайперские винтовки", "damage": 120,
     "desc": "Крупнокалиберная винтовка"},
    {"id": 19, "name": "Benelli M4", "price": 42990, "category": "Дробовики", "damage": 85,
     "desc": "Итальянский полуавтомат"},
    {"id": 20, "name": "Mossberg 590", "price": 35990, "category": "Дробовики", "damage": 80,
     "desc": "Тактический дробовик"},
    {"id": 21, "name": "Saiga-12", "price": 49990, "category": "Дробовики", "damage": 82,
     "desc": "Российский самозарядный дробовик"},
    {"id": 22, "name": "M249 SAW", "price": 78990, "category": "Пулеметы", "damage": 45, "desc": "Ручной пулемёт США"},
    {"id": 23, "name": "PKM", "price": 69990, "category": "Пулеметы", "damage": 48, "desc": "Российский пулемёт"},
    {"id": 24, "name": "Катана", "price": 19990, "category": "Холодное оружие", "damage": 55,
     "desc": "Японский меч самурая"},
    {"id": 25, "name": "Тактический нож", "price": 4990, "category": "Холодное оружие", "damage": 25,
     "desc": "Многофункциональный нож"},
    {"id": 26, "name": "Кунай", "price": 4990, "category": "Холодное оружие", "damage": 25, "desc": "Метательный нож"},
    {"id": 27, "name": "Оптический прицел", "price": 15990, "category": "Аксессуары", "damage": 0,
     "desc": "Увеличивает дальность"},
    {"id": 28, "name": "Глушитель", "price": 8990, "category": "Аксессуары", "damage": 0,
     "desc": "Снижает шум выстрела"},
    {"id": 29, "name": "Красный лазер", "price": 4990, "category": "Аксессуары", "damage": 0,
     "desc": "Повышает точность"},
    {"id": 30, "name": "Коллиматор", "price": 12990, "category": "Аксессуары", "damage": 0,
     "desc": "Быстрое прицеливание"},
]


class RGBBackground(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.hue = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        import math
        r = int((math.sin(self.hue * 0.008) + 1) * 127.5)
        g = int((math.sin((self.hue + 120) * 0.008) + 1) * 127.5)
        b = int((math.sin((self.hue + 240) * 0.008) + 1) * 127.5)

        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(r, g, b, 200))
        gradient.setColorAt(0.33, QColor(g, b, r, 200))
        gradient.setColorAt(0.66, QColor(b, r, g, 200))
        gradient.setColorAt(1, QColor(r, g, b, 200))

        painter.fillRect(self.rect(), QBrush(gradient))
        self.hue = (self.hue + 1) % 360


class MilitaryShop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌈 NEON ARMORY ULTRA HD | RGB CYBERPUNK 🌈")
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("QMainWindow { background-color: #000000; }")

        self.cart = {}

        # RGB фон
        self.rgb_bg = RGBBackground(self)
        self.rgb_bg.setGeometry(0, 0, 1920, 1080)

        # Главный контейнер
        central = QWidget()
        central.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(35, 35, 35, 35)
        main_layout.setSpacing(30)

        # ===== ЛЕВАЯ ПАНЕЛЬ =====
        left_panel = QWidget()
        left_panel.setFixedWidth(360)
        left_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 180);
                border-radius: 30px;
                border: 2px solid rgba(255, 0, 255, 100);
            }
        """)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(25)
        left_layout.setContentsMargins(20, 25, 20, 25)

        # Заголовок
        self.title_label = QLabel("⚡ NEON\nARMORY ⚡\nULTRA HD")
        self.title_label.setStyleSheet("font-size: 36px; font-weight: bold; padding: 20px;")
        self.title_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(self.title_label)

        # Поиск
        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍 ПОИСК ОРУЖИЯ...")
        self.search.setMinimumHeight(55)
        self.search.setStyleSheet("""
            QLineEdit {
                background-color: rgba(30, 30, 50, 220);
                border: 2px solid rgba(0, 255, 255, 100);
                border-radius: 20px;
                padding: 15px 20px;
                color: #ffffff;
                font-size: 15px;
                font-weight: bold;
            }
            QLineEdit:focus {
                border: 2px solid #ff00ff;
            }
        """)
        self.search.textChanged.connect(self.filter_products)
        left_layout.addWidget(self.search)

        # Категории
        cat_label = QLabel("📀 КАТЕГОРИИ")
        cat_label.setStyleSheet("color: #00ffff; font-weight: bold; font-size: 18px; margin-left: 8px;")
        left_layout.addWidget(cat_label)

        self.cat_list = QListWidget()
        categories = ["◈ ВСЕ ТОВАРЫ", "◈ ШТУРМОВЫЕ ВИНТОВКИ", "◈ ПИСТОЛЕТЫ", "◈ СНАЙПЕРСКИЕ",
                      "◈ ДРОБОВИКИ", "◈ ПУЛЕМЕТЫ", "◈ ХОЛОДНОЕ", "◈ АКСЕССУАРЫ"]
        for cat in categories:
            self.cat_list.addItem(cat)
        self.cat_list.setStyleSheet("""
            QListWidget {
                background-color: rgba(30, 30, 50, 200);
                border: 2px solid rgba(255, 0, 255, 50);
                border-radius: 20px;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 14px;
                color: #dddddd;
            }
            QListWidget::item:selected {
                background-color: #ff00ff;
                color: #ffffff;
                border-radius: 12px;
            }
            QListWidget::item:hover {
                background-color: rgba(255, 0, 255, 0.3);
            }
        """)
        self.cat_list.currentRowChanged.connect(self.filter_products)
        left_layout.addWidget(self.cat_list)

        # Статистика
        stats_frame = QWidget()
        stats_frame.setStyleSheet("background-color: rgba(30, 30, 50, 180); border-radius: 20px;")
        stats_layout = QVBoxLayout(stats_frame)
        stats_layout.setContentsMargins(15, 15, 15, 15)

        self.count_label = QLabel(f"📦 В НАЛИЧИИ: {len(products)}")
        self.count_label.setStyleSheet("color: #00ff00; font-size: 15px; font-weight: bold;")
        stats_layout.addWidget(self.count_label)

        self.cart_label = QLabel("🛒 В КОРЗИНЕ: 0")
        self.cart_label.setStyleSheet("color: #ffaa00; font-size: 15px; font-weight: bold;")
        stats_layout.addWidget(self.cart_label)

        left_layout.addWidget(stats_frame)
        left_layout.addStretch()

        # ===== ЦЕНТР =====
        center_panel = QWidget()
        center_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 160);
                border-radius: 30px;
                border: 2px solid rgba(0, 255, 255, 80);
            }
        """)
        center_layout = QVBoxLayout(center_panel)
        center_layout.setContentsMargins(20, 20, 20, 20)
        center_layout.setSpacing(15)

        header = QLabel("💀 АКТУАЛЬНОЕ ВООРУЖЕНИЕ 💀")
        header.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #ffffff; padding: 15px; background-color: rgba(255, 0, 255, 70); border-radius: 25px;")
        header.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(header)

        # Таблица
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["⚔ НАЗВАНИЕ", "📁 ТИП", "💰 ЦЕНА", "💥 УРОН", "✨ ДЕЙСТВИЕ"])
        self.table.setColumnWidth(0, 380)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 160)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 180)
        self.table.setAlternatingRowColors(True)
        self.table.setMinimumHeight(700)
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: rgba(20, 20, 40, 200);
                alternate-background-color: rgba(35, 35, 60, 200);
                border: none;
                gridline-color: rgba(255, 255, 255, 20);
            }
            QTableWidget::item {
                padding: 18px;
                color: #e0e0e0;
                font-size: 14px;
            }
            QTableWidget::item:selected {
                background-color: #ff00ff;
                color: #ffffff;
            }
            QHeaderView::section {
                background-color: rgba(255, 0, 255, 120);
                padding: 18px;
                font-weight: bold;
                color: #ffffff;
                font-size: 14px;
                border: none;
            }
        """)
        center_layout.addWidget(self.table)

        # ===== ПРАВАЯ ПАНЕЛЬ =====
        right_panel = QWidget()
        right_panel.setFixedWidth(480)
        right_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 180);
                border-radius: 30px;
                border: 2px solid rgba(255, 0, 255, 100);
            }
        """)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(20)
        right_layout.setContentsMargins(20, 25, 20, 25)

        cart_title = QLabel("🛸 КОРЗИНА ПОКУПОК 🛸")
        cart_title.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #ffffff; padding: 15px; background-color: rgba(0, 255, 255, 70); border-radius: 25px;")
        cart_title.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(cart_title)

        self.cart_list = QListWidget()
        self.cart_list.setMinimumHeight(550)
        self.cart_list.setStyleSheet("""
            QListWidget {
                background-color: rgba(30, 30, 50, 200);
                border: 2px solid rgba(0, 255, 255, 50);
                border-radius: 20px;
                padding: 10px;
            }
            QListWidget::item {
                padding: 18px;
                color: #dddddd;
                border-bottom: 1px solid rgba(255, 255, 255, 20);
                font-size: 14px;
            }
        """)
        right_layout.addWidget(self.cart_list)

        self.total_label = QLabel("💰 ИТОГО: 0 ₽")
        self.total_label.setStyleSheet(
            "font-size: 28px; font-weight: bold; color: #ffffff; padding: 20px; background-color: rgba(255, 0, 255, 100); border-radius: 25px;")
        self.total_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(self.total_label)

        # Кнопки (ФИКСИРОВАННЫЕ, НЕ ПЛЫВУТ)
        btn_checkout = QPushButton("💎 ОФОРМИТЬ ЗАКАЗ 💎")
        btn_checkout.setFixedHeight(60)
        btn_checkout.setStyleSheet("""
            QPushButton {
                background-color: #ff00ff;
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #00ffff;
                color: #000000;
            }
        """)
        btn_checkout.clicked.connect(self.checkout)
        right_layout.addWidget(btn_checkout)

        btn_clear = QPushButton("🗑 ОЧИСТИТЬ КОРЗИНУ 🗑")
        btn_clear.setFixedHeight(55)
        btn_clear.setStyleSheet("""
            QPushButton {
                background-color: #ff3300;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #ff6600;
            }
        """)
        btn_clear.clicked.connect(self.clear_cart)
        right_layout.addWidget(btn_clear)

        main_layout.addWidget(left_panel)
        main_layout.addWidget(center_panel, 1)
        main_layout.addWidget(right_panel)

        # Таймер для RGB заголовка
        self.hue = 0
        self.title_timer = QTimer()
        self.title_timer.timeout.connect(self.update_title_color)
        self.title_timer.start(50)

        self.load_products()

    def resizeEvent(self, event):
        self.rgb_bg.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def update_title_color(self):
        self.hue = (self.hue + 2) % 360
        r = int(self.hue / 360 * 255)
        g = int(((self.hue + 120) % 360) / 360 * 255)
        b = int(((self.hue + 240) % 360) / 360 * 255)
        color = f"#{r:02x}{g:02x}{b:02x}"
        self.title_label.setStyleSheet(f"font-size: 36px; font-weight: bold; padding: 20px; color: {color};")

    def load_products(self, category="◈ ВСЕ ТОВАРЫ", search=""):
        self.table.setRowCount(0)

        cat_map = {
            "◈ ВСЕ ТОВАРЫ": "Все",
            "◈ ШТУРМОВЫЕ ВИНТОВКИ": "Штурмовые винтовки",
            "◈ ПИСТОЛЕТЫ": "Пистолеты",
            "◈ СНАЙПЕРСКИЕ": "Снайперские винтовки",
            "◈ ДРОБОВИКИ": "Дробовики",
            "◈ ПУЛЕМЕТЫ": "Пулеметы",
            "◈ ХОЛОДНОЕ": "Холодное оружие",
            "◈ АКСЕССУАРЫ": "Аксессуары"
        }

        cat_clean = cat_map.get(category, "Все")

        filtered = []
        for p in products:
            if cat_clean != "Все" and p['category'] != cat_clean:
                continue
            if search and search.lower() not in p['name'].lower():
                continue
            filtered.append(p)

        self.table.setRowCount(len(filtered))

        for i, p in enumerate(filtered):
            # Название
            name_item = QTableWidgetItem(f"🔫 {p['name']}")
            name_item.setToolTip(p['desc'])
            self.table.setItem(i, 0, name_item)

            # Категория
            self.table.setItem(i, 1, QTableWidgetItem(p['category']))

            # Цена
            price_item = QTableWidgetItem(f"{p['price']:,} ₽")
            price_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.table.setItem(i, 2, price_item)

            # Урон
            damage_item = QTableWidgetItem(str(p['damage']))
            damage_item.setTextAlignment(Qt.AlignCenter)
            if p['damage'] >= 85:
                damage_item.setForeground(QColor(255, 80, 80))
            elif p['damage'] >= 40:
                damage_item.setForeground(QColor(80, 255, 80))
            else:
                damage_item.setForeground(QColor(80, 180, 255))
            self.table.setItem(i, 3, damage_item)

            # Кнопка покупки (ФИКСИРОВАННАЯ)
            btn_widget = QWidget()
            btn_layout = QHBoxLayout(btn_widget)
            btn_layout.setContentsMargins(0, 0, 0, 0)

            buy_btn = QPushButton("✨ ВЗЯТЬ ✨")
            buy_btn.setFixedSize(130, 42)
            buy_btn.setStyleSheet("""
                QPushButton {
                    background-color: #00ffff;
                    color: #000000;
                    font-weight: bold;
                    border-radius: 15px;
                    font-size: 13px;
                }
                QPushButton:hover {
                    background-color: #ff00ff;
                    color: #ffffff;
                }
            """)
            buy_btn.clicked.connect(lambda checked, x=p: self.add_to_cart(x))

            btn_layout.addWidget(buy_btn)
            btn_layout.setAlignment(Qt.AlignCenter)
            self.table.setCellWidget(i, 4, btn_widget)

        self.count_label.setText(f"📦 В НАЛИЧИИ: {len(filtered)}")

    def filter_products(self):
        category = "◈ ВСЕ ТОВАРЫ"
        if self.cat_list.currentItem():
            category = self.cat_list.currentItem().text()
        self.load_products(category, self.search.text())

    def add_to_cart(self, product):
        pid = product['id']
        if pid in self.cart:
            self.cart[pid]['qty'] += 1
        else:
            self.cart[pid] = {'product': product, 'qty': 1}
        self.update_cart()

        msg = QMessageBox(self)
        msg.setWindowTitle("✅ ДОБАВЛЕНО")
        msg.setText(f"✨ {product['name']} ✨\n\nдобавлен в корзину!\n💰 {product['price']:,} ₽")
        msg.setStyleSheet("""
            QMessageBox { background-color: #1a1a2e; }
            QMessageBox QLabel { color: #ffffff; font-size: 14px; }
            QPushButton { background-color: #ff00ff; color: #ffffff; padding: 12px 24px; border-radius: 15px; font-weight: bold; }
        """)
        msg.exec_()

    def update_cart(self):
        self.cart_list.clear()
        total = 0
        items = 0

        for data in self.cart.values():
            p = data['product']
            qty = data['qty']
            subtotal = p['price'] * qty
            total += subtotal
            items += qty

            self.cart_list.addItem(f"🔫 {p['name'][:32]}  ✖ {qty}  =  {subtotal:>13,} ₽")

        self.total_label.setText(f"💰 ИТОГО: {total:>15,} ₽")
        self.cart_label.setText(f"🛒 В КОРЗИНЕ: {items}")

    def clear_cart(self):
        reply = QMessageBox.question(self, "⚠️ ОЧИСТКА", "ОЧИСТИТЬ ВСЮ КОРЗИНУ?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cart.clear()
            self.update_cart()

    def checkout(self):
        if not self.cart:
            QMessageBox.warning(self, "⚠️ ОШИБКА", "КОРЗИНА ПУСТА!")
            return

        total = sum(d['qty'] * d['product']['price'] for d in self.cart.values())
        receipt = "═" * 55 + "\n"
        receipt += "                🧾 ЗАКАЗ ОФОРМЛЕН 🧾\n"
        receipt += "═" * 55 + "\n\n"

        for d in self.cart.values():
            p = d['product']
            receipt += f"🔫 {p['name'][:38]}\n"
            receipt += f"                    ✖ {d['qty']} шт.  =  {p['price'] * d['qty']:>13,} ₽\n\n"

        receipt += "═" * 55 + "\n"
        receipt += f"                    💰 ИТОГО: {total:>18,} ₽\n"
        receipt += "═" * 55 + "\n\n"
        receipt += "                    Спасибо за покупку!\n"
        receipt += "                    🌈 NEON ARMORY ULTRA HD 🌈"

        msg = QMessageBox(self)
        msg.setWindowTitle("✅ ЗАКАЗ ПОДТВЕРЖДЁН")
        msg.setText(receipt)
        msg.setStyleSheet("""
            QMessageBox { background-color: #0a0a0f; }
            QMessageBox QLabel { color: #00ffff; font-size: 14px; font-family: monospace; }
            QPushButton { background-color: #ff00ff; color: #ffffff; padding: 14px 28px; border-radius: 18px; font-weight: bold; font-size: 14px; }
        """)
        msg.exec_()

        self.cart.clear()
        self.update_cart()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MilitaryShop()
    window.showFullScreen()
    sys.exit(app.exec_())
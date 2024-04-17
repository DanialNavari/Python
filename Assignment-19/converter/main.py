import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui_main import Ui_mainWindow


class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.cal.clicked.connect(self.getItem)
        self.ui.combo_units.currentTextChanged.connect(self.changeUnit)
        self.ui.combo_from.currentTextChanged.connect(self.changeFrom)

        self.unit = {
            "وزن": ["گرم", "کیلوگرم", "تن", "پوند"],
            "طول": ["میلی متر", "سانتی متر", "متر", "کیلومتر", "اینچ"],
            "دما": ["سانتی گراد", "فارنهایت", "کلوین"],
            "حجم دیجیتالی": [
                "بیت",
                "بایت",
                "کیلوبایت",
                "مگابایت",
                "گیگابایت",
                "ترابایت",
            ],
        }

        self.unit_tabdil = {
            "وزن": {
                "گرم": 1,
                "کیلوگرم": 1000,
                "تن": 1000000,
                "پوند": 500,
            },
            "طول": {
                "میلی متر": 1,
                "سانتی متر": 10,
                "متر": 1000,
                "کیلومتر": 1000000,
                "اینچ": 25.4,
            },
            "دما": {"سانتی گراد": 1, "فارنهایت": 32, "کلوین": -273.15},
            "حجم دیجیتالی": {
                "بیت": 1,
                "بایت": 8,
                "کیلوبایت": 8000,
                "مگابایت": 8000000,
                "گیگابایت": 8000000000,
                "ترابایت": 8000000000000,
            },
        }

    def getItem(self):
        comboUnit = str(self.ui.combo_units.currentText())
        comboFrom = str(self.ui.combo_from.currentText())
        comboTo = str(self.ui.combo_to.currentText())
        from_num = int(self.ui.text_from.text())
        from_ = self.unit_tabdil[comboUnit][comboFrom]
        to_ = self.unit_tabdil[comboUnit][comboTo]

        if comboUnit == "دما":
            if comboFrom == "کلوین":
                cel_from = 273.15 + from_num
            elif comboFrom == "فارنهایت":
                cel_from = (from_num - 32) / 9.5
            else:
                cel_from = from_num

            if comboTo == "کلوین":
                cel_to = cel_from - 273.15
            elif comboTo == "فارنهایت":
                cel_to = (cel_from * 9.5) + 32
            else:
                cel_to = cel_from

            self.ui.text_to.setText(str(round(cel_to, 0)))

        else:
            tabdil = float((from_num * from_) / to_)
            self.ui.text_to.setText(str(round(tabdil, 2)))

    def changeUnit(self):
        unit_ = self.ui.combo_units.currentText()
        self.ui.combo_from.clear()
        self.ui.combo_to.clear()
        self.ui.combo_from.addItems(self.unit[unit_])

    def changeFrom(self):
        self.ui.combo_to.clear()
        unit_item = self.ui.combo_units.currentText()
        from_selected_item = self.ui.combo_from.currentIndex()
        self.ui.combo_to.addItems(self.unit[unit_item])
        self.ui.combo_to.removeItem(from_selected_item)


app = QApplication(sys.argv)

converter = Converter()
converter.changeUnit()
converter.show()

app.exec()

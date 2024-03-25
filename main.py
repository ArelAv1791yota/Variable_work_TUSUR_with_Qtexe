from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon
import method as MP_Cl
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout
import rc_Resurs_pack

# ----------------------------------------Основной класс главного блока-------------------------------------------------
class MainClass(QWidget):
    def __init__(self, width: int, height: int, parent=None):
        # Получаем ui-дизайн (без .py)
        QWidget.__init__(self, parent)
        designer_file = QFile("design.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(designer_file, self)
        designer_file.close()

        # Задаем позиционирование на экране
        self.width = width
        self.height = height
        self.setMinimumSize(width // 2, height // 2)
        self.setMaximumSize(width // 2, height // 2)
        # Растягиваем по окну
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)
        # Иконка и название внутри окна
        self.setWindowIcon(QIcon("rep_ico/ico_logo"))
        self.setWindowTitle("Shalyga_123-3P")

        # Задаем переменные
        self.nums = [1, 2, 2, -5, 5]
        self.n = 10

        # Устанавливаем zero-переменные
        self.ui.lineA.setText(str(self.nums[0]))
        self.ui.lineB.setText(str(self.nums[1]))
        self.ui.lineC.setText(str(self.nums[2]))
        self.ui.lineD.setText(str(self.nums[3]))
        self.ui.lineE.setText(str(self.nums[4]))
        self.ui.lineN.setText(str(self.n))

        # Инициализируем кнопку
        self.ui.pushButton.clicked.connect(self.calculater_button)

    # -----------------------------------Функция снятия вводимых значений с окна----------------------------------------
    def get_text(self):
        self.nums = [float(self.ui.lineA.text()), float(self.ui.lineB.text()), float(self.ui.lineC.text()),
                     (float(self.ui.lineD.text()), float(self.ui.lineE.text())), int(self.ui.lineN.text())]

    # ----------------------------------------Обращение к блоку вычисления----------------------------------------------
    def calculater_button(self):
        self.get_text()
        self.ui.lineOutMSim.setText("")
        self.ui.lineOutMLP.setText("")
        if self.ui.checkMSim.checkState():
            self.ui.lineOutMSim.setText('{:0.5f}'.format(MP_Cl.Method_Pack(self.nums).SP()))
        if self.ui.checkMLP.checkState():
            self.ui.lineOutMLP.setText('{:0.5f}'.format(MP_Cl.Method_Pack(self.nums).LP()))


# -------------------------------------2-ой этап самоинициализации проекта----------------------------------------------
def start_program():
    app = QApplication(sys.argv)
    screen_rect = app.primaryScreen().availableGeometry()
    window = MainClass(screen_rect.width(), screen_rect.height())
    window.show()
    sys.exit(app.exec_())


# -------------------------------------1-ый этап самоинициализации проекта----------------------------------------------
if __name__ == '__main__':
    start_program()

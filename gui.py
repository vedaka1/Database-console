import sys
from PyQt5 import uic, QtCore
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from main_console import *




class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)
        self.print_register_btn.clicked.connect(self.print_reg)
        self.delete_register_btn.clicked.connect(self.delete_reg)
        self.update_register_btn.clicked.connect(self.update_reg)
        self.text_field_1.setPlaceholderText('Введите id регистра')
        self.text_field_2.setPlaceholderText('Введите оценку')

    def print_reg(self):
        text = ''
        self.info_test.setText(print_register(text))

    def delete_reg(self):
        try:
            reg_id = int(self.text_field_1.text())
            delete_register(reg_id)
        except:
            print('Error')

    def update_reg(self):
        try:
            reg_id = int(self.text_field_1.text())
            mark = int(self.text_field_2.text())
            update_register(reg_id, mark)
        except:
            print('Error')


if __name__ == ("__main__"):
    app = QApplication(sys.argv)
    main_window = Main()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedWidth(900)
    widget.setFixedHeight(650)
    widget.setWindowTitle('Database')
    widget.show()
    app.exec()
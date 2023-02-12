import sys, traceback
from PyQt6 import uic, QtWidgets
from main_console import print_register, add_register, delete_register, update_register


class Update_dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("update_dialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.id_field.setPlaceholderText('id')
        self.mark_field.setPlaceholderText('mark')


class Delete_dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("delete_dialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.id_field.setPlaceholderText('id')


class Add_dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("add_dialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.student_id_field.setPlaceholderText('student id')
        self.discipline_name_field.setPlaceholderText('disclipline name')
        self.teacher_id_field.setPlaceholderText('teacher id')
        self.mark_field.setPlaceholderText('mark')


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.delete_register_btn.clicked.connect(self.delete_reg)
        self.update_register_btn.clicked.connect(self.update_reg)
        self.add_register_btn.clicked.connect(self.add_reg)
        self.print_reg()

    def print_reg(self):
        try:
            text = ''
            self.info_field.setText(print_register(text))
        except:
            print('\033[31m -- print_reg Error -- \033[0m')

    def add_reg(self):
        dlg = Add_dialog()
        try:
            if dlg.exec():
                add_register(int(dlg.student_id_field.text()),
                             str(dlg.discipline_name_field.text()),
                             int(dlg.teacher_id_field.text()),
                             int(dlg.mark_field.text()))
                self.print_reg()
                print('Success add_reg, id: ', int(dlg.id_field.text()))
            else:
                print('Canceled add_reg')
        except:
            print('\033[31m -- add_reg Error -- \033[0m',
                  traceback.format_exc())

    def delete_reg(self):
        dlg = Delete_dialog()
        try:
            if dlg.exec():
                delete_register(int(dlg.id_field.text()))
                print("Success delete_reg, id", int(dlg.id_field.text()))
                self.print_reg()
            else:
                print("Canceled delete_reg")
        except:
            print('\033[31m -- delete_reg Error -- \033[0m',
                  traceback.format_exc())

    def update_reg(self):
        dlg = Update_dialog()
        try:
            if dlg.exec():
                update_register(int(dlg.id_field.text()),
                                int(dlg.mark_field.text()))
                self.print_reg()
                print('Success update_reg, id: ', int(dlg.id_field.text()))
            else:
                print('Canceled update_dialog')
        except:
            print('\033[31m -- update_reg Error -- \033[0m',
                  traceback.format_exc())


if __name__ == ("__main__"):
    app = QtWidgets.QApplication(sys.argv)
    widget = Main()
    widget.setWindowTitle('Database')
    widget.show()
    app.exec()
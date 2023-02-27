import sys, traceback
from PyQt6 import uic, QtWidgets
from main_console import print_register, add_register, delete_register, update_register, connection


class Update_dialog(QtWidgets.QDialog):

    def __init__(self):
        super(Update_dialog, self).__init__()
        uic.loadUi("update_dialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


class Delete_dialog(QtWidgets.QDialog):

    def __init__(self):
        super(Delete_dialog, self).__init__()
        uic.loadUi("delete_dialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


class Add_dialog(QtWidgets.QDialog):

    def __init__(self):
        super(Add_dialog, self).__init__()
        uic.loadUi("add_dialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("main.ui", self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.delete_register_btn.clicked.connect(self.delete_reg)
        self.update_register_btn.clicked.connect(self.update_reg)
        self.add_register_btn.clicked.connect(self.add_reg)
        self.load_data()

    def load_data(self):
        try:
            x = 0
            items = print_register(x)
            tablerow = 0
            self.tableWidget.setRowCount(len(items))
            for row in items:
                x = [str(i) for i in list(row)]
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(x[0]))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(x[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(x[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(x[3]))
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(x[4]))
                tablerow += 1
        except:
            print('\033[31m -- load_data Error -- \033[0m', traceback.format_exc())

    def add_reg(self):
        dlg = Add_dialog()
        try:
            if dlg.exec():
                add_register(int(dlg.student_id_field.text()),
                             str(dlg.discipline_name_field.text()),
                             int(dlg.teacher_id_field.text()),
                             int(dlg.mark_field.text()))
                self.load_data()
                print('Success add_reg, id')
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
                self.load_data()
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
                self.load_data()
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
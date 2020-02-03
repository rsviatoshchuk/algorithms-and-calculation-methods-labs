from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QDesktopWidget, QFormLayout,
                             QLineEdit, QPushButton, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIntValidator
from os import remove
import linear_algorithm
import branched_algorithm
import cyclic_algorithm


class LabWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.center()

    def init_window(self):
        self.setWindowTitle("Lab1")
        self.setMinimumSize(QSize(600, 500))
        self.setStyleSheet("background-color:#2D3047; color:black; font-family: 'Open Sans Condensed'; font-size: 24px")

        tabs = QTabWidget()
        tabs.addTab(LinearAlgorithmWindow(), "Linear")
        tabs.addTab(BranchedAlgorithmWindow(), "Branched")
        tabs.addTab(CyclicAlgorithmWindow(), "Cyclic")
        tabs.setStyleSheet("background-color:#767BA3")

        vb = QVBoxLayout()
        vb.addWidget(tabs)
        self.setLayout(vb)

    def center(self):
        """function, that center window on the screen"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class LinearAlgorithmWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()

        self.linear_image_label = QLabel()
        self.linear_image_label.setPixmap(QPixmap("lab1_linear.png"))
        self.linear_image_label.setAlignment(Qt.AlignCenter)
        self.form.addWidget(self.linear_image_label)

        self.file_load_button = QPushButton("Load file")
        self.file_load_button.clicked.connect(self.load_file)
        self.form.addWidget(self.file_load_button)

        self.a_label = QLabel("a ")
        self.a_entry_field = QLineEdit()
        self.a_entry_field.textChanged.connect(self.check_float)
        self.form.addRow(self.a_label, self.a_entry_field)

        self.b_label = QLabel("b ")
        self.b_entry_field = QLineEdit()
        self.b_entry_field.textChanged.connect(self.check_float)
        self.form.addRow(self.b_label, self.b_entry_field)

        self.x_label = QLabel("x ")
        self.x_entry_field = QLineEdit()
        self.x_entry_field.textChanged.connect(self.check_float)
        self.form.addRow(self.x_label, self.x_entry_field)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_linear)
        self.form.addWidget(self.calculate_button)

        self.calculated_value_label = QLabel()
        self.calculated_value_label.hide()
        self.form.addWidget(self.calculated_value_label)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.save_to_file_button.hide()
        self.form.addWidget(self.save_to_file_button)

        self.setLayout(self.form)

    def check_float(self, text):
        try:
            if text is not "":
                float(text)
        except ValueError:
            QMessageBox().warning(self, "Invalid input", "Value must be float!", QMessageBox.Ok)

    def calculate_linear(self):
        errors = []
        try:
            a = float(self.a_entry_field.text())
        except:
            errors.append("Invalid value a")

        try:
            b = float(self.b_entry_field.text())
        except:
            errors.append("Invalid value b")

        try:
            x = float(self.x_entry_field.text())
        except:
            errors.append("Invalid value x")

        if len(errors) == 0:
            self.calculated_value_label.setText(str(linear_algorithm.linear(a, b, x)))
            self.calculated_value_label.show()
            self.save_to_file_button.show()
        else:
            QMessageBox().warning(self, "Invalid input", "\n".join(errors), QMessageBox.Ok)

    def load_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Load file")
            with open(file_name[0], "r") as file:
                self.a_entry_field.setText(file.readline().split()[1])
                self.b_entry_field.setText(file.readline().split()[1])
                self.x_entry_field.setText(file.readline().split()[1])
                self.calculated_value_label.hide()
                self.save_to_file_button.hide()
        except:
            QMessageBox().warning(self, "Error", "Shit happens")

    def save_to_file(self):
        file_name = "linear"
        counter = 1
        while True:
            try:
                with open(file_name + str(counter) + ".txt", "xt") as file:
                    file.write("a " + self.a_entry_field.text() + "\n")
                    file.write("b " + self.b_entry_field.text() + "\n")
                    file.write("x " + self.x_entry_field.text() + "\n")
                    file.write("calculated " + self.calculated_value_label.text() + "\n")

            except FileExistsError:
                counter += 1
            else:
                QMessageBox.information(self, "Info",
                                        "Successfully saved in {}".format(file_name + str(counter) + ".txt"),
                                        QMessageBox.Ok)
                break


class BranchedAlgorithmWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()

        self.branched_image_label = QLabel()
        self.branched_image_label.setPixmap(QPixmap("lab1_branched.png"))
        self.branched_image_label.setAlignment(Qt.AlignCenter)
        self.form.addWidget(self.branched_image_label)

        self.file_load_button = QPushButton("Load file")
        self.file_load_button.clicked.connect(self.load_file)
        self.form.addWidget(self.file_load_button)

        self.r_label = QLabel("r ")
        self.r_entry_field = QLineEdit()
        self.r_entry_field.textChanged.connect(self.check_float)
        self.form.addRow(self.r_label, self.r_entry_field)

        self.b_label = QLabel("b ")
        self.b_entry_field = QLineEdit()
        self.b_entry_field.textChanged.connect(self.check_float)
        self.form.addRow(self.b_label, self.b_entry_field)

        self.c_label = QLabel("c ")
        self.c_entry_field = QLineEdit()
        self.c_entry_field.textChanged.connect(self.check_float)
        self.form.addRow(self.c_label, self.c_entry_field)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_branched)
        self.form.addWidget(self.calculate_button)

        self.calculated_value_label = QLabel()
        self.calculated_value_label.hide()
        self.form.addWidget(self.calculated_value_label)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.save_to_file_button.hide()
        self.form.addWidget(self.save_to_file_button)

        self.setLayout(self.form)

    def check_float(self, text):
        try:
            if text is not "":
                float(text)
        except ValueError:
            QMessageBox().warning(self, "Invalid input", "Value must be float!", QMessageBox.Ok)

    def calculate_branched(self):
        errors = []
        try:
            r = float(self.r_entry_field.text())
        except:
            errors.append("Invalid value r")

        try:
            b = float(self.b_entry_field.text())
        except:
            errors.append("Invalid value b")

        try:
            c = float(self.c_entry_field.text())
        except:
            errors.append("Invalid value c")

        if len(errors) == 0:
            self.calculated_value_label.setText(str(branched_algorithm.branched(r, b, c)))
            self.calculated_value_label.show()
            self.save_to_file_button.show()
        else:
            QMessageBox().warning(self, "Invalid input", "\n".join(errors), QMessageBox.Ok)

    def load_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Load file")
            with open(file_name[0], "r") as file:
                self.r_entry_field.setText(file.readline().split()[1])
                self.b_entry_field.setText(file.readline().split()[1])
                self.c_entry_field.setText(file.readline().split()[1])
                self.calculated_value_label.hide()
                self.save_to_file_button.hide()
        except:
            QMessageBox().warning(self, "Error", "Shit happens")

    def save_to_file(self):
        file_name = "branched"
        counter = 1
        while True:
            try:
                with open(file_name + str(counter) + ".txt", "xt") as file:
                    file.write("a " + self.r_entry_field.text() + "\n")
                    file.write("b " + self.b_entry_field.text() + "\n")
                    file.write("x " + self.c_entry_field.text() + "\n")
                    file.write("calculated " + self.calculated_value_label.text() + "\n")

            except FileExistsError:
                counter += 1
            else:
                QMessageBox.information(self, "Info",
                                        "Successfully saved in {}".format(file_name + str(counter) + ".txt"),
                                        QMessageBox.Ok)
                break


class CyclicAlgorithmWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()

        self.cyclic_image_label = QLabel()
        self.cyclic_image_label.setPixmap(QPixmap("lab1_cyclic.png"))
        self.cyclic_image_label.setAlignment(Qt.AlignCenter)
        self.form.addWidget(self.cyclic_image_label)

        self.file_load_button = QPushButton("Load file")
        self.file_load_button.clicked.connect(self.load_file)
        self.form.addWidget(self.file_load_button)

        self.a_table = QTableWidget()
        self.a_table.setStyleSheet("background-color: white; color:black; font-size: 16px")
        self.a_table.setColumnCount(10)
        self.a_table.setRowCount(1)
        self.a_table.setVerticalHeaderLabels(["a"])
        self.a_table.setFixedHeight(75)
        self.a_table.itemChanged.connect(self.check_input_table)
        self.form.addWidget(self.a_table)

        self.b_table = QTableWidget()
        self.b_table.setStyleSheet("background-color: white; color:black; font-size: 16px")
        self.b_table.setColumnCount(10)
        self.b_table.setRowCount(1)
        self.b_table.setVerticalHeaderLabels(["b"])
        self.b_table.setFixedHeight(75)
        self.b_table.itemChanged.connect(self.check_input_table)
        self.form.addWidget(self.b_table)

        self.n_label = QLabel("n ")
        self.n_entry_field = QLineEdit()
        self.n_entry_field.setValidator(QIntValidator())
        self.n_entry_field.textChanged.connect(self.check_int)
        self.form.addRow(self.n_label, self.n_entry_field)

        self.p_label = QLabel("p ")
        self.p_entry_field = QLineEdit()
        self.p_entry_field.setValidator(QIntValidator())
        self.p_entry_field.textChanged.connect(self.check_int)
        self.form.addRow(self.p_label, self.p_entry_field)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_cyclic)
        self.form.addWidget(self.calculate_button)

        self.calculated_value_label = QLabel()
        self.calculated_value_label.hide()
        self.form.addWidget(self.calculated_value_label)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.save_to_file_button.hide()
        self.form.addWidget(self.save_to_file_button)

        self.setLayout(self.form)

    def check_int(self, text):
        try:
            if text is not "":
                int(text)
        except ValueError:
            QMessageBox().warning(self, "Invalid input", "Value n and p must be integers!", QMessageBox.Ok)

    def calculate_cyclic(self):
        errors = []
        a = []
        if self.a_table.item(0, 0) is None or self.a_table.item(0, 0).text() is "":
            raise ValueError

        for column in range(self.a_table.columnCount()):
            item = self.a_table.item(0, column)
            if item is None or item.text() is "":
                break
            else:
                a.append(float(item.text()))

        b = []
        if self.b_table.item(0, 0) is None or self.a_table.item(0, 0).text() is "":
            raise ValueError

        for column in range(self.b_table.columnCount()):
            item = self.b_table.item(0, column)
            if item is None or item.text() is "":
                break
            else:
                b.append(float(item.text()))

        try:
            n = int(self.n_entry_field.text())
        except Warning:
            errors.append("Invalid value n")

        try:
            p = int(self.p_entry_field.text())
        except:
            errors.append("Invalid value p")

        if len(errors) == 0:
            self.calculated_value_label.setText(str(cyclic_algorithm.cyclic(a, b, n, p)))
            self.calculated_value_label.show()
            self.save_to_file_button.show()
        else:
            QMessageBox().warning(self, "Invalid input", "\n".join(errors), QMessageBox.Ok)

    def load_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Load file")
            with open(file_name[0], "r") as file:
                a = file.readline().split()
                b = file.readline().split()
                n = file.readline().split()[1]
                p = file.readline().split()[1]
                self.insert_row(self.a_table, a, 0)
                self.insert_row(self.b_table, b, 0)
                self.n_entry_field.setText(n)
                self.p_entry_field.setText(p)
                self.calculated_value_label.hide()
                self.save_to_file_button.hide()
        except ValueError:
            QMessageBox().warning(self, "Error", "Shit happens")

    def insert_row(self, table, row_list, row):
        table.setColumnCount(len(row_list)-1)
        for item_index in range(1, len(row_list)):
            table.setItem(row, item_index-1, QTableWidgetItem(row_list[item_index]))

    def save_to_file(self):
        file_name = "cyclic"
        extension = ".txt"
        counter = 1
        while True:
            try:
                with open(file_name + str(counter) + extension, "xt") as file:
                    try:
                        self.write_table_row(self.a_table, 0, file)
                        self.write_table_row(self.b_table, 0, file)
                        self.write_value(self.n_label, self.n_entry_field, file)
                        self.write_value(self.p_label, self.p_entry_field, file)
                    except:
                        remove(file_name + str(counter) + extension)
                        QMessageBox.warning(self, "Error", "Invalid input")
                        return
            except FileExistsError:
                counter += 1
            else:
                QMessageBox.information(self, "Info",
                                        "Successfully saved in {}".format(file_name + str(counter) + ".txt"),
                                        QMessageBox.Ok)
                break

    def write_table_row(self, table, row, file):
        if table.item(row, 0) is None or table.item(row, 0).text() is "":
            raise ValueError

        file.write(table.takeVerticalHeaderItem(row).text())

        for column in range(table.columnCount()):
            item = table.item(row, column)
            if item is None or item.text() is "":
                break
            else:
                file.write(" " + item.text())

        file.write("\n")

    def write_value(self, label, line_edit, file):
        if line_edit is None or line_edit.text() == "":
            raise ValueError
        else:
            file.write(label.text() + line_edit.text() + "\n")

    def check_input_table(self, Qitem):
        if Qitem.text() == "":
            return
        else:
            try:
                test = float(Qitem.text())
            except ValueError:
                t = Qitem.tableWidget()
                t.setFocus()
                Qitem.setText("")
                t.setCurrentCell(0, Qitem.column())

                Msgbox = QMessageBox()
                Msgbox.setText("Error, value must be number!")
                Msgbox.exec()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    lab1_window = LabWindow()
    lab1_window.show()
    sys.exit(app.exec_())

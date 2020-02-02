from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QDesktopWidget, QFormLayout,
                             QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QDoubleValidator
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
        self.setMinimumSize(QSize(600, 400))
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
        self.a_entry_field.setValidator(QDoubleValidator())
        self.form.addRow(self.a_label, self.a_entry_field)

        self.b_label = QLabel("b ")
        self.b_entry_field = QLineEdit()
        self.b_entry_field.setValidator(QDoubleValidator())
        self.form.addRow(self.b_label, self.b_entry_field)

        self.x_label = QLabel("x ")
        self.x_entry_field = QLineEdit()
        self.x_entry_field.setValidator(QDoubleValidator())
        self.form.addRow(self.x_label, self.x_entry_field)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_linear)
        self.form.addWidget(self.calculate_button)

        self.calculated_value_label = QLabel()
        self.form.addWidget(self.calculated_value_label)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.form.addWidget(self.save_to_file_button)

        self.setLayout(self.form)

    def calculate_linear(self):
        errors = []
        try:
            a = int(self.a_entry_field.text())
        except:
            errors.append("Invalid value a")

        try:
            b = int(self.b_entry_field.text())
        except:
            errors.append("Invalid value b")

        try:
            x = int(self.x_entry_field.text())
        except:
            errors.append("Invalid value x")

        if len(errors) == 0:
            self.calculated_value_label.setText(str(linear_algorithm.linear(a, b, x)))
        else:
            QMessageBox().warning(self, "Invalid input", "\n".join(errors), QMessageBox.Ok)

    def load_file(self):
        pass

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
        self.r_entry_field.setValidator(QDoubleValidator())
        self.form.addRow(self.r_label, self.r_entry_field)

        self.b_label = QLabel("b ")
        self.b_entry_field = QLineEdit()
        self.b_entry_field.setValidator(QDoubleValidator())
        self.form.addRow(self.b_label, self.b_entry_field)

        self.c_label = QLabel("c ")
        self.c_entry_field = QLineEdit()
        self.c_entry_field.setValidator(QDoubleValidator())
        self.form.addRow(self.c_label, self.c_entry_field)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_branched)
        self.form.addWidget(self.calculate_button)

        self.calculated_value_label = QLabel()
        self.form.addWidget(self.calculated_value_label)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.form.addWidget(self.save_to_file_button)

        self.setLayout(self.form)

    def calculate_branched(self):
        errors = []
        try:
            r = int(self.r_entry_field.text())
        except:
            errors.append("Invalid value r")

        try:
            b = int(self.b_entry_field.text())
        except:
            errors.append("Invalid value b")

        try:
            c = int(self.c_entry_field.text())
        except:
            errors.append("Invalid value c")

        if len(errors) == 0:
            self.calculated_value_label.setText(str(branched_algorithm.branched(r, b, c)))
        else:
            QMessageBox().warning(self, "Invalid input", "\n".join(errors), QMessageBox.Ok)

    def load_file(self):
        pass

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

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_cyclic)
        self.form.addWidget(self.calculate_button)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.form.addWidget(self.save_to_file_button)

        self.setLayout(self.form)

    def calculate_cyclic(self):
        pass

    def load_file(self):
        pass

    def save_to_file(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    lab1_window = LabWindow()
    lab1_window.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QDesktopWidget, QFormLayout,
                             QLineEdit, QPushButton, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIntValidator
from os import remove


class LabWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.center()

    def init_window(self):
        self.setWindowTitle("Lab2")
        self.setMinimumSize(QSize(600, 500))
        self.setStyleSheet("background-color:#2D3047; color:black; font-family: 'Open Sans Condensed'; font-size: 24px")


    def center(self):
        """function, that center window on the screen"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class MergeSortUI(QWidget):
    def __init__(self):
        super().__init__()

    def load_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Load file")
            with open(file_name[0], "r") as file:
                pass
                # self.a_entry_field.setText(file.readline().split()[1:])
        except:
            QMessageBox().warning(self, "Error", "Shit happens")

    def save_to_file(self):
        file_name = "linear"
        counter = 1
        while True:
            try:
                with open(file_name + str(counter) + ".txt", "xt") as file:
                    pass
            except FileExistsError:
                counter += 1
            else:
                QMessageBox.information(self, "Info",
                                        "Successfully saved in {}".format(file_name + str(counter) + ".txt"),
                                        QMessageBox.Ok)
                break


class SortTest(QWidget):
    def __init__(self):
        super().__init__()

    def load_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Load file")
            with open(file_name[0], "r") as file:
                pass
        except:
            QMessageBox().warning(self, "Error", "Shit happens")

    def save_to_file(self):
        file_name = "branched"
        counter = 1
        while True:
            try:
                with open(file_name + str(counter) + ".txt", "xt") as file:
                    pass

            except FileExistsError:
                counter += 1
            else:
                QMessageBox.information(self, "Info",
                                        "Successfully saved in {}".format(file_name + str(counter) + ".txt"),
                                        QMessageBox.Ok)
                break


class SortTestPlots(QWidget):
    def __init__(self):
        super().__init__()

    def save_plots(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    lab2_window = LabWindow()
    lab2_window.show()
    sys.exit(app.exec_())

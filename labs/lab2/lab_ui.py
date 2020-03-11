from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QDesktopWidget, QFormLayout,
                             QLineEdit, QPushButton, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIntValidator
from os import remove
import random
import merge_sort


class LabWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab2")
        self.setMinimumSize(QSize(600, 500))
        self.setStyleSheet("background-color:#2D3047; color:black; font-family: 'Open Sans Condensed'; font-size: 24px")

        tabs = QTabWidget()
        tabs.addTab(MergeSortUI(), "Sort")
        tabs.addTab(SortTest(), "TimeTest")
        tabs.setStyleSheet("background-color:#767BA3")

        vb = QVBoxLayout()
        vb.addWidget(tabs)
        self.setLayout(vb)

        self.center()

    def center(self):
        """function, that center window on the screen"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class MergeSortUI(QWidget):
    def __init__(self):
        super().__init__()

        self.vb = QVBoxLayout()

        self.load_file_button = QPushButton("Load file")
        self.load_file_button.clicked.connect(self.load_file)
        self.vb.addWidget(self.load_file_button)

        self.sorting_array_entry_field = QLineEdit()
        self.vb.addWidget(self.sorting_array_entry_field)

        self.sort_button = QPushButton("Sort")
        self.sort_button.clicked.connect(self.sort)
        self.vb.addWidget(self.sort_button)

        self.sorted_array_entry_field = QLineEdit()
        self.vb.addWidget(self.sorted_array_entry_field)

        self.save_to_file_button = QPushButton("Save to file")
        self.save_to_file_button.clicked.connect(self.save_to_file)
        self.save_to_file_button.hide()
        self.vb.addWidget(self.save_to_file_button)

        self.vb.addStretch(1)

        self.setLayout(self.vb)

    def load_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Load file")
            with open(file_name[0], "r") as file:
                self.sorting_array_entry_field.setText(" ".join(file.readline().split()[1:]))
            self.save_to_file_button.hide()
        except:
            QMessageBox().warning(self, "Error", "Shit happens")

    def save_to_file(self):
        file_name = "sort"
        counter = 1
        while True:
            try:
                with open(file_name + str(counter) + ".txt", "xt") as file:
                    file.write("sorting_array " + self.sorting_array_entry_field.text() + "\n")
                    file.write("sorted_array " + self.sorted_array_entry_field.text() + "\n")
            except FileExistsError:
                counter += 1
            else:
                QMessageBox.information(self, "Info",
                                        "Successfully saved in {}".format(file_name + str(counter) + ".txt"),
                                        QMessageBox.Ok)
                break

    def sort(self):
        try:
            array = list(map(float, self.sorting_array_entry_field.text().split()))
            print(array)
            self.sorted_array_entry_field.setText(" ".join(list(map(str, merge_sort.merge_sort_with_time(array)[0]))))
            self.save_to_file_button.show()
        except FileExistsError:
            QMessageBox().warning(self, "Error", "Invalid input")


class SortTest(QWidget):
    def __init__(self):
        super().__init__()
        self.test_arrays = None
        self.chart_timetest = None

        self.vb = QVBoxLayout()

        self.generate_test_arrays_button = QPushButton("Generate arrays")
        self.generate_test_arrays_button.clicked.connect(self.generate_test_arrays)
        self.vb.addWidget(self.generate_test_arrays_button)

        self.start_time_test_button = QPushButton("Start TimeTest")
        self.start_time_test_button.clicked.connect(self.start_time_test)
        self.vb.addWidget(self.start_time_test_button)

        self.setLayout(self.vb)

    def generate_test_arrays(self):
        test_arrays = []
        for i in range(1, 11):
            test_arrays.append([random.randint(0, 1000) for i in range(10000*i)])
        self.test_arrays = test_arrays

    def start_time_test(self):
        chart_timetest = []
        for array in self.test_arrays:
            chart_timetest.append([len(array), merge_sort.merge_sort_with_time(array)[1]])
        self.chart_timetest = chart_timetest
        print(chart_timetest)

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

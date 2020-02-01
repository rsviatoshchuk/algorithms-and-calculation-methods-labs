from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QDesktopWidget, QFormLayout,
                             QLineEdit, QPushButton)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap


class LabWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.center()

    def init_window(self):
        self.setWindowTitle("Lab1")
        self.setMinimumSize(QSize(600, 400))
        self.setStyleSheet("background-color:#2D3047")

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

        form = QFormLayout()

        linear_image_label = QLabel()
        linear_image_label.setPixmap(QPixmap("lab1_linear.png"))

        form.addWidget(linear_image_label)

        a_label = QLabel("a")
        # a_label.setStyleSheet()
        a_entry_field = QLineEdit()
        form.addRow(a_label, a_entry_field)

        b_label = QLabel("b")
        b_entry_field = QLineEdit()
        form.addRow(b_label, b_entry_field)

        x_label = QLabel("x")
        x_entry_field = QLineEdit()
        form.addRow(x_label, x_entry_field)
        self.setLayout(form)

        calculate_button = QPushButton("Calculate")
        form.addWidget(calculate_button)


class BranchedAlgorithmWindow(QWidget):
    def __init__(self):
        super().__init__()


class CyclicAlgorithmWindow(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    lab1_window = LabWindow()
    lab1_window.show()
    sys.exit(app.exec_())

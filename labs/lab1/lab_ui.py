from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QSize


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

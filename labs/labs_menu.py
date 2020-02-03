from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGroupBox, QGridLayout, QVBoxLayout,
                             QDesktopWidget)
from labs.lab1 import lab_ui as l1


class MainLabsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_main_window()

    def init_main_window(self):
        self.setWindowTitle("AMO Labs")
        self.center()
        self.setStyleSheet("background-color:#2D3047")  # #2D3047  #020403
        self.create_layout()
        self.show()

    def create_layout(self):
        vertical_box = QVBoxLayout()

        info_label = QLabel("Це гловне меню, що об'єднує всі лаби в одному місці\n"
                            "Варіант завдань - 23")
        info_label.setStyleSheet("color:white; font-family: 'Open Sans Condensed'; font-size: 24px")

        vertical_box.addWidget(info_label)
        labs_group_box = QGroupBox()
        grid_labs = QGridLayout()

        button_lab1 = QPushButton("Lab1")
        button_lab2 = QPushButton("Lab2")
        button_lab3 = QPushButton("Lab3")
        button_lab4 = QPushButton("Lab4")
        button_lab5 = QPushButton("Lab5")

        button_lab1.setStyleSheet("color:white; font-family: 'Open Sans Condensed'; font-size: 24px")
        button_lab2.setStyleSheet("color:white; font-family: 'Open Sans Condensed'; font-size: 24px")
        button_lab3.setStyleSheet("color:white; font-family: 'Open Sans Condensed'; font-size: 24px")
        button_lab4.setStyleSheet("color:white; font-family: 'Open Sans Condensed'; font-size: 24px")
        button_lab5.setStyleSheet("color:white; font-family: 'Open Sans Condensed'; font-size: 24px")

        button_lab1.clicked.connect(self.open_lab1)
        button_lab2.clicked.connect(self.open_lab2)
        button_lab3.clicked.connect(self.open_lab3)
        button_lab4.clicked.connect(self.open_lab4)
        button_lab5.clicked.connect(self.open_lab5)

        grid_labs.addWidget(button_lab1, 0, 0)
        grid_labs.addWidget(button_lab2, 0, 1)
        grid_labs.addWidget(button_lab3, 0, 2)
        grid_labs.addWidget(button_lab4, 1, 0)
        grid_labs.addWidget(button_lab5, 1, 2)

        labs_group_box.setLayout(grid_labs)
        vertical_box.addWidget(labs_group_box)
        self.setLayout(vertical_box)

    def open_lab1(self):
        self.lab1 = l1.LabWindow()
        self.lab1.show()

    def open_lab2(self):
        pass

    def open_lab3(self):
        pass

    def open_lab4(self):
        pass

    def open_lab5(self):
        pass

    def center(self):
        """function, that center window on the screen"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_labs_window = MainLabsWindow()
    main_labs_window.show()
    sys.exit(app.exec_())

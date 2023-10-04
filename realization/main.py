from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sorting algorithms")
        self.main_layout = QHBoxLayout()

        self.left, self.top, self.width, self.height = 1100, 100, 360, 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(360, 600)
        self.setStyleSheet("background-color: #ffffff;")
        
        self.time = QLabel(self)
        self.time.setText("")
        self.time.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.time.setStyleSheet("background-color: #ffffff; color: white; border-radius: 10px;")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.move(100, -5)
        self.time.setFixedSize(160, 30)

        self.name_app = QLabel(self)
        self.name_app.setText("Sorting algorithms")
        self.name_app.setFont(QFont("Arial", 25, QFont.Weight.Bold))
        self.name_app.setStyleSheet("background-color: #262626; color: white; border-radius: 20px;")
        self.name_app.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_app.move(4, 4)
        self.name_app.setFixedSize(352, 80)
        self.name_app.lower()
        
        self.end_app = QLabel(self)
        self.end_app.setStyleSheet("background-color: #262626; border-radius: 20px;")
        self.end_app.move(4, 516)
        self.end_app.setFixedSize(352, 80)
        
        button_widget = QWidget(self)
        button_widget.setStyleSheet("background-color: #353535;")
        button_layout = QVBoxLayout(button_widget)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_widget.setFixedSize(352, 520)
        button_widget.move(4, 50)
        button_widget.lower()
        
        self.merge_sort = QPushButton("Merge sort")
        self.merge_sort.setGeometry(150, 100, 200, 50)
        self.merge_sort.setFont(QFont("Arial", 20))
        self.merge_sort.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.merge_sort.setFixedSize(200, 40)
        
        self.tree_sort = QPushButton("Tree sort")
        self.tree_sort.setGeometry(150, 200, 200, 100)
        self.tree_sort.setFont(QFont("Arial", 20))
        self.tree_sort.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.tree_sort.setFixedSize(200, 40)
        
        self.exit = QPushButton("Exit", self)
        self.exit.setGeometry(150, 600, 200, 50)
        self.exit.setFont(QFont("Arial", 20))
        self.exit.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        self.exit.setFixedSize(200, 40)
        
        button_layout.addWidget(self.merge_sort)
        button_layout.addWidget(self.tree_sort)
        button_layout.addWidget(self.exit)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
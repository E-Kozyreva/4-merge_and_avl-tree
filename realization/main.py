from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Sorting algorithms")
        self.setGeometry(1000, 100, 500, 700)
        self.setFixedSize(500, 700)
        self.setStyleSheet("background-color: #240046;")
        
        # плашка с округленными краям
        self.up = QLabel(self)
        self.up.setStyleSheet("background-color: #3c096c; border-radius: 10px;")
        self.up.setGeometry(0, -10, 500, 60)
        
        # текст к верхней плашке
        self.label = QLabel(self)
        self.label.setText("Sorting algorithms")
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white;")
        self.label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.label.adjustSize()
        self.label.move(150, 10)
        
        # кнопка merge sort
        self.merge_sort = QPushButton("Merge sort", self)
        self.merge_sort.setGeometry(150, 100, 200, 50)
        self.merge_sort.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        self.merge_sort.setStyleSheet("background-color: #5a189a; color: white; border-radius: 10px;")
        self.merge_sort.clicked.connect(self.merge_sort_clicked)
        
        # кнопка tree sort
        self.tree_sort = QPushButton("Tree sort", self)
        self.tree_sort.setGeometry(150, 200, 200, 50)
        self.tree_sort.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        self.tree_sort.setStyleSheet("background-color: #5a189a; color: white; border-radius: 10px;")
        self.tree_sort.clicked.connect(self.tree_sort_clicked)
        
        # кнопка выхода 
        self.exit = QPushButton("Exit", self)
        self.exit.setGeometry(150, 600, 200, 50)
        self.exit.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        self.exit.setStyleSheet("background-color: #ff9100; color: white; border-radius: 10px;")
        self.exit.clicked.connect(self.close)
        
        
    def merge_sort_clicked(self):
        print("Merge sort button clicked")
        
    def tree_sort_clicked(self):
        print("Tree sort button clicked")
        
    def back_clicked(self):
        print("Back button clicked")
    
    def exit_clicked(self):
        print("Exit button clicked")
        self.close()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
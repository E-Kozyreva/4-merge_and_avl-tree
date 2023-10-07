from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize, Qt
import sys

from buttons import Buttons
from design import Design
import funcbuttons


class MainWindow(QMainWindow, Buttons):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sorting algorithms")
        self.main_layout = QHBoxLayout()

        self.left, self.top, self.width, self.height = 1100, 100, 360, 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(360, 600)
        self.setStyleSheet("background-color: #ffffff;")
        
        # time widget
        self.time = QLabel(self)
        self.time = Design.time_label(self.time)

        # name app widget
        self.name_app = QLabel(self)
        self.name_app = Design.name_app_label(self.name_app)
        
        # end app widget
        self.end_app = QLabel(self)
        self.end_app = Design.end_app_label(self.end_app)
        
        # button widget
        self.button_widget = QWidget(self)
        self.button_layout = QVBoxLayout(self.button_widget)
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_widget = Design.button_widget(self.button_widget)
        
        # merge sort button
        self.button_layout.addWidget(Buttons.)
        self.merge_sort.clicked.connect(self.merge_sort_clicked)
        
        # tree sort button
        self.tree_sort = QPushButton("Tree sort")
        self.tree_sort = Design.black_button(self.tree_sort)
        self.button_layout.addWidget(self.tree_sort)
        self.tree_sort.clicked.connect(self.tree_sort_clicked)
        
        # exit button
        self.exit = QPushButton("Exit")
        self.exit = Design.white_button(self.exit)
        self.button_layout.addWidget(self.exit)
        self.exit.clicked.connect(self.exit_clicked)
    
    def merge_sort_clicked(self):
        self.index = 0
        # 2-way merge sort button
        self.t_way = QPushButton("2-way", self)
        self.t_way = Design.black_button(self.t_way)
        self.button_layout.addWidget(self.t_way)
        self.t_way.clicked.connect(self.t_way_clicked)

        # 4-way merge sort button
        self.f_way = QPushButton("4-way", self)
        self.f_way = Design.black_button(self.f_way)
        self.button_layout.addWidget(self.f_way)

        # 8-way merge sort button
        self.e_way = QPushButton("8-way", self)
        self.e_way = Design.black_button(self.e_way)
        self.button_layout.addWidget(self.e_way)
        
        # back button
        self.back = QPushButton("Back", self)
        self.back = Design.white_button(self.back)
        self.button_layout.addWidget(self.back)
        
        self.name_app.setText("Merge sort")
        funcbuttons.HideButtons.merge_algo(self.merge_sort, self.tree_sort, self.exit)
        funcbuttons.ShowButtons.merge_algo(self.t_way, self.f_way, self.e_way, self.back)

        self.t_way.clicked.connect(self.t_way_clicked)
        self.back.clicked.connect(self.back_clicked)
        
    def t_way_clicked(self):
        self.t_way.hide()
        self.f_way.hide()
        self.e_way.hide()
        self.back.hide()
        self.name_app.setText("2-way merge sort")

        # button enter array
        self.enter_array = QPushButton("Enter array", self)
        self.enter_array = Design.black_button(self.enter_array)
        self.button_layout.addWidget(self.enter_array)
        self.enter_array.show()

        # button random array
        self.random_array = QPushButton("Random array", self)
        self.random_array = Design.black_button(self.random_array)
        self.button_layout.addWidget(self.random_array)
        self.random_array.show()

        # add array from file 
        self.add_array_from_file = QPushButton("Add array from file", self)
        self.add_array_from_file = Design.black_button(self.add_array_from_file)
        self.button_layout.addWidget(self.add_array_from_file)
        self.add_array_from_file.show()

        # back button
        self.back = QPushButton("Back", self)
        self.back = Design.white_button(self.back)
        self.button_layout.addWidget(self.back)
        self.back.show()
        
    def tree_sort_clicked(self):
        self.index = 1
        # tree sort button
        self.avl_sort = QPushButton("Avl sort")
        self.avl_sort = Design.black_button(self.avl_sort)
        self.button_layout.addWidget(self.avl_sort)

        # back button
        self.back = QPushButton("Back", self)
        self.back = Design.white_button(self.back)
        self.button_layout.addWidget(self.back)
        
        self.name_app.setText("Tree sort")
        funcbuttons.HideButtons.tree_algo(self.merge_sort, self.tree_sort, self.exit)
        funcbuttons.ShowButtons.tree_algo(self.avl_sort, self.back)

        self.back.clicked.connect(self.back_clicked)

    def show_hide(self):
        self.buttons = {0: [funcbuttons.ShowButtons.merge_algo_back(self.merge_sort, self.tree_sort, self.exit), 
                            funcbuttons.HideButtons.merge_algo_back(self.t_way, self.f_way, self.e_way, self.back)],
                        1: [funcbuttons.ShowButtons.tree_algo_back(self.merge_sort, self.tree_sort, self.exit), 
                            funcbuttons.HideButtons.tree_algo_back(self.av, self.back)],
                        }
        
        return self.buttons[self.index][0], self.buttons[self.index][1]

    def back_clicked(self):
        self.show_hide()

        self.name_app.setText("Sorting algorithms")


    

    def exit_clicked(self):
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
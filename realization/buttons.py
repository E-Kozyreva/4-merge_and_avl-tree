from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize, Qt

from design import Design

class Buttons:
    def __init__(self):
        self.merge_sort = QPushButton("Merge sort")
        self.merge_sort = Design.black_button(self.merge_sort)

        self.tree_sort = QPushButton("Tree sort")
        self.tree_sort = Design.black_button(self.tree_sort)
        
        self.exit = QPushButton("Exit")
        self.exit = Design.white_button(self.exit)
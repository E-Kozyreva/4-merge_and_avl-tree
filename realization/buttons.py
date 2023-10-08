from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize, Qt

from design import Design

class Buttons:
    def merge_sort_button():
        merge_sort = QPushButton("Merge sort")
        merge_sort = Design.black_button(merge_sort)
        return merge_sort
    
    
    def t_way_button():
        t_way = QPushButton("2-way")
        t_way = Design.black_button(t_way)
        return t_way
    
    
    def f_way_button():
        f_way = QPushButton("4-way")
        f_way = Design.black_button(f_way)
        return f_way
    
    
    def e_way_button():
        e_way = QPushButton("8-way")
        e_way = Design.black_button(e_way)
        return e_way
    
    
    def tree_sort_button():
        tree_sort = QPushButton("Tree sort")
        tree_sort = Design.black_button(tree_sort)
        return tree_sort
    
    
    def avl_button():
        avl_tree = QPushButton("AVL tree")
        avl_tree = Design.black_button(avl_tree)
        return avl_tree
    
    
    def enter_array_button():
        enter_array = QPushButton("Enter array")
        enter_array = Design.black_button(enter_array)
        return enter_array
    
    
    def random_array_button():
        random_array = QPushButton("Random array")
        random_array = Design.black_button(random_array)
        return random_array
    
    
    def add_array_from_file_button():
        add_array_from_file = QPushButton("Add array from file")
        add_array_from_file = Design.black_button(add_array_from_file)
        return add_array_from_file
    
    
    def back_button():
        back_b = QPushButton("Back")
        back_b = Design.white_button(back_b)
        return back_b
    
    
    def exit_button():
        exit_b = QPushButton("Exit")
        exit_b = Design.white_button(exit_b)
        return exit_b
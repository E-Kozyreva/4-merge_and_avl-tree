from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize, Qt
import sys

class MergeSort:
    def __init__(self, array, time):
        self.array = array
        self.time = time

    def merge2(arr):
        if len(arr) > 1:                              
            mid = len(arr) // 2                      
            left = arr[:mid]                          
            right = arr[mid:]                         
            
            MergeSort.merge2(left)                          
            MergeSort.merge2(right) 
            
            i = j = k = 0                            
            
            while i < len(left) and j < len(right): 
                if left[i] < right[j]:               
                    arr[k] = left[i]                 
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            
            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1
        
        return arr
    
    def merge4(arr, start, first_quarter, midpoint, third_quarter, end):
        leftest_arr = arr[start:first_quarter + 1]  
        left_arr = arr[first_quarter + 1:midpoint + 1]
        right_arr = arr[midpoint + 1:third_quarter + 1]
        rightest_arr = arr[third_quarter + 1:end + 1]
        
        leftest_arr.append(float("inf"))  
        left_arr.append(float("inf"))
        right_arr.append(float("inf"))
        rightest_arr.append(float("inf"))
        
        i = j = l = m = 0
        
        for k in range(start, end + 1): 
            if leftest_arr[i] <= left_arr[j] and leftest_arr[i] <= right_arr[l] and leftest_arr[i] <= rightest_arr[m]:
                arr[k] = leftest_arr[i]
                i += 1
            elif left_arr[j] <= right_arr[l] and left_arr[j] <= rightest_arr[m]:
                arr[k] = left_arr[j]
                j += 1
            elif right_arr[l] <= rightest_arr[m]:
                arr[k] = right_arr[l]
                l += 1
            else:
                arr[k] = rightest_arr[m]
                m += 1

    def mergesort4(arr, start, end):
        if end - start > 0:
            midpoint = (start + end) // 2  
            fq = (start + midpoint) // 2
            tq = (midpoint + end) // 2
            
            MergeSort.mergesort4(arr, start, fq)
            MergeSort.mergesort4(arr, fq + 1, midpoint)
            MergeSort.mergesort4(arr, midpoint + 1, tq)
            MergeSort.mergesort4(arr, tq + 1, end)
            MergeSort.merge4(arr, start, fq, midpoint, tq, end)
        
        return arr


class TreeSort:
    def __init__(self, array, time):
        self.array = array
        self.time = time

    class Node:
        # BST data structure
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

        def insert(self, val):
            if self.val:
                if val < self.val:
                    if self.left is None:
                        self.left = Node(val)
                    else:
                        self.left.insert(val)
                elif val > self.val:
                    if self.right is None:
                        self.right = Node(val)
                    else:
                        self.right.insert(val)
            else:
                self.val = val


    def inorder(root, res):
        # Recursive traversal
        if root:
            TreeSort.inorder(root.left, res)
            res.append(root.val)
            TreeSort.norder(root.right, res)


    def tree_sort(arr):
        # Build BST
        if len(arr) == 0:
            return arr
        root = TreeSort.Node(arr[0])
        for i in range(1, len(arr)):
            root.insert(arr[i])
        # Traverse BST in order.
        res = []
        TreeSort.inorder(root, res)
        return res


class Design:
    def time_label(time):
        time.setFixedSize(140, 30)
        time.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        time.move(110, -7)
        return time


    def name_app_label(name_app):
        name_app.setFixedSize(352, 80)
        name_app.move(4, 4)
        name_app.setText("Sorting algorithms")
        name_app.setFont(QFont("Arial", 25, QFont.Weight.Bold))
        name_app.setStyleSheet("background-color: #262626; color: white; border-radius: 20px;")
        name_app.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_app.lower()
        return name_app


    def end_app_label(end_app):
        end_app.setFixedSize(352, 80)
        end_app.move(4, 516)
        end_app.setStyleSheet("background-color: #262626; border-radius: 20px;")
        return end_app
    

    def button_widget(button_widget):
        button_widget.setFixedSize(352, 520)
        button_widget.move(4, 50)
        button_widget.setStyleSheet("background-color: #353535;")
        button_widget.lower()
        return button_widget
    

    def black_button(button):
        button.setGeometry(150, 100, 200, 50)
        button.setFixedSize(240, 50)
        button.setFont(QFont("Arial", 20))
        button.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        return button
    

    def white_button(button):
        button.setGeometry(150, 100, 200, 50)
        button.setFixedSize(240, 50)
        button.setFont(QFont("Arial", 20))
        button.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        return button
        

class MainWindow(QMainWindow):
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
        self.merge_sort = QPushButton("Merge sort")
        self.merge_sort = Design.black_button(self.merge_sort)
        self.button_layout.addWidget(self.merge_sort)
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
    
    def merge_sort_clicked(self, hide_buttons: list):
        for button in hide_buttons:
            button.hide()
        self.name_app.setText("Merge sort")

        # 2-way merge sort button
        self.t_way = QPushButton("2-way", self)
        self.t_way = Design.black_button(self.t_way)
        self.button_layout.addWidget(self.t_way)
        self.t_way.show()
        self.t_way.clicked.connect(self.t_way_clicked)

        # 4-way merge sort button
        self.f_way = QPushButton("4-way", self)
        self.f_way = Design.black_button(self.f_way)
        self.button_layout.addWidget(self.f_way)
        self.f_way.show()

        # 8-way merge sort button
        self.e_way = QPushButton("8-way", self)
        self.e_way = Design.black_button(self.e_way)
        self.button_layout.addWidget(self.e_way)
        self.e_way.show()
        
        # back button
        self.back = QPushButton("Back", self)
        self.back = Design.white_button(self.back)
        self.button_layout.addWidget(self.back)
        self.back.show()
        self.back.clicked.connect(self.back_clicked)

    def t_way_clicked(self, hide_buttons: list):
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
        self.merge_sort.hide()
        self.tree_sort.hide()
        self.exit.hide()
        self.name_app.setText("Tree sort")

        # tree sort button
        self.avl_sort = QPushButton("Avl sort")
        self.avl_sort = Design.black_button(self.avl_sort)
        self.button_layout.addWidget(self.avl_sort)
        self.avl_sort.show()

        # back button
        self.back = QPushButton("Back", self)
        self.back = Design.white_button(self.back)
        self.button_layout.addWidget(self.back)
        self.back.show()
        self.back.clicked.connect(self.back_clicked_tree_sort)

    def back_clicked(self, hide_buttons, show_buttons):
        self.avl_sort.hide()
        self.back.hide()

        self.merge_sort.show()
        self.tree_sort.show()
        self.exit.show()
        self.name_app.setText("Sorting algorithms")

    def exit_clicked(self):
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
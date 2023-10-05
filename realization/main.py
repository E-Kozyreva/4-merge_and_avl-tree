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
        self.time.setFixedSize(140, 30)
        self.time.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.move(110, -7)

        # name app widget
        self.name_app = QLabel(self)
        self.name_app.setFixedSize(352, 80)
        self.name_app.move(4, 4)
        self.name_app.setText("Sorting algorithms")
        self.name_app.setFont(QFont("Arial", 25, QFont.Weight.Bold))
        self.name_app.setStyleSheet("background-color: #262626; color: white; border-radius: 20px;")
        self.name_app.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_app.lower()
        
        # end app widget
        self.end_app = QLabel(self)
        self.end_app.setFixedSize(352, 80)
        self.end_app.move(4, 516)
        self.end_app.setStyleSheet("background-color: #262626; border-radius: 20px;")
        
        # button widget
        self.button_widget = QWidget(self)
        self.button_layout = QVBoxLayout(self.button_widget)
        self.button_widget.setFixedSize(352, 520)
        self.button_widget.move(4, 50)
        self.button_widget.setStyleSheet("background-color: #353535;")
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_widget.lower()
        
        # merge sort button
        self.merge_sort = QPushButton("Merge sort")
        self.merge_sort.setGeometry(150, 100, 200, 50)
        self.merge_sort.setFixedSize(200, 40)
        self.merge_sort.setFont(QFont("Arial", 20))
        self.merge_sort.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.button_layout.addWidget(self.merge_sort)
        self.merge_sort.clicked.connect(self.merge_sort_clicked)
        
        # tree sort button
        self.tree_sort = QPushButton("Tree sort")
        self.tree_sort.setGeometry(150, 200, 200, 100)
        self.tree_sort.setFixedSize(200, 40)
        self.tree_sort.setFont(QFont("Arial", 20))
        self.tree_sort.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.button_layout.addWidget(self.tree_sort)
        self.tree_sort.clicked.connect(self.tree_sort_clicked)
        
        # exit button
        self.exit = QPushButton("Exit", self)
        self.exit.setGeometry(150, 600, 200, 50)
        self.exit.setFixedSize(200, 40)
        self.exit.setFont(QFont("Arial", 20))
        self.exit.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        self.button_layout.addWidget(self.exit)
        self.exit.clicked.connect(self.exit_clicked)
    
    def merge_sort_clicked(self):
        self.merge_sort.hide()
        self.tree_sort.hide()
        self.exit.hide()
        self.name_app.setText("Merge sort")

        # 2-way merge sort button
        self.t_way = QPushButton("2-way", self)
        self.t_way.setGeometry(150, 100, 200, 50)
        self.t_way.setFixedSize(200, 40)
        self.t_way.setFont(QFont("Arial", 20))
        self.t_way.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.button_layout.addWidget(self.t_way)
        self.t_way.show()

        # 4-way merge sort button
        self.f_way = QPushButton("4-way", self)
        self.f_way.setGeometry(150, 100, 200, 50) 
        self.f_way.setFixedSize(200, 40)
        self.f_way.setFont(QFont("Arial", 20))
        self.f_way.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.button_layout.addWidget(self.f_way)
        self.f_way.show()

        # 8-way merge sort button
        self.e_way = QPushButton("8-way", self)
        self.e_way.setGeometry(150, 200, 200, 50)
        self.e_way.setFixedSize(200, 40)
        self.e_way.setFont(QFont("Arial", 20))
        self.e_way.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.button_layout.addWidget(self.e_way)
        self.e_way.show()
        
        # back button
        self.back = QPushButton("Back", self)
        self.back.setGeometry(150, 600, 200, 50)
        self.back.setFixedSize(200, 40)
        self.back.setFont(QFont("Arial", 20))
        self.back.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        self.button_layout.addWidget(self.back)
        self.back.show()
        self.back.clicked.connect(self.back_clicked_merge_sort)
        
    def tree_sort_clicked(self):
        self.merge_sort.hide()
        self.tree_sort.hide()
        self.exit.hide()
        self.name_app.setText("Tree sort")

        # tree sort button
        self.avl_sort = QPushButton("Avl sort")
        self.avl_sort.setGeometry(150, 100, 200, 50)
        self.avl_sort.setFixedSize(200, 40)
        self.avl_sort.setFont(QFont("Arial", 20))
        self.avl_sort.setStyleSheet("background-color: #262626; color: white; border-radius: 10px;")
        self.button_layout.addWidget(self.avl_sort)
        self.avl_sort.show()

        # back button
        self.back = QPushButton("Back", self)
        self.back.setGeometry(150, 600, 200, 50)
        self.back.setFixedSize(200, 40)
        self.back.setFont(QFont("Arial", 20))
        self.back.setStyleSheet("background-color: #ffffff; color: black; border-radius: 10px;")
        self.button_layout.addWidget(self.back)
        self.back.show()
        self.back.clicked.connect(self.back_clicked_tree_sort)
        
    def back_clicked_merge_sort(self):
        self.t_way.hide()
        self.f_way.hide()
        self.e_way.hide()
        self.back.hide()

        self.merge_sort.show()
        self.tree_sort.show()
        self.exit.show()
        self.name_app.setText("Sorting algorithms")

    def back_clicked_tree_sort(self):
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
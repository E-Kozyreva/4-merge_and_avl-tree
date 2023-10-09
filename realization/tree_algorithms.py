# класс для хранения узла бинарного дерева
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left, self.right = None, None

# Ввод
#     tree - бинарное дерево
#     elem - элемент, который нужно добавить в бинарное дерево
# Вывод
#     обновленное дерево
def insert_elem(tree, elem):
    if tree is None:
        tree = Node(elem)
        return tree
    if elem <= tree.elem:
        tree.left = insert_elem(tree.left, elem)
    elif elem > tree.elem:
        tree.right = insert_elem(tree.right, elem)
    
    return tree
# Ввод
#     tree - бинарное дерево
#     arr - массив, в который записывается отсортированный массив
#     next_index - индекс следующего элемента
# Вывод
#     индекс следующего элемента

def tree_traversal(tree, arr, next_index):
    if tree is not None:
        next_index = tree_traversal(tree.left, arr, next_index)
        arr[next_index] = tree.elem
        next_index += 1
        next_index = tree_traversal(tree.right, arr, next_index)
        
    return next_index
# Ввод
#     arr - массив для сортировки
# Вывод
#     -
def tree_sort(arr):
    tree = None
    for elem in arr:
        tree = insert_elem(tree, elem)
    tree_traversal(tree, arr, 0)
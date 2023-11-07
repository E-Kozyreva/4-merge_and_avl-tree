class Node:
    def __init__(self, elem: int) -> None:
        self.elem = elem
        self.left, self.right = None, None


def insert_elem(tree: list, elem: int) -> list:
    if tree is None:
        tree = Node(elem)
        return tree
    if elem <= tree.elem:
        tree.left = insert_elem(tree.left, elem)
    elif elem > tree.elem:
        tree.right = insert_elem(tree.right, elem)
    return tree


def tree_traversal(tree: list, arr: list, next_index: int) -> int:
    if tree is not None:
        next_index = tree_traversal(tree.left, arr, next_index)
        arr[next_index] = tree.elem
        next_index += 1
        next_index = tree_traversal(tree.right, arr, next_index)
    return next_index


def tree_sort(arr: list) -> None:
    tree = None
    for elem in arr:
        tree = insert_elem(tree, elem)
    tree_traversal(tree, arr, 0)

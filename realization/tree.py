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

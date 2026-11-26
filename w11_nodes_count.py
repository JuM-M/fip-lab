class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = BinaryNode(10)
root.left = BinaryNode(5)
root.right = BinaryNode(15)
root.left.left = BinaryNode(3)
root.left.right = BinaryNode(7)
root.right.left = BinaryNode(12)
root.right.right = BinaryNode(20)

def nodes_count(root):
    if root is None:
        return 0
    return 1 + nodes_count(root.left) + nodes_count(root.right)

print(nodes_count(root))
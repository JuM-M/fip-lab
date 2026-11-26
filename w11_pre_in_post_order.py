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

def preorder(node):
    if node is None:
        return []
    order = []
    order.append(node.val)
    order.extend(preorder(node.left))
    order.extend(preorder(node.right))
    return order
def inorder(node):
    if node is None:
        return []
    order = []
    order.extend(inorder(node.left))
    order.append(node.val)
    order.extend(inorder(node.right))
    return order
def postorder(node):
    if node is None:
        return []
    order = []
    order.extend(postorder(node.left))
    order.extend(postorder(node.right))
    order.append(node.val)
    return order

print(preorder(root))
print(inorder(root))
print(postorder(root))


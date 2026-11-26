class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_insert(root,val):
    if root is None:
        root = BinaryNode(val)
    if root.val < val:
        root.right = bst_insert(root.right,val)
    if root.val > val:
        root.left = bst_insert(root.left,val)
    return root

def bst_search(root,val):
    if root is None:
        return False
    if root.val == val:
        return True
    if root.val > val:
        return bst_search(root.left,val)
    if root.val < val:
        return bst_search(root.right,val)

root = None
for x in [50,30,70,20,40,60,80]:
    root = bst_insert(root,x)

print(bst_search(root,40))
print(bst_search(root,65))
print(bst_search(root,80))
print()
print()
print(bst_search(root,20))
print(bst_search(root,45))
print(bst_search(root,76))
print(bst_search(root,47))


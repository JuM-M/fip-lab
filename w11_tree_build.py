class TreeNode:
    def __init__(self,val):
        self.children = []
        self.val = val

ceo = TreeNode("CEO")
cto = TreeNode("CTO")
cfo = TreeNode("CFO")
kuaiji = TreeNode("会计")
shenji = TreeNode("审计")
ceo.children.append(cto)
ceo.children.append(cfo)
cfo.children.append(kuaiji)
cfo.children.append(shenji)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_recursive(node):
    if node is None:
        return

    print(node.value)

    preorder_recursive(node.left)
    preorder_recursive(node.right)

def postorder_recursive(node):
    if node is None:
        return
    
    postorder_recursive(node.left)
    postorder_recursive(node.right)

    print(node.value)

def inorder_recursive(node):
    if node is None:
        return
    
    inorder_recursive(node.left)

    print(node.value)

    inorder_recursive(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("전위 순회")
preorder_recursive(root)

print("후위 순회")
postorder_recursive(root)

print("중위 순회")
inorder_recursive(root)
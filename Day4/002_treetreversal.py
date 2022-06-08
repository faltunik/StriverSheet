#https://www.codingninjas.com/codestudio/problems/tree-traversal_981269?topList=striver-sde-sheet-problems

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder = [] # here we first put left child, then itself and then right
    preorder = []  # here we first put itself, left and then right
    postorder = [] # here left, right, itself
    def inorder_traversal(root, inorder):
        if not root: return
        inorder_traversal(root.left, inorder)
        inorder.append(root.data)
        inorder_traversal(root.right, inorder)
        return
    def preorder_traversal(root, preorder):
        if not root: return
        
        preorder.append(root.data)
        preorder_traversal(root.left, preorder)
        preorder_traversal(root.right, preorder)
        return
    def postorder_traversal(root, postorder):
        if not root: return
        postorder_traversal(root.left, postorder)
        postorder_traversal(root.right, postorder)
        postorder.append(root.data)
        
        return
    
    postorder_traversal(root,postorder)
    inorder_traversal(root,inorder)
    preorder_traversal(root,preorder)
    
    return inorder, preorder, postorder


# i think, they actaully asked us to implement a tree traversal with just once function
# and  not sure, I failed

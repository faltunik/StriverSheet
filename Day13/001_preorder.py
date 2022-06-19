'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    # Write your code here.
    ans = []
    if not root: return []
    
    def help(root):
        if not root.left and not root.right:
            ans.append(root.data)
            return
        if root.left:
            help(root.left)
        ans.append(root.data)
        if root.right:
            help(root.right)
        return
    
    help(root)
    return ans



#https://www.codingninjas.com/codestudio/problems/inorder-traversal_3839605?topList=striver-sde-sheet-problems
# easy
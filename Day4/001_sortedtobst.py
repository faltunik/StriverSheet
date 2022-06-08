'''
    Following is the TreeNode class structure

	class TreeNode :
    	def __init__(self, val) :
        	self.val = val
        	self.left = None
        	self.right = None

    	def __del__(self):
        	if self.left:
            	del self.left
        	if self.right:
            	del self.right
            
'''
class TreeNode :
        def __init__(self, val) :
            self.val = val
            self.left = None
            self.right = None

        def __del__(self):
            if self.left:
                del self.left
            if self.right:
                del self.right

def sortedArrToBST(arr, n):
    # simple recursive solution
    def help(i,j):
        if i>=j: return None
        m = (i+j)//2
        root = TreeNode(arr[m])
        root.left = help(i, m)
        root.right = help(m+1, j)
        return root
    return help(0,n)

#https://www.codingninjas.com/codestudio/problems/convert-sorted-array-to-bst_1264995?topList=striver-sde-sheet-problems
# Easy Level

# first: I thought i ==j but then I put j = n, instead n-1, got that error
# only 58% better in leetcode submission
#
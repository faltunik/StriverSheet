



# wrong attempt

def changeTree(root): 
    # Write your code here.
    def help(root):
        if not root: return 0 # if root is Null, return 0
        if not root.left and not root.right: return  root.data # if root is leaf, return it's value
        #l = 0 if not root.left else help(root.left)  # if root.left exist, left will be gone through else0
        #r = 0 if not root.right else help(root.right)
        tmp = help(root.left) + help(root.right)
        cache = root.data
        root.data = tmp
        if cache > root.data:
            k = cache -tmp
            while root:
                root.data += k
                root = root.left or root.right
        return root.data
    
    help(root)
    return root


# after watching solution
# hint: 
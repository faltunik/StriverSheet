# https://www.codingninjas.com/codestudio/problems/cycle-detection-in-a-singly-linked-list_628974?topList=striver-sde-sheet-problems
# medium but easy

def detectCycle(head) :
    # Write your code here.
    while head:
        if head.data == -1.5: return True
        head.data = -1.5
        head = head.next
    return False
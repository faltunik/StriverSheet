# https://www.codingninjas.com/codestudio/problems/add-two-numbers-as-linked-lists_1170520?topList=striver-sde-sheet-problems
# medium


from os import *
from sys import *
from collections import *
from math import *



# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next



# bruteforce
class Bruteforce:
    def addTwoNumbers(self, head1, head2):
        # Write your code here.
        s = str(self.help(head1) + self.help(head2))
        return self.helper(s)
        
# convert number into linked list    
    def helper(self,s):
        i = len(s)-1
        dummyhead = Node(-1)
        node = Node(int(s[i]))
        dummyhead.next = node
        i -=1
        while i>=0:
            node.next = Node(int(s[i]))
            node = node.next
            i -=1
        return dummyhead.next
    
    def help(self,node):
        k =0
        n = 0
        while node:
            n += node.data*(10**k)
            k +=1
            node = node.next
        return n


# in above solution frist we are finding number from linked list and then adding those and then converting that into linked list
# we can avoid that using varibale carry and we can manipulate value of larger head

# so we will add the value of h1 and h2, and change value of h1, and if sum >9, we will carry= s//10,
# if we reach end of any head
# if h1, then add prev.next = h2 and then we will add the carr
# now we reach end and if there is still a carry,
# add new node with that value


# wrong attempt 1

from os import *
from sys import *
from collections import *
from math import *

# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def addTwoNumbers(head1, head2):
    # 5 1 0 6 -1
    # 6 7 3 4 -1
    # 1 9 3 
    # 1 9 3 0 1 -1
# my  1 9 3 1 -1
    dummyhead= Node(-1)
    dummyhead.next = head1
    c = 0
    while head1 and head2:
        tmp = head1.data + head2.data + c
        head1.data, c = tmp%10, tmp//10
        if head1.next:
            head1, head2 = head1.next, head2.next
        elif head2.next:
            head1.next = head2.next
            head1 = head1.next
            break
        else:            
            break
    while c and head1:
        tmp = (head1.data+c)
        head1.data,c = tmp%10, tmp//10
        if head1: head1 = head1.next
        else: break
    if c: head1.next = Node(c)
    return dummyhead.next


# not sure why I am getting the wrong answer

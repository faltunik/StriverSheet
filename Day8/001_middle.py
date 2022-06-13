# https://www.codingninjas.com/codestudio/problems/middle-of-linked-list_973250?topList=striver-sde-sheet-problems

from os import *
from sys import *
from collections import *
from math import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    s = f = head
    while f.next:
        s = s.next
        f = f.next
        if f.next:
            f = f.next
    return s


# so this was basic question, we alreayd use this technique for many questions

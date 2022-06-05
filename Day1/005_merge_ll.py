from os import *
from sys import *
from collections import *
from math import *

import sys
from sys import stdin

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    dummyhead = Node(-1)
    dummyhead.next = first
    help(first, second, dummyhead)
    return dummyhead.next

def help(first,second, prev):
    if not first:
        prev.next = second
        return 
    if not second:
        prev.next = first
        return 
    if first.data <second.data:
        help(first.next, second, first)
        return
    if first.data >= second.data:
        tmp = second.next
        prev.next = second
        second.next = first
        second = tmp
        help(first, second, prev.next)
        return


# i have no idea, how it get submitted
# i mean I didn't read input nor I print anything while in other problems I was getting error
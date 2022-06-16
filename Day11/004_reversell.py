#
# medium
# very good question

from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    if not head: return None
    res = Node(head.data)
    head = head.next
    while head:
        tmp = head.next
        head.next = res
        res = head
        head  = tmp
    return res
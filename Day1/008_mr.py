from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    m = n*(n+1)/2 - sum(set(arr))
    r = sum(arr) - sum(set(arr))
    return m,r



     

# yeh codestudio chutiya platform hai sala, smjh nhi ata ki code fail kahan ho rha hai
# first attmept: failed(5June)
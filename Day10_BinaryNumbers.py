import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    data = bin(n)
    maxi = 0
    curr = 0
    for i in data:
        if i == '1':
            curr = curr + 1
        else:
            maxi = max(maxi,curr)
            curr = 0
            
    print(max(maxi,curr))

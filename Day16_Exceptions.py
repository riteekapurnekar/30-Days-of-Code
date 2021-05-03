import sys

S = input().strip()

try:
    x = int(S)
    print(x)
except:
    print("Bad String")


# Online Python - IDE, Editor, Compiler, Interpreter

def sumArray(arr):
    # Please add your code here
    pass
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sumArray(arr[1:])
 

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
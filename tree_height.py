# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    nodes = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    max_height = 0
    # Your code here
    stack = [(root, 1)]
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in nodes[node]:
            stack.append((child, height+1))
    return max_height


def main():
    # implement input form keyboard and from files
    n = int(input())
    parents = list(map(int, input().split()))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    print(compute_height(n, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
print(numpy.array([1,2,3]))

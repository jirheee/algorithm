

import sys

l = []
n = int(sys.stdin.readline())

for i in range(n):
    instruction = sys.stdin.readline().split()
    if instruction[0] == "push":
        l.append(instruction[1])
    elif instruction[0] == "pop":
        print(l.pop() if len(l) != 0 else -1)
    elif instruction[0] == "size":
        print(len(l))
    elif instruction[0] == "empty":
        print(1 if len(l)==0 else 0)
    elif instruction[0] == "top":
        print(l[-1] if len(l) != 0 else -1)

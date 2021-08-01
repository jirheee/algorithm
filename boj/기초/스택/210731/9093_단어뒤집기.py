import sys

n = int(sys.stdin.readline())

for i in range(n):
    sentence = sys.stdin.readline()
    splited = [word[::-1] for word in sentence.split()]
    print(" ".join(splited))
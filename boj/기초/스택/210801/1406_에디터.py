from sys import stdin

if __name__ == "__main__":

    left = list(stdin.readline().strip())
    right = []

    n = int(stdin.readline())

    for _ in range(n):
        instr = stdin.readline().strip().split()
        if instr[0] == "L" and left:
            right.append(left.pop())
        if instr[0] == "D" and right:
            left.append(right.pop())
        if instr[0] == "B" and left:
            left.pop()
        if instr[0] == "P":
            left.append(instr[1])
    
    right.reverse()
    print("".join(left+right))
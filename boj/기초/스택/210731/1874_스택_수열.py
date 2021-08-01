from sys import stdin

def solve(n):
    l = list(range(n, 0, -1))

    stack = []
    trace = []
    for i in range(n):
        next_seq_num = int(stdin.readline())
        if len(stack) == 0:
            stack.append(l.pop())
            trace.append("+")
            
        while next_seq_num > stack[-1]:
            stack.append(l.pop())
            trace.append("+")

        if next_seq_num == stack[-1]:
            stack.pop()
            trace.append("-")
        else:
            print("NO")
            return
    
    for t in trace:
        print(t)

if __name__ == "__main__":
    n = int(stdin.readline())
    solve(n)
    


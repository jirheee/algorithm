from sys import stdin

def solve(seq):
    
    result = [-1 for _ in seq]

    stack = [0]
    for i in range(1, len(seq)):
        while stack and seq[stack[-1]] < seq[i]:
            result[stack.pop()] = seq[i]
        
        stack.append(i)
    
    return " ".join(map(str,result))


if __name__ == "__main__":
    n = int(stdin.readline())
    seq = list(map(int, stdin.readline().strip().split()))

    print(solve(seq))
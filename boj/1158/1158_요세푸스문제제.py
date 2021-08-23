import sys


if __name__ == "__main__":
    n, k = [int(i) for i in sys.stdin.readline().split()]

    l = list(range(1, n+1))
    answer = []
    pointer = -1
    for i in range(n):
        pointer = (pointer + k) % len(l)
        answer.append(str(l.pop(pointer)))
        pointer -= 1
    
    print(f"<{', '.join(answer)}>")


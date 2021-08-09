import sys

def solve(n):
    # 1<=n<11
    l = [0, 1, 2, 4]

    for i in range(4, n+1):
        l.append(l[i-1]+l[i-2]+l[i-3])

    print(l[n])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    for i in range(n):
        solve(int(sys.stdin.readline()))
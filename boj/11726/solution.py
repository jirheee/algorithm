import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    l = [0 for _ in range(n+1)]

    if n==1:
        print(1)
    elif n==2:
        print(2)
    else:
        l[1] = 1
        l[2] = 2

        for i in range(3, n+1):
            l[i] = l[i-1]+l[i-2]

        print(l[n]%10007)
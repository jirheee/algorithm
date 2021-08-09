from sys import stdin

if __name__ == "__main__":
    # 1<=n<=10^6
    n = int(stdin.readline())

    l = [-1, 0, 1, 1]

    for i in range(4,n+1):
        k = l[i-1]
        if i%2 == 0:
            k = min(k, l[i//2])
        if i%3 == 0:
            k = min(k, l[i//3])
        l.append(k+1)

    print(l[n])



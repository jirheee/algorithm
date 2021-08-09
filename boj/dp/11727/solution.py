import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    if n == 1:
        print(1)
    elif n==2:
        print(3)
    else:
        l = [0 for _ in range(n+1)]
        
        l[1] = 1
        l[2] = 3

        if (1<=n<3 ): print(l[n])
        else:
            for i in range(3, n+1):
                l[i] = l[i-1]+l[i-2]*2

            print(l[n]%10007)
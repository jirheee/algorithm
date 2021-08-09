from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    plist = list(map(int, stdin.readline().split()))

    l = [0 for _ in range(1001)]
    l[1] = plist[0]

    for i in range(2, n+1):
        trivial_max = max([l[i-(num_cards+1)] + p for num_cards,p in enumerate(plist) if i-(num_cards+1) >= 0])

        for j in range(1, i+1):
            if l[j] + l[i-j] > trivial_max:
                trivial_max = l[j] + l[i-j]
        
        l[i] = trivial_max
    
    print(l[n])


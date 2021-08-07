from sys import stdin

def solve(seq):
    l = []

    sorted(enumerate(seq), lambda x: x[1])

    
    return " ".join(map(str,result))


if __name__ == "__main__":
    n = int(stdin.readline())
    seq = list(map(int, stdin.readline().strip().split()))

    print(solve(seq))
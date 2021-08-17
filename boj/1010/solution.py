from sys import stdin
import math

def solve(n: int, m: int) -> int:
    return math.comb(m, n)


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        n, m = [int(i) for i in stdin.readline().split()]
        answer = solve(n, m)
        print(answer)
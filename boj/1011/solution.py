from sys import stdin

def solve(distance):
    current = 0
    count = 1
    while True:
        current += count//2
        next = current + (count+1) // 2
        if current <= distance <=next:
            return count
        
        count += 1

if __name__ == "__main__":
    n = int(stdin.readline())

    for _ in range(n):
        x, y = [int(i) for i in stdin.readline().strip().split()]
        answer = solve(y - x)
        print(answer)
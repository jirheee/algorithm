from sys import stdin
from typing import List, Tuple

def solve(map: List[List[int]], n):

    nodes = set([(i, j) for i in range(n) for j in range(n) if map[i][j] == 1])

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(x, y):
        count = 1
        for x_off, y_off in directions:
            new_x, new_y = x+x_off, y+y_off
            if not (0<=new_x<n and 0<=new_y<n) or not (new_x, new_y) in nodes:
                continue
            
            nodes.remove((new_x, new_y))
            count += dfs(new_x, new_y)
        
        return count


    num_houses = []
    while nodes:
        num_houses.append(dfs(*nodes.pop()))
    
    print(len(num_houses))
    for n in sorted(num_houses):
        print(n)

if __name__ == "__main__":
    n = int(stdin.readline())

    map = [list(map(int, stdin.readline().strip())) for _ in range(n)]

    solve(map, n)
from sys import stdin
from typing import List
from pprint import pprint as pp


def solve(map: List[List[int]], n: int, m: int) -> int:

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    visited = [[False for _ in range(m)] for _ in range(n)]
    dist = [[0 for _ in range(m)] for _ in range(n)]

    queue = [(0, 0)]
    visited[0][0] = True
    dist[0][0] = 1
    
    while queue:
        x_start, y_start = queue.pop(0)
        current_dist = dist[x_start][y_start]

        for x_offset, y_offset in directions:
            x = x_start + x_offset
            y = y_start + y_offset

            if not (0<=x<n and 0<=y<m):
                continue

            if not visited[x][y] and map[x][y] == 1:
                if x == n-1 and y == m-1:
                    return current_dist + 1
                
                queue.append((x, y))
                visited[x][y] = True
                dist[x][y] = current_dist + 1
        

    return -1

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    map = [[int(num) for num in stdin.readline().strip()] for _ in range(n)]
    print(solve(map, n, m))
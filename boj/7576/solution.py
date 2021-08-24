from sys import stdin

if __name__ == "__main__":
    m, n = map(int, stdin.readline().split())

    tomato_map = [list(map(int, stdin.readline().split())) for  _ in range(n)]

    print(tomato_map)

    visited = [[False for _ in range(m)] for _ in range(n)]
    riped_tomatoes = set([(i, j) for i in range(n) for j in range(m) if tomato_map[i][j] == 1])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(x, y):
        # visited 복사?
        queue = [(x, y)]
        while queue:
            x, y = queue.pop()
            
    
    max_day = 0
    while riped_tomatoes:
        x, y = riped_tomatoes.pop()
        max_day = max(max_day, bfs(*riped_tomatoes.pop()))

    if all([all(l) for l in visited]):
        print(max_day)
    else:
        print(-1)
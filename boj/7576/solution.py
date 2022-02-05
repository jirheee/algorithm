from sys import stdin

if __name__ == "__main__":
    m, n = map(int, stdin.readline().split())

    tomato_map = [list(map(int, stdin.readline().split())) for  _ in range(n)]

    visited = [[False for _ in range(m)] for _ in range(n)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(tomatoes):
        new_tomatoes = []

        for x,y  in tomatoes:
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                    continue
                if visited[new_x][new_y]:
                    continue
                visited[new_x][new_y] = True
                if tomato_map[new_x][new_y] == 0:
                    new_tomatoes.append((new_x, new_y))
        
        return new_tomatoes
    
    max_day = 0

    tomatoes = []
    for r, row in enumerate(tomato_map):
        for c, val in enumerate(row):
            if val == 1:
                visited[r][c] = True
                tomatoes.append((r, c))
            if val == -1:
                visited[r][c] = True

    while True:
        tomatoes = bfs(tomatoes)        
        if len(tomatoes) == 0:
            break
        max_day += 1

    if all([all(l) for l in visited]):
        print(max_day)
    else:
        print(-1)
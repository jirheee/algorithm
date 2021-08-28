from sys import stdin
from typing import FrozenSet, List, Tuple, MutableSet
from copy import deepcopy

Coord = Tuple[int, int]

def get_wall_combinations(wall_coords: List[Coord]) -> MutableSet[FrozenSet[Coord]]:
    result = set()

    for coord1 in wall_coords:
        for coord2 in wall_coords:
            for coord3 in wall_coords:
                fs = frozenset([coord1, coord2, coord3])
                if len(fs) == 3:
                    result.add(fs)

    return result

def get_virus_area_size(lab_map: List[List[int]], virus_coords: List[Coord], visited: List[List[bool]]) -> int:
    def get_adjacent_nodes(coord: Coord) -> List[Coord]:
        result = []
        r, c = coord
        for r_off, c_off in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r+r_off, c+c_off
            if not (0<=new_r<len(lab_map) and 0<=new_c<len(lab_map[0])):
                continue

            if lab_map[new_r][new_c] == 0 and not visited[new_r][new_c]:
                result.append((new_r, new_c))
        
        return result

    virus_area_size = len(virus_coords)
    queue = deepcopy(virus_coords)
    while queue:
        coord = queue.pop(0)
        for r, c in get_adjacent_nodes(coord):
            if not visited[r][c] and lab_map[r][c] == 0:
                queue.append((r, c))
                virus_area_size += 1
                visited[r][c] = True

    return virus_area_size

def setup_visited(visited: List[List[int]], blank_coords: List[Coord]):
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            visited[i][j] = True

    for r, c in blank_coords:
        visited[r][c] = False
    

def solve(lab_map: List[List[int]], n: int, m: int) -> int:
    virus_coords = []
    blank_coords = []
    wall_coords = []

    for row_idx, row in enumerate(lab_map):
        for col_idx, elem in enumerate(row):
            if elem == 0:
                blank_coords.append((row_idx, col_idx))
            elif elem == 1:
                wall_coords.append((row_idx, col_idx))
            elif elem == 2:
                virus_coords.append((row_idx, col_idx))
            else:
                raise ValueError(f"Invalid Input: {elem}")
            
    wall_combinations = get_wall_combinations(blank_coords)

    min_virus_area_size = 65
    visited = [[False for _ in range(m)] for _ in range(n)]

    for (r1, c1), (r2, c2), (r3, c3) in wall_combinations:
        # assert lab_map[r1][c1] == 0 and lab_map[r2][c2] == 0 and lab_map[r3][c3] == 0

        lab_map[r1][c1] = 1
        lab_map[r2][c2] = 1
        lab_map[r3][c3] = 1

        setup_visited(visited, blank_coords)

        min_virus_area_size = min(min_virus_area_size, get_virus_area_size(lab_map, virus_coords, visited))

        lab_map[r1][c1] = 0
        lab_map[r2][c2] = 0
        lab_map[r3][c3] = 0

    return n*m - min_virus_area_size - len(wall_coords) - 3

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())

    lab_map = [list(map(int, stdin.readline().split())) for _ in range(n)]



    print(solve(lab_map, n, m))

    # 0 0 0 0 0 0         0 0 0 0 1 0
    # 1 0 0 0 0 2    =>   1 0 0 1 0 2
    # 1 1 1 0 0 2         1 1 1 0 0 2
    # 0 0 0 0 0 2         0 0 0 1 0 2

    # 2 0 0 0 1 1 0         2 1 0 0 1 1 0
    # 0 0 1 0 1 2 0         1 0 1 0 1 2 0
    # 0 1 1 0 1 0 0         0 1 1 0 1 0 0
    # 0 1 0 0 0 0 0    =>   0 1 0 0 0 1 0
    # 0 0 0 0 0 1 1         0 0 0 0 0 1 1
    # 0 1 0 0 0 0 0         0 1 0 0 0 0 0
    # 0 1 0 0 0 0 0         0 1 0 0 0 0 0

    # 2 0 0 0 0 0 0 2          2 0 0 0 0 0 0 2
    # 2 0 0 0 0 0 0 2          2 0 0 0 0 0 0 2
    # 2 0 0 0 0 0 0 2          2 0 0 0 0 0 0 2
    # 2 0 0 0 0 0 0 2    =>    2 0 0 0 0 0 0 2
    # 2 0 0 0 0 0 0 2          2 0 0 0 0 0 0 2
    # 0 0 0 0 0 0 0 0          1 0 0 0 0 0 0 0
    # 0 0 0 0 0 0 0 0          0 1 0 0 0 0 0 0
    # 0 0 0 0 0 0 0 0          0 0 1 0 0 0 0 0
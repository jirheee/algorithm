from sys import stdin

def find_groups(graph: list[list[str]], n: int) -> set[frozenset[int]]:
    
    visited = [False for _ in range(n)]

    def get_reachable(node):
        return [i for i in range(n) if graph[node][i] == "Y"]

    def dfs(node: int) -> list[int]:
        if visited[node]:
            return []
        visited[node] = True
        result = [node]

        for reachable_node in get_reachable(node):
            for n in dfs(reachable_node):
                result.append(n)

        return result
    
    return set(frozenset(dfs(node)) for node in range(n) if not visited[node])

def solve(groups, graph, n):
    if n == 1:
        return 0

    for group in groups:
        if len(group) == 1:
            return -1

    num_edges = 0
    for i in range(n):
        num_edges += sum([1 if char == "Y" else 0 for char in graph[i]])
    num_edges //= 2
    
    if num_edges+1 < n:
        return -1

    return len(groups) - 1


if __name__ == "__main__":
    n = int(stdin.readline())

    graph = [list(stdin.readline().strip()) for _ in range(n)]

    groups = find_groups(graph, n)

    print(solve(groups, graph, n))
        

    
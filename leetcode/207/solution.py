from typing import List

class Solution:
    # Get graph and sources
    def get_info(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        is_source_list = [True for _ in range(numCourses)]

        for src, dest in prerequisites:
            graph[src].append(dest)
            is_source_list[dest] = False
        
        sources = [node for node, is_source in enumerate(is_source_list) if is_source]

        return graph, sources


    def topological_sort(self, graph, sources):
        visited = []
        # traverse the graph using dfs
        # push nodes to visited retaining partial order
        def dfs(node, prev):  
            if node in visited:
                return

            if prev == -1:
                visited.insert(0, node)
            else:
                prev_index = visited.index(prev)
                visited.insert(prev_index+1, node)
                

            for adj in graph[node]:
                dfs(adj, node)
            

        for source in sources:
            dfs(source, -1)
        
        return visited
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, sources = self.get_info(numCourses, prerequisites)

        # print(f"Graph: {graph}\nSources: {sources}")

        top_sorted = self.topological_sort(graph, sources)

        if numCourses != len(top_sorted):
            return False

        # print(f"Top Sorted: {top_sorted}")

        while top_sorted:
            node = top_sorted.pop()

            for reachable in graph[node]:
                if reachable in top_sorted or reachable == node:
                    return False
            
        return True
    
if __name__ == "__main__":
    numCourses = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    print(Solution().canFinish(numCourses, prerequisites))
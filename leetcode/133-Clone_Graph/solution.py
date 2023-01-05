from pprint import pprint as pp
class Node:

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        return f"Node({self.val}, {self.neighbors})"

    def __repr__(self) -> str:
        return f"Node({self.val}, {self.neighbors})"

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None: return None

        cloned_dict = {node.val: Node(node.val)}

        def clone_helper(node):
            new_neighbors = []
            for neighbor in node.neighbors:
                if neighbor.val in cloned_dict:
                    new_neighbors.append(cloned_dict[neighbor.val])
                else:
                    new_neighbor = Node(neighbor.val)
                    cloned_dict[neighbor.val] = new_neighbor
                    new_neighbors.append(new_neighbor)
                    
                    clone_helper(neighbor)
            cloned_dict[node.val].neighbors = new_neighbors
        
        clone_helper(node)

        pp(cloned_dict)
        
        return cloned_dict[node.val]

if __name__ == "__main__":
    graph = [Node(1), Node(2), Node(3), Node(4)]
    graph[0].neighbors = [graph[1], graph[3]]
    graph[1].neighbors = [graph[0], graph[2]]
    graph[2].neighbors = [graph[1], graph[3]]
    graph[3].neighbors = [graph[0], graph[2]]

    cloned = Solution().cloneGraph(graph[0])




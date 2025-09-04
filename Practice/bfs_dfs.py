from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
    print()

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
        print("DFS (Recursive) Traversal:", end=" ")
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)
    if len(visited) == len(graph):
        print()

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    print("DFS (Iterative) Traversal:", end=" ")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))
    print()

if __name__ == "__main__":
    print("Graph:", graph)
    bfs(graph, 1)
    dfs_recursive(graph, 1)
    dfs_iterative(graph, 1)

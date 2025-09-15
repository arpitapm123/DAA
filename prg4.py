from collections import deque
def dfs(graph, root):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])  # Push neighbors
    return visited
def bfs(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])  # Enqueue neighbors
    return visited



if __name__ == "__main__":
    graph = {}
    # Take input from user
    n = int(input("Enter number of vertices: "))
    print("Enter vertex labels (e.g., A, B, C):")
    vertices = [input().strip() for _ in range(n)]
    # Initialize adjacency list
    for v in vertices:
        graph[v] = []
    e = int(input("Enter number of edges: "))
    print("Enter edges in format: u v (means edge from u -> v)")
    for _ in range(e):
        u, v = input().split()
        graph[u].append(v)   # directed edge
        # For undirected graph, also add: graph[v].append(u)
    print("\nGraph (Adjacency List):")
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")
    # Traversals
    start_node = input("\nEnter the starting node for traversal: ").strip()
    dfs_result = dfs(graph, start_node)
    bfs_result = bfs(graph, start_node)
    print("\nDFS Traversal starting from node", start_node, ":")
    print(" -> ".join(dfs_result))
    print("\nBFS Traversal starting from node", start_node, ":")
    print(" -> ".join(bfs_result))
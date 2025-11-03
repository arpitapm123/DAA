def create_adjacency_matrix(vertices, edges, directed=False):
    adj_matrix = [[0] * vertices for _ in range(vertices)]
# Step 2: Fill adjacency matrix with given edges
    for (u, v) in edges:
        adj_matrix[u][v] = 1
    if not directed:   # For undirected graph, mark both
        adj_matrix[v][u] = 1
    return adj_matrix
def calculate_degrees(adj_matrix, directed=False):
    vertices = len(adj_matrix)
    in_degree = [0] * vertices
    out_degree = [0] * vertices
    for i in range(vertices):
        for j in range(vertices):
            if adj_matrix[i][j] == 1:
                out_degree[i] += 1
                in_degree[j] += 1
    return in_degree, out_degree
if __name__ == "__main__":
    print("Graph Representation with In-Degree and Out-Degree\n")
# Input graph details
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
directed = input("Is the graph directed? (yes/no): ").lower() == "yes"
# Input edges
edges = []
print("\nEnter the edges (format: u v for edge u->v):")
for _ in range(e):
  u, v = map(int, input().split())
  edges.append((u, v))
# Create adjacency matrix
adj = create_adjacency_matrix(n, edges, directed)
# Display adjacency matrix
print("\nAdjacency Matrix:")
for row in adj:
    print(" ".join(map(str, row)))
# Calculate and display degrees
    in_degree, out_degree = calculate_degrees(adj, directed)
    print("\nVertex\tIn-Degree\tOut-Degree")
for i in range(n):
    print(f"{i}\t{in_degree[i]}\t\t{out_degree[i]}")
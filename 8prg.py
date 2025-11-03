def create_matrix(n, edges):
 adj=[[0]*n for i in range(n)]
 for (u, v) in edges:
  adj[u][v]=adj[v][u]=1 # For undirected graph
  return adj
n,e=map(int, input("Enter vertices and edges:").split())
edges=[tuple(map(int, input().split()))for _ in range(e)]
adj = create_matrix(n,edges)
print("\nAdjacency Matrix:")
for row in adj:
   print(*row)
def prims(graph):
    n=len(graph)
    selected=[0]*n
    selected[0]=1
    edges=0;cost=0
    print("edges:Cost")
    while edges<n-1:
        m=10**9;x=y=0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and 0<graph[i][j]<m:
                        m=graph[i][j];x=i;y=j
        print(f"{x}-{y}:{m}")
        cost+=m;selected[y]=1;edges+=1
    print("Minimum Cost:",cost)
n=int(input("Enter number of vertices:"))
print("enter adjacency matrix(0 if no edges):")
graph=[list(map(int,input().split())) for i in range(n)]
prims(graph)
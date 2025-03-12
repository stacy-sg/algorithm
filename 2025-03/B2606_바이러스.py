import sys
input = sys.stdin.readline

def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)

n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(v):
    x,y=map(int,input().split())
    graph[x]+=[y]
    graph[y]+=[x]

dfs(1)
print(sum(visited)-1)
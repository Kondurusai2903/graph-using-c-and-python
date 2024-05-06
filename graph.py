# ------------------------dfs
def dfs(adj, visited, node):
    visited[node] = True
    print(node, end=" ")
    for i in adj[node]:
        if (visited[i] == False):
            dfs(adj, visited, i)


adj = [[1, 2], [2, 3], [4 5], [], [], []]
visited = [0]*len(adj)
dfs(adj, visited, 0)

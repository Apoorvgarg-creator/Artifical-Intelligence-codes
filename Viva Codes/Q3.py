N = 1000
adj = [[] for i in range(N)]

def dfs_helper(u, node, visited, path, parent, target):
    visited[u] = True
    path.append([parent, u])
    if u == target:
        return True

    for x in adj[u]:
        if (not visited[x]):
            if dfs_helper(x, node, visited, path, u, target) == True:
                return True

    return False

def dfs(node, source, target):

    visited = [False for i in range(node)]

    path = []
    for i in range(node):
        visited[i] = False

    dfs_helper(source, node, visited, path, -1, target)
    
    print("Path followed: ")

    for i in path:
        if(i[0] == -1):
            continue
        print("{} - > {}".format(i[0], i[1]))


def insertEdge(u, v):

    adj[u].append(v)
    adj[v].append(u)

if __name__ == '__main__':
    node = int(input("Enter number of Nodes(0,N-1): "))
    edge = int(input("Enter number of Edges: "))
    print("Enter Edges: ")
    for i in range(edge):
        inp = input()
        x, y = int(inp.split(' ')[0]), int(inp.split(' ')[1])
        insertEdge(x, y)

    source = int(input("Enter Source: "))
    target = int(input("Enter Destination: "))

dfs(node, source, target)
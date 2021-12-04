N = 1000
adj = [[] for i in range(N)]
def dfs_helper(u, node,visited,path,parent,target):
    
    
    visited[u] = True
    path.append([parent, u])
    # print(u, end = " ")
    if u==target:
        return True

    for x in adj[u]:
 
        if (not visited[x]):
            if dfs_helper(x, node, visited,path,u,target)==True:
                return True

    return False

def dfs(node,source,target):
 
    visited = [False for i in range(node)]
 
    path = []
    for i in range(node):
        visited[i] = False
 
    dfs_helper(source, node, visited,path, -1,target)
    for i in path:
        print(i)
             
def insertEdge(u, v):
     
    adj[u].append(v)
    adj[v].append(u)
 
if __name__ == '__main__':
     

    node = 11
    edge = 13
 
    insertEdge(0, 1)
    insertEdge(0, 2)
    insertEdge(1, 5)
    insertEdge(1, 6)
    insertEdge(2, 4)
    insertEdge(2, 9)
    insertEdge(6, 7)
    insertEdge(6, 8)
    insertEdge(7, 8)
    insertEdge(2, 3)
    insertEdge(3, 9)
    insertEdge(3, 10)
    insertEdge(9, 10)
    source=0
    target=9
    
    dfs(node,source,target)
    
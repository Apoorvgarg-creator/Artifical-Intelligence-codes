from queue import PriorityQueue
v = 14

def best_first_search(source, target, n):
    visited = [False] * n
    visited[0] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        if u == target:
            print(u,end="")
            break
        print("{}->".format(u), end='')


        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


v = int(input("Enter number of Nodes(0,N-1): "))
graph = [[] for i in range(v)]
edge = int(input("Enter number of Edges: "))
print("Enter Edges: ")
for i in range(edge):
    inp = input()
    x, y, z = int(inp.split(' ')[0]), int(inp.split(' ')[1]), int(inp.split(' ')[2])
    addedge(x, y, z)

source = int(input("Enter Source: "))
target = int(input("Enter Destination: "))

# addedge(0, 1, 3)
# addedge(0, 2, 6)
# addedge(0, 3, 5)
# addedge(1, 4, 9)
# addedge(1, 5, 8)
# addedge(2, 6, 12)
# addedge(2, 7, 14)
# addedge(3, 8, 7)
# addedge(8, 9, 5)
# addedge(8, 10, 6)
# addedge(9, 11, 1)
# addedge(9, 12, 10)
# addedge(9, 13, 2)

source = 0
target = 9
best_first_search(source, target, v)
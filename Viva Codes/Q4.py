import random

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    
    return neighbours

def getnextneighbour(tsp, neighbours):
    curroutlength = routeLength(tsp, neighbours[0])
    nextneighbour = -1
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < curroutlength:
            curroutlength = currentRouteLength
            nextneighbour = neighbour
            break
    return nextneighbour, curroutlength

def hillClimbing(tsp):
    currentSolution = [3, 0, 4, 1, 2]
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    nextneighbour, nextneighbourRouteLength = getnextneighbour(tsp, neighbours)

    while nextneighbourRouteLength < currentRouteLength:
        currentSolution = nextneighbour
        currentRouteLength = nextneighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        nextneighbour, nextneighbourRouteLength = getnextneighbour(tsp, neighbours)
        if nextneighbour == -1:
            break

    return currentSolution, currentRouteLength

def main():
    tsp = [[6, 1, 8, 4, 5],[100, 5, 3, 4, 1],[20, 10, 0, 2, 100],[100, 2, 8, 6, 4],[1, 30, 5, 110, 2]]

    sol, sum = hillClimbing(tsp)

    print('Ans: ')
    for i in range(len(sol)):
        print(sol[i], end="")
        if i != len(sol)-1:
            print('->', end="")
    print('\nshortest route sum: {}'.format(sum))

if __name__ == "__main__":
    main()
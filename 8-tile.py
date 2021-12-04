def accept(n):
    puz = []
    for i in range(0, n):
        temp = input().split(" ")
        puz.append(temp)
    return puz

print("Enter the initial state matrix \n")
n = int(input("Enter size:"))
board = accept(n)

EmptyTileX = -1
EmptyTileY = -1
for i in range(0, n):
    for j in range(0, n):
        if board[i][j] == "-1":
            EmptyTileX, EmptyTileY = i, j

print(EmptyTileX,EmptyTileY)
print(50*"=" + "\n Apoorv (2019UIT3151) \n" + 50*"=")

print("Initial state:")
for y in range(0, n):
    for x in range(0, n):
        print(board[y][x], end=" ")
    print(end='\n')

while True:
    direction = input("Enter direction: (U,D,L,R)")
    if (direction == "D"):
        if (EmptyTileY + 1 < n):
            t = board[EmptyTileY + 1][EmptyTileX]
            board[EmptyTileY + 1][EmptyTileX] = board[EmptyTileY][EmptyTileX]
            board[EmptyTileY][EmptyTileX] = t
            EmptyTileY += 1
        else:
            print("Move not possible")
            continue
    elif (direction == "U"):
        if (EmptyTileY - 1 >= 0):
            t = board[EmptyTileY - 1][EmptyTileX]
            board[EmptyTileY - 1][EmptyTileX] = board[EmptyTileY][EmptyTileX]
            board[EmptyTileY][EmptyTileX] = t
            EmptyTileY -= 1
        else:
            print("Move not possible")
            continue
    elif (direction == "L"):
        if (EmptyTileX - 1 >= 0):
            t = board[EmptyTileY][EmptyTileX - 1]
            board[EmptyTileY][EmptyTileX - 1] = board[EmptyTileY][EmptyTileX]
            board[EmptyTileY][EmptyTileX] = t
            EmptyTileX -= 1
        else:
            print("Move not possible")
            continue
    elif (direction == "R"):
        if (EmptyTileX + 1 < n):
            t = board[EmptyTileY][EmptyTileX + 1]
            board[EmptyTileY][EmptyTileX + 1] = board[EmptyTileY][EmptyTileX]
            board[EmptyTileY][EmptyTileX] = t
            EmptyTileX += 1
        else:
            print("Move not possible")
            continue
    else:
        print("!! Unexpected direction !!")
        break

    for y in range(0, n):
        for x in range(0, n):
            print(board[y][x], end=" ")
        print(end='\n')


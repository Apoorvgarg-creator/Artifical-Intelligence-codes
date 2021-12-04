# import pygame
# import os
# n = 3
# pygame.init()
#
# w, h = 215, 215
#
# gameDisplay = pygame.display.set_mode((w, h))
#
# board = [["3","4","1"],["2","6","-1"],["5","7","8"]]
#
# EmptyTileX = 2
# EmptyTileY = 1
# print(EmptyTileX,EmptyTileY)
#
# application_path = os.path.dirname(__file__)
# application_path = application_path.replace('\\', '/')
#
# tile = pygame.image.load(application_path + "/tile.jpg")
#
# blank = pygame.image.load(application_path + "/blank.jpg")
#
#
# def navigate(direction, EmpXTile, EmpYTile):
#     if (direction == "D"):
#         if (EmpYTile + 1 < n):
#             t = board[EmpYTile + 1][EmpXTile]
#             board[EmpYTile + 1][EmpXTile] = board[EmpYTile][EmpXTile]
#             board[EmpYTile][EmpXTile] = t
#             EmpYTile += 1
#
#     elif (direction == "U"):
#         if (EmpYTile - 1 >= 0):
#             t = board[EmpYTile - 1][EmpXTile]
#             board[EmpYTile - 1][EmpXTile] = board[EmpYTile][EmpXTile]
#             board[EmpYTile][EmpXTile] = t
#             EmpYTile -= 1
#     elif (direction == "L"):
#         if (EmpXTile - 1 >= 0):
#             t = board[EmpYTile][EmpXTile - 1]
#             board[EmpYTile][EmpXTile - 1] = board[EmpYTile][EmpXTile]
#             board[EmpYTile][EmpXTile] = t
#             EmpXTile -= 1
#     elif (direction == "R"):
#         if (EmpXTile + 1 < n):
#             t = board[EmpYTile][EmpXTile + 1]
#             board[EmpYTile][EmpXTile + 1] = board[EmpYTile][EmpXTile]
#             board[EmpYTile][EmpXTile] = t
#             EmpXTile += 1
#     return EmpXTile, EmpYTile
#
#
# crashed = False
# while crashed == False:
#     # Capture frame-by-frame
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 EmptyTileX, EmptyTileY = navigate("U", EmptyTileX, EmptyTileY)
#             if event.key == pygame.K_LEFT:
#                 EmptyTileX, EmptyTileY = navigate("L", EmptyTileX, EmptyTileY)
#             if event.key == pygame.K_RIGHT:
#                 EmptyTileX, EmptyTileY = navigate("R", EmptyTileX, EmptyTileY)
#             if event.key == pygame.K_DOWN:
#                 EmptyTileX, EmptyTileY = navigate("D", EmptyTileX, EmptyTileY)
#     counter = -1
#     for y in range(0, n):
#         for x in range(0, n):
#             # print(x, position[x])
#             font = pygame.font.Font('freesansbold.ttf', 22)
#             tileNum = font.render(str(board[y][x]), True, (0, 0, 0)).convert_alpha()
#             counter += 1
#             if board[y][x] == "-1":
#                 gameDisplay.blit(blank, (x * 64 + 10, y * 64 + 10))
#                 continue
#             else:
#                 gameDisplay.blit(tile, (x * 64 + 10, y * 64 + 10))
#                 # print(x%n*120,x/n*120)
#             gameDisplay.blit(tileNum, (x * 64 + 30, y * 64 + 30))
#     pygame.display.update()

import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
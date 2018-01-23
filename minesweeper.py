# To-do list:
# - Implement flags
# - Implement gameplay changes that come with flags
# - Larger maps (custom ones, too)
# - Navigation system for large maps
# - Save and continue games
# - Menu (to access settings and maybe help)

import random

width = height = 9
totalmines = 10

def genmines(x, y):
    for _ in range(totalmines):
        mine = random.randint(0, width * height - 1)
        while mine in mines or mine == y * width + x:
            mine = random.randint(0, width * height - 1)
        mines.append(mine)
        
def calctile(x, y):
    minesfound = 0
    nearby = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
    tried.append(y * width + x)
    
    for near_x, near_y in nearby:
        near_x += x
        near_y += y
        if near_x < 0 or near_x >= width or near_y < 0 or near_y >= height:
            continue
        if near_y * width + near_x in mines:
            minesfound += 1
    if minesfound != 0:
        board[y * width + x] = str(minesfound)
    else:
        board[y * width + x] = " "
        
        for near_x, near_y in nearby:
            near_x += x
            near_y += y
            if near_x < 0 or near_x >= width or near_y < 0 or near_y >= height:
                continue
            if not near_y * width + near_x in tried:
                calctile(near_x, near_y)

def drawboard():
    print()
    for y in range(height):
        for x in range(width):
            print("[" + board[y * width + x] + "]", end="")
        print()

board = ["-"] * width * height
mines = []
tried = []
firstturn = True

print("\nWelcome to Minesweeper! Version 1.1.0")

while True:
    drawboard()
    print('\nInput the coordinates as "<x> <y>", e.g. "2 6".')
    print('Use mode \'P\' (in "<x> <y> [mode]") to preview chosen tile, e.g. "9 4 p".')
    coords = input("Coordinates: ").split()

    while True:
        valid = False
        if len(coords) < 2:
            print("At least 2 parameters required. Please try again.")
            coords = input("Coordinates: ").split()
            continue
        if len(coords) > 3:
            print("No more than 3 parameters allowed. Please try again")
            coords = input("Coordinates: ").split()
            continue
        if coords[0].isnumeric() and coords[1].isnumeric():
            x, y = int(coords[0]) - 1, int(coords[1]) - 1
        else:
            print("Coordinates must be written using numbers. Please try again.")
            coords = input("Coordinates: ").split()
            continue
        if x < 0 or x >= width or y < 0 or y >= height:
            print("Coordinates must exist on the board. Please try again.")
            coords = input("Coordinates: ").split()
            continue
        if y * width + x in tried:
            print("Tile must still be unturned. Please try again.")
            coords = input("Coordinates: ").split()
            continue
        if len(coords) == 3:
            if coords[2].upper() == "P":
                board[y * width + x] = "P"
                drawboard()
                print("\nFind 'P'. Is that the tile you want to pick?")
                print("Type anything to accept, or nothing to decline.")
                accept = input("Option: ")
                if not accept:
                    board[y * width + x] = "-"
                    drawboard()
                    print('\nInput the coordinates as "<x> <y>", e.g. "2 6".')
                    print('Use mode \'P\' (in "<x> <y> [mode]") to preview chosen tile, e.g. "9 4 p".')
                    coords = input("Coordinates: ").split()
                    continue
            else:
                print("That mode is not available. Please try again.")
                coords = input("Coordinates: ").split()
                continue
        break
    
    if firstturn:
        genmines(x, y)
        firstturn = False

    if y * width + x in mines:
        board[y * width + x] = "!"
        drawboard()
        print("\nYou uncovered a mine! You lose.")
        break

    calctile(x, y)

    if board.count("-") == totalmines:
        drawboard()
        print("\nYou uncovered all but the mines! You win.")
        break

print("Thanks for playing!")

# Coded on Python 3.6.3
# Connect Four 1.1.0

width = 7
height = 6
board = [" ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " "]
player = ["X", "O"]

def drawBoard():
    print()
    for y in range(height):
        for x in range(width):
            print("[" + board[y * width + x] + "]", end="")
        print()

def checkWin():
    for x in range(width - 3):
        for y in range(height):
            if board[y * width + x] == board[y * width + (x + 1)] == board[y * width + (x + 2)] == board[y * width + (x + 3)] != " ":
                return True
    for x in range(width):
        for y in range(height - 3):
            if board[y * width + x] == board[(y + 1) * width + x] == board[(y + 2) * width + x] == board[(y + 3) * width + x] != " ":
                return True
    for x in range(width - 3):
        for y in range(height - 3):
            if board[y * width + x] == board[(y + 1) * width + (x + 1)] == board[(y + 2) * width + (x + 2)] == board[(y + 3) * width + (x + 3)] != " ":
                return True
    for x in range(width - 3):
        for y in range(height - 3):
            if board[(y + 3) * width + x] == board[(y + 2) * width + (x + 1)] == board[(y + 1) * width + (x + 2)] == board[y * width + (x + 3)] != " ":
                return True
    return False

print("Welcome to Connect Four!")
drawBoard()
isPlaying = True
while isPlaying:
    players = [0, 1]
    for p in players:
        print("\nPlayer " + str(p + 1) + ": '" + player[p] + "'")
        
        validCol = False
        while not validCol:
            x = input("Col: ")
            if x.isnumeric():
                if not (int(x) > 7 or int(x) < 1):
                    x = int(x) - 1
                    validCol = True

        col = []
        for c in range(height):
            col += [board[c * width + x]]
        if not " " in col:
            players.insert(p, p * len(players))

        for y in range(height, 0, -1):
            if board[(y - 1) * width + x] == " ":
                board[(y - 1) * width + x] = player[p]
                break

        drawBoard()
            
        if checkWin():
            print("\nPlayer " + str(p + 1) + " wins!")
            winner = p
            isPlaying = False
            break

        if not " " in board:
            print("\nIt's a draw.")
            isPlaying = False
            break
print("\nThanks for playing!")

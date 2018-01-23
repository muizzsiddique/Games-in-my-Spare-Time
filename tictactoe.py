# Coded in Python 3.6.3
# Tic-tac-toe v1.2.0

import random

player = ["X", "O"]
wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 4, 8], [2, 4, 6]]

def drawBoard():
    print()
    for y in range(3):
        for x in board[y * 3:y * 3 + 3]:
            print("[" + x + "]", end="")
        print()

def checkWin():
    global wins
    for w, v, u in wins:
        if board[w] == board[v] == board[u] != " ":
            return True
    return False

def setPiece(): # A.I-sorta
    global wins
    for w, v, u in wins: # Always blocks...
        if board[w] == board[v] == "X" and board[u] == " ":
            board[u] = "O"
            return
        elif board[w] == board[u] == "X" and board[v] == " ":
            board[v] = "O"
            return
        elif board[v] == board[u] == "X" and board[w] == " ":
            board[w] = "O"
            return
    while True: # ...or plays a random move.
        square = random.randint(0, 8)
        if board[square] == " ":
            board[square] = "O"
            return
    

def menu():
    global mode
    while True:
        print("\nPlay the game in [S]ingleplayer or [M]ultiplayer, or [Q]uit.")
        menuInput = input("Option: ").upper()[:1]
        if menuInput == "S":
            mode = 0
            game()
        elif menuInput == "M":
            mode = 1
            game()
        elif menuInput == "Q":
            break
        else:
            continue

def game():
    global board
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    drawBoard()
    isPlaying = True
    while isPlaying:
        for p in range(2):
            print("\nPlayer ", p + 1, ": '" + player[p] + "'", sep="")
            lastPlay = False
            if board.count(" ") == 1:
                lastPlay = True
                board[board.index(" ")] = player[p]
            if not lastPlay:
                while (p == 0 or mode == 1): # Player one's turn unless multiplayer.
                    print("Pick a square [1-9]. Left-to-right; top-to-bottom.")
                    square = input("Square: ")
                    if square.isnumeric():
                        square = int(square) - 1
                        if square < 0 or square > 8:
                            continue
                        if board[square] == " ":
                            board[square] = player[p]
                            break
                if p == 1 and mode == 0: # Singleplayer: Computer's turn
                    setPiece()
            drawBoard()
            if checkWin():
                print("\nPlayer", p + 1, "wins!")
                isPlaying = False
                break
            if not " " in board:
                print("\nBoth players draw!")
                isPlaying = False
                break

print("Welcome to Tic-Tac-Toe!")
menu()

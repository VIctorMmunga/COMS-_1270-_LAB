# Victor Munga 10/12/2025
# Lab: Four In Sequence
# Description:
# A console-based Connect Four game that lets one or two players
# take turns dropping pieces into a grid. The goal is to connect
# four pieces horizontally, vertically, or diagonally.

import random
import sys

def printTitleMaterial():
    print("Four In Sequence!")
    print()
    print("By: <Victor Mmunga>")
    print("[COM S 127 #3]")
    print()

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice
def chooseNumPlayers():
    numPlayers = int(input("Number of Players? [1] / [2]: "))
    while numPlayers != 1 and numPlayers != 2:
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))
    return numPlayers

def printBanner():
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def getPlayerPiece(playerNumber):
    piece=""
    if playerNumber == 0:
        piece= "."
    elif playerNumber == 1:
        piece= "X"
    elif playerNumber == 2:
        piece= "O"
    return piece

def createBoard(width, height):
    empty = getPlayerPiece(0)
    board = []
    for i in range(0, height):
        board.append([])
        for j in range (0,width):
            board[i].append(empty)
    return board
def printBoard(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print()
    for i in range(0, len(board[0])):
        print(i, end=" ")
    print()
    print()
def getColumnInt(board, playerNumber):
     return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))

def getInputInRange(board, playerNumber):
    col = getColumnInt(board, playerNumber)
    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber)
    return col

def getHumanInput(board, playerNumber):
    col = getInputInRange(board, playerNumber)
    while getOpenRow(board, col) == -1:
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber)
    return col

def getOpenRow(board, col):
    empty = getPlayerPiece(0)
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == empty:
            return row
    return -1
def placePiece(board, row, col, piece):
    board[row][col] = piece
def dropPieceIntoBoard(board, col, playerNumber):
    row = getOpenRow(board, col)
    placePiece(board, row, col, getPlayerPiece(playerNumber))
def checkDraw(board):
    empty= getPlayerPiece(0)
    for row in board:
        for column in row:
         if column == empty:
            return False
    return True
def checkWinner(board, playerNumber):
    piece = getPlayerPiece(playerNumber)
    height = len(board)
    width = len(board[0])
    for row in range(0, len(board)):
        for column in range(0, len(board[0])-3):
            if board[row][column]== piece and board[row][column+1]== piece and board[row][column+2]== piece and board[row][column+3]==piece:
             return True
    for c in range(width):
        for r in range(height-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    for r in range(height-3):
        for c in range(width-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    for r in range(3, height):
        for c in range(width-3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False
def checkForNextMoveWin(board, playerNumber):
    empty = getPlayerPiece(0)
    piece = getPlayerPiece(playerNumber)
    for col in range(len(board[0])):  
        row = getOpenRow(board, col)  
        if row != -1:  
            placePiece(board, row, col, piece)  
            if checkWinner(board, playerNumber):  
                placePiece(board, row, col, empty)  
                return col  
            placePiece(board, row, col, empty)  
    return -1  
def checkAdjacent(board, playerNumber):
    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []
    for column in range(0, len(board[0])):
        row = getOpenRow(board, column)
        if row != -1:
            if row - 1 >= 0 and column - 1 >= 0:
                if board[row-1][column-1] == piece:
                    adjacents.append(column)
            if column - 1 >= 0:
                if board[row][column-1] == piece:
                    adjacents.append(column)
            if row + 1 < len(board) and column - 1 >= 0:
                if board[row+1][column-1] == piece:
                    adjacents.append(column)
            if row + 1 < len(board):
                if board[row+1][column] == piece:
                    adjacents.append(column)
            if row + 1 < len(board) and column + 1 < len(board[0]):
                if board[row+1][column+1] == piece:
                    adjacents.append(column)
            if column + 1 < len(board[0]):
                if board[row][column+1] == piece:
                    adjacents.append(column)
            if row - 1 >= 0 and column + 1 < len(board[0]):
                if board[row-1][column+1] == piece:
                    adjacents.append(column)
            if row - 1 >= 0:
                if board[row-1][column] == piece:
                    adjacents.append(column)

    if len(adjacents) > 1:
        randVal = random.randrange(0, len(adjacents))
        col = adjacents[randVal]
    return col
def getComputerInput(board, currentPlayerTurn):
    
    opponentPlayerTurn = switchTurns(currentPlayerTurn)
    col = checkForNextMoveWin(board, currentPlayerTurn)
    if col == -1:
        col = checkForNextMoveWin(board, opponentPlayerTurn)
    if col == -1:
        col = checkAdjacent(board, currentPlayerTurn)
    if col == -1:
        col = random.randrange(0, len(board[0]))
        while getOpenRow(board, col) == -1:
            col = random.randrange(0, len(board[0]))
    print(f"Player {currentPlayerTurn} (Computer) selects column {col}")
    return col
def resetGameOptions():
    currentPlayerTurn = 1
    winner = False
    draw = False
    return currentPlayerTurn, winner, draw

def switchTurns(currentPlayerTurn):
    return ((currentPlayerTurn % 2) + 1)

def printInstructions():
    print("Instructions: Connect Four in a row vertically, horizontally, or diagonally to win!")
    print("Players alternate turns and select a column to drop their piece.")
    print("Player 1 is 'X', Player 2 is 'O'. The computer uses 'O' when single-player mode is selected.")
    print("The game ends when a player wins or the board is full (draw).")
    print()
def main():
    running = True
    currentPlayerTurn = 1
    winner = False
    draw = False
    printTitleMaterial()
    while running:
        choice = initialChoice()
        if choice == "p":
            currentPlayerTurn, winner, draw = resetGameOptions()
            numPlayers = chooseNumPlayers()
            board = createBoard(7, 6)
            printBanner()
            printBoard(board)
            while True:
                if numPlayers == 1:
                    if currentPlayerTurn == 1:
                        col = getHumanInput(board, currentPlayerTurn)
                    elif currentPlayerTurn==2:
                        col = getComputerInput(board, currentPlayerTurn)
                    else:
                       print("ERROR: currentPlayerTurn is neither 1 or 2! it is actually:{0}".format(currentPlayerTurn))
                       sys.exit()
                elif numPlayers== 2:
                    col = getHumanInput(board, currentPlayerTurn)
                else:
                    print("ERROR: numPlayers is neither 1 or 2! it is actually:{0}".format(numPlayers))
                    sys.exit()
                dropPieceIntoBoard(board, col, currentPlayerTurn)
                printBoard(board)
                winner = checkWinner(board, currentPlayerTurn)
                draw = checkDraw(board)

                if winner == True:
                    print("~~ Player {0} ({1}) Wins! ~~".format(currentPlayerTurn,getPlayerPiece(currentPlayerTurn)))
                    print()
                    break
                elif draw== True:
                    print("~~ Draw! ~~")
                    print()
                    break
                else:
                    print("~~ End Of Player {0} ({1}) Turn ~~".format(
    currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                currentPlayerTurn = switchTurns(currentPlayerTurn)

        elif choice == "i":
            printInstructions()
        elif choice == "q":
            print("Goodbye! Thanks for playing Four In Sequence!")
            running = False
        else:
            print("ERROR: Invalid choice. Exiting.")
            quit()

if __name__ == "__main__":
    main()
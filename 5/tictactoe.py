import os
import time

board = [" "] * 10
player = 1
Game = 0
Mark = "X"

def DrawBoard():
    print(" {} | {} | {}".format(board[1], board[2], board[3]))
    print("___|___|___")
    print(" {} | {} | {}".format(board[4], board[5], board[6]))
    print("___|___|___")
    print(" {} | {} | {}".format(board[7], board[8], board[9]))
    print("   |   |   ")

def CheckPosition(x):
    return board[x] == " "

def CheckWin():
    global Game
    for i in range(1, 10, 3):  # Check rows
        if board[i] == board[i + 1] == board[i + 2] == Mark:
            Game = 1
            return
    for i in range(1, 4):  # Check columns
        if board[i] == board[i + 3] == board[i + 6] == Mark:
            Game = 1
            return
    if (
        board[1] == board[5] == board[9] == Mark
        or board[3] == board[5] == board[7] == Mark
    ):
        Game = 1
    if " " not in board[1:]:
        Game = -1

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print("Please Wait...")
time.sleep(1)

while Game == 0:
    os.system("cls")  # For Windows, use "clear" for Unix-like systems
    DrawBoard()
    print("Player {}'s chance".format(player))
    Mark = "X" if player % 2 != 0 else "O"
    choice = int(input("Enter the position between [1-9] where you want to mark: "))

    if 1 <= choice <= 9 and CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

os.system("cls")  # For Windows, use "clear" for Unix-like systems
DrawBoard()
if Game == -1:
    print("Game Draw")
else:
    print("Player {} Won".format(2 - (player % 2)))

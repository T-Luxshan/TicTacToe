
"""
    This is an ordinary game everyone used to play when they were kids.
    There are two options here
        1. Computer/AI mode
        2. Two player mode
    In computer mode you will play against an algorithm.
    In two players mode input for 'X' and 'O' will be get from the user.
    GO ahead and try this.....
"""
from board import *
import random

print("             _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("             *** Welcome to the Game Tic Tac Toe ***")
print("             _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print()
print()

while True:
    start = input("Do you want to dive in to the game? <Y / N> : ").strip()
    if start.lower() not in ['y', 'n']:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!Error: Just Input Y or N numbers!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()
    else:
        count = 0
        break

if start.lower() == 'n':
    print("Ta ta By By.....")
else:
    # Ask the user to select mood.
    def modeSelect():
        print("You can choose between these 2 modes to play")
        print("1. Computer/AI mode \n2. Two player mode")
        mode = input("Choose 1 / 2 :").strip()
        print()
        try:
            mode = int(mode)
            if mode == 1:
                print("Try not to lose....\nBecoz defeating an AI is Impossible")
                print()
                robot()
            elif mode == 2:
                players()
            return mode
        except:
            print("Invalid key !! Input 1 or 2")
            return False


    modes = ["computerMove(board)", "playerTwo()"]
    while True:
        isvalid = modeSelect()
        if isvalid:
            try:
                game_mood = modes[isvalid - 1]
                break
            except:
                print("Please select 1 or 2")


def main():
    board = [[' '] * 3, [' '] * 3, [' '] * 3]

    # Get Input from Player one.
    def playerOne():
        p1 = input("Your mark is 'X' \nWhere do you want to mark? \nInput Row and  Column: ").rstrip().split()
        print()
        if isValidInput(p1, board):  # Check input validity.
            board[int(p1[0]) - 1][int(p1[1]) - 1] = 'X'
            boardLocation(board)
            return True
        else:
            return False

    # Get Input from Player two.
    def playerTwo():
        p2 = input("Your mark is 'O' \nWhere do you want to mark? \nInput Row and  Column: ").rstrip().split()
        print()
        if isValidInput(p2, board):  # Check input validity.
            board[int(p2[0]) - 1][int(p2[1]) - 1] = 'O'
            boardLocation(board)
            return True
        else:
            return False

    # Algorithm for computer.
    def computerMove(b):

        # find empty coordinates to mark.
        possible_moves = []
        need_move = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    possible_moves.append([i, j])

        # mark 'O' is there any winning chances.
        for c in ['O', 'X']:
            for move in possible_moves:
                board_copy = b.copy()
                board_copy[move[0]][move[1]] = c
                if checkWin(board_copy)[0]:
                    board_copy[move[0]][move[1]] = ' '
                    board[move[0]][move[1]] = 'O'
                    print(f"Computer chose {move[0] + 1}, {move[1] + 1}")
                    print()
                    boardLocation(board)
                    need_move = False
                    break
                else:
                    board_copy[move[0]][move[1]] = ' '
                    need_move = True
            if not need_move:
                break

        # If no winning possibilities go for center box if that is empty.
        if need_move:  # Center position.
            if board[1][1] == ' ':
                board[1][1] = 'O'
                print("Computer chose 2, 2")
                print()
                boardLocation(board)

            # If 'X' was marked in the opposite corners, 'O' should be marked any middle box.
            # This move avoids a tricky move of 'X'.
            elif (board[0][0] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[2][0] == 'X'):
                middle = [[1, 2], [2, 1], [2, 3], [3, 2]]
                possible_middles = [i for i in middle if i in possible_moves]
                random_middle = random.choice(possible_middles)
                board[random_middle[0]][random_middle[1]] = 'O'
                print("Computer chose", random_middle[0] + 1, random_middle[1] + 1)
                boardLocation(board)
                print()

            # Then go for the corners to avoid another tricky move of 'X'.
            elif any(i in possible_moves for i in [[0, 0], [0, 2], [2, 0], [2, 2]]):
                corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
                possible_corners = [i for i in corners if i in possible_moves]
                random_corner = random.choice(possible_corners)
                board[random_corner[0]][random_corner[1]] = 'O'
                print("Computer chose", random_corner[0] + 1, random_corner[1] + 1)
                print()
                boardLocation(board)

            # Then go for middle boxes.
            else:
                middle = [[1, 2], [2, 1], [2, 3], [3, 2]]
                possible_middles = [i for i in middle if i in possible_moves]
                random_middle = random.choice(possible_middles)
                board[random_middle[0]][random_middle[1]] = 'O'
                print("Computer chose", random_middle[0] + 1, random_middle[1] + 1)
                boardLocation(board)
                print()
        return True

    # Check whether win or not.
    def checkWin(b):
        row = rowCheck(b)
        if row[0]:  # Checking row by row.
            victory = True
            return victory, row[1]
        col = columnCheck(b)
        # Checking column by column.
        if col[0]:
            victory = True
            return victory, col[1]

        l_d = leftDiagonalCheck(b)
        if l_d[0]:  # Checking Left Diagonal.
            victory = True
            return victory, l_d[1]

        r_d = rightDiagonalCheck(b)
        if r_d[0]:  # Checking right Diagonal.
            victory = True
            return victory, r_d[1]

        victory = False
        return victory, 0

    # Check whether tie or not.
    def checkTie():

        for t in range(3):
            if ' ' in board[t]:
                return False
        print()
        print("================")
        print("== It's a TIE ==")
        print("================")
        return True

    boardLocation(board)
    print()

    # Loop the program till tie or one of them win.
    while True:
        while True:
            is_valid = playerOne()
            if is_valid:
                break
        is_win = checkWin(board)
        if is_win[0] or checkTie():
            break

        while True:
            is_valid = eval(game_mood)
            if is_valid:
                break
        is_win = checkWin(board)
        if is_win[0] or checkTie():
            break
    if is_win[0]:
        winner(is_win[1])
    return is_win[1]


x_win = 0
o_win = 0
tie = 0

# This block makes sure that this game runs infinite times until the user says no.
if start.lower() == 'y':
    while True:
        if count > 0:
            while True:
                start = input("Do you want to dive in to the game?< Y / N > :").strip()
                if start.lower() in ['y', 'n']:
                    break
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!Error: Just Input Y / N numbers!!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print()
        if start.lower() == 'y':
            count += 1
            who = main()
            if who == 'X':
                x_win += 1
            elif who == 'O':
                o_win += 1
            else:
                tie += 1
        else:
            break

# Ask for summary.
while True:
    report = input("Do you want your game record? <Y/N> :")
    if report.lower() in ['y', 'n']:
        break
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!Error: Just Input Y / N numbers!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()

if report.lower() == 'y':
    print("Total Game Played:", count)
    print("      X wins     :", x_win)
    print("      O wins     :", o_win)
    print("      Ties       :", tie)

print(" Ta Ta By By, Have a Good Day")

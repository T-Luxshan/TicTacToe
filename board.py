
def boardLocation(b):
    print("         |         |         ")
    print("    " + b[0][0] + "    |" + "    " + b[0][1] + "    |" + "    " + b[0][2])
    print("         |         |         ")
    print("-----------------------------")

    print("         |         |         ")
    print("    " + b[1][0] + "    |" + "    " + b[1][1] + "    |" + "    " + b[1][2])
    print("         |         |         ")
    print("-----------------------------")

    print("         |         |         ")
    print("    " + b[2][0] + "    |" + "    " + b[2][1] + "    |" + "    " + b[2][2])
    print("         |         |         ")


def players():
    print("   (＾◡＾)_/\_(＾◡＾)   [ Hello, Players 🙂!]")
    print("    /¯|         |¯\ ")
    print("      |         |   ")
    print("     / \       / \  ")
    print()


def robot():
    print("       \  /")
    print("      [▪‿▪]_/ [ Greetings! opponent!]")
    print("      /¯|      [ Let's Play  ♪└|∵|┐♪ ]")
    print("        |     ")
    print("       / \    ")
    print()


# Check whether input is correct or not.
def isValidInput(arr, b):
    try:
        arr = list(map(int, arr))
        if any(x > 3 for x in arr):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!Row and Column must be less than three!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print()
            valid = False

        elif len(arr) != 2:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!Error: Just Input 2 numbers!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print()
            valid = False

        elif b[int(arr[0]) - 1][int(arr[1]) - 1] != ' ':
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!That box is filled Already, Try another!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print()
            valid = False
        else:
            valid = True

    except:

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!Please input Valid number!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()
        valid = False

    return valid


# Check winning possibilities
# Checking row by row.
def rowCheck(b):
    for i in b:
        if " " not in i:
            if 'X' in i and 'O' in i:
                continue
            else:
                return True, i[0]
    return False, 0


# Checking column by column.
def columnCheck(b):
    for i in range(3):
        temp = []
        for j in range(3):
            if b[j][i] != " ":
                temp.append(b[j][i])
        if len(temp) == 3 and not ('X' in temp and 'O' in temp):
            return True, temp[0]
    return False, 0


# Checking Left Diagonal.
def leftDiagonalCheck(b):
    diagonal_left = True
    diagonal_left_element = []
    for i in range(3):
        if b[i][i] == ' ':
            diagonal_left = False
            break
        else:
            diagonal_left_element.append(b[i][i])
    if diagonal_left and (len(diagonal_left_element) == 3 and
                          not ('X' in diagonal_left_element and 'O' in diagonal_left_element)):
        return True, b[1][1]
    return False, 0


# Checking right Diagonal.
def rightDiagonalCheck(b):
    diagonal_right = True
    diagonal_right_element = []
    for i in range(2, -1, -1):
        if b[2 - i][i] == ' ':
            diagonal_right = False
            break
        else:
            diagonal_right_element.append(b[2 - i][i])

    if diagonal_right and (len(diagonal_right_element) == 3 and
                           not ('X' in diagonal_right_element and 'O' in diagonal_right_element)):
        return True, b[1][1]
    return False, 0


# Winner print Pattern.
def winner(who):
    # if who == "X":
    print()
    print("#################################")
    print(f"##     The Winner is '{who}'", "\N{Party Popper}    ##")
    print("#################################")
    print()
    return who

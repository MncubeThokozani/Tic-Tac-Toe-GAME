import random


print("Welcome to Tic Tac Toe")
possibleNo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gamebord = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
columns = 3


def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(columns):
            print("", gamebord[x][y], end=" |")
    print("\n+---+---+---+")


def modifyArray(num, turn):
    num -= 1
    if num == 0:
        gamebord[0][0] = turn
    elif num == 1:
        gamebord[0][1] = turn
    elif num == 2:
        gamebord[0][2] = turn
    elif num == 3:
        gamebord[1][0] = turn
    elif num == 4:
        gamebord[1][1] = turn
    elif num == 5:
        gamebord[1][2] = turn
    elif num == 6:
        gamebord[2][0] = turn
    elif num == 7:
        gamebord[2][1] = turn
    elif num == 8:
        gamebord[2][2] = turn


def checkforWinner(gamebord):
    #x axis
    if(gamebord[0][0]=="X" and gamebord[0][1]=="X" and gamebord[0][2]=="X"):
        print("X has won!")
        return "X"
    elif(gamebord[0][0]=="O" and gamebord[0][1]=="O" and gamebord[0][2]=="O"):
        print("O has won!")
        return"O"
    elif (gamebord[1][0]=="X" and gamebord[1][1]=="X" and gamebord[1][2]=="X"):
        print("X has won!")
        return"X"
    elif (gamebord[1][0] == "O" and gamebord[1][1] == "O" and gamebord[1][2] == "O"):
        print("O has won!")
        return "O"
    elif(gamebord[2][0]=="X" and gamebord[2][1]=="X" and gamebord[2][2]=="X"):
        print("X has won!")
        return"X"
    elif (gamebord[2][0] == "O" and gamebord[2][1] == "O" and gamebord[2][2] == "O"):
        print("O has won!")
        return "O"
    #y-axis
    elif(gamebord[0][0]=="X" and gamebord[1][0]=="X" and gamebord[2][0]=="X"):
        print("X has won!")
        return "x"
    elif (gamebord[0][0] == "O" and gamebord[1][0] == "O" and gamebord[2][0] == "O"):
        print("O has won!")
        return "O"
    elif (gamebord[0][1] == "X" and gamebord[1][1] == "X" and gamebord[2][1] == "X"):
        print("X has won!")
        return "x"
    elif (gamebord[0][1] == "O" and gamebord[1][1] == "O" and gamebord[2][1] == "O"):
        print("O has won!")
        return "O"
    elif (gamebord[0][2] == "X" and gamebord[1][2] == "X" and gamebord[2][2] == "X"):
        print("X has won!")
        return "x"
    elif (gamebord[0][2] == "O" and gamebord[1][2] == "O" and gamebord[2][2] == "O"):
        print("O has won!")
        return "O"
    #crossboard
    elif(gamebord[0][0]=="X" and gamebord[1][1]=="X" and gamebord[2][2]=="X"):
        print("X has won!")
        return "X"
    elif (gamebord[0][0] == "O" and gamebord[1][1] == "O" and gamebord[2][2] == "O"):
        print("O has won!")
        return "O"
    elif(gamebord[0][2]=="X"and gamebord[1][1]=="X" and gamebord[2][0]=="X"):
        print("X has won!")
        return "X"
    elif (gamebord[0][2] == "O" and gamebord[1][1] == "O" and gamebord[2][0] == "O"):
        print("O has won!")
        return "O"
leaveLoop = False
turnCounter = 0

while not leaveLoop:
    if turnCounter % 2 == 1:
        printGameBoard()
        numberpicked = int(input("\nChoose a number [1-9]: "))
        if 1 <= numberpicked <= 9 and numberpicked in possibleNo:
            modifyArray(numberpicked, "X")
            possibleNo.remove(numberpicked)
            winner = checkforWinner(gamebord)
            if winner:
                leaveLoop = True

        else:
            print("invalid input. Pleas try again")

    else:
        if possibleNo:
            print("CPU's turn: ")
            cpuChoice = random.choice(possibleNo)
            print("Choice: ", cpuChoice)
            modifyArray(cpuChoice, "O")
            possibleNo.remove(cpuChoice)
            winner = checkforWinner(gamebord)
            if winner:
                leaveLoop = True
            elif not possibleNo:
                print("It's a tie!")

                leaveLoop = True

    turnCounter += 1
    #C:\Users\thoko\PycharmProjects\pythonProject\Project.py




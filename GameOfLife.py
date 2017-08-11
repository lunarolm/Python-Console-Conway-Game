import copy
import time

board = [[0, 0, 0, 0, 0]
    ,[0, 0, 0, 0, 0]
    ,[0, 0, 0, 1, 0]
    ,[0, 0, 0, 1, 0]
    ,[0, 0, 0, 1, 0]]

gameRunning = True
i = 0

def cellOnCheck(num):
    return (num == 1)

while gameRunning:
    i += 1

    tempBoard = copy.deepcopy(board)

    for x in range (0, len(board)):
        print (board[x])
        for y in range (0, len(board)):
            #print("y=", y)
            neighbourNum = 0
            try:
                if(cellOnCheck(board[x][y + 1])):#checks cell immediately to the right
                    neighbourNum +=1
            except Exception:
                #print("barrier right of ", x, y)
                pass

            if (cellOnCheck(board[x][y - 1])):#checks cell immediately to the left
                neighbourNum += 1

            if (cellOnCheck(board[x -1][y])):#checks cell immediately above
                neighbourNum += 1

            try:
                if (cellOnCheck(board[x + 1][y])):#checks cell immediately below
                    neighbourNum += 1
            except Exception:
                #print("barrier down of ", x, y)
                pass
            try:
                if (cellOnCheck(board[x - 1][y -1])):#checks cell to the northwest
                    neighbourNum += 1
            except Exception:
                pass
            try:
                if (cellOnCheck(board[x - 1][y + 1])):#checks cell to the northeast
                    neighbourNum += 1
            except Exception:
                pass
            try:
                if (cellOnCheck(board[x + 1][y -1])):#checks cell to the southwest
                    neighbourNum += 1
            except Exception:
                pass
            try:
                if (cellOnCheck(board[x + 1][y + 1])):#checks cell to the southeast
                    neighbourNum += 1
            except Exception:
                pass


            if cellOnCheck(board[x][y]):#cell is alive
                #print ("detected 1!", neighbourNum, "", x, "", y)
                if (neighbourNum < 2 or neighbourNum > 3):#cell dies if it has less than two neighbours or more than three
                    tempBoard[x][y] = 0
                    #print("killed cell at", x, y)
                #pass if cell has two or three neighbours
            if not cellOnCheck(board[x][y]):
                if (neighbourNum == 3):#cell is born if empty cell has exactly 3 neighbours
                    tempBoard[x][y] = 1
                    #print("created cell at",x, y)

    #updates the board
    board = copy.deepcopy(tempBoard)
    print("updated board!")

    if(i >= 5):
        gameRunning = False
        break
    print("\n")
    time.sleep(0.3)
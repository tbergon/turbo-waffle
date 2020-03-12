import itertools    




def win(board):


    #Stalemate
    if board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and board[1][0] != 0 and board[1][1] != 0 and board[1][2] != 0 and board[2][0] != 0 and board[2][1] != 0 and board[2][2] != 0:
        print("No one wins, everyone loses")
        return True

    #Horizontal
    for row in board:
        print(row)
        if row.count(row[0])==len(row) and row[0] != 0:
            print("Player",row[0],"wins :)")
            return True
                

    #Vertical
    
    for column in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[column])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Player",check[0],"wins :)")
            return True

    #Diagonal /

    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != 0:
        print("Player", board[1][1],"wins :)") 
        return True

    #Diagonal \
    
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != 0: 
        print("Player", board[1][1],"wins :)")
        return True

    return False

    


def printBoard(player=0, row=0, column=0, displayOnly = False):
    
    print("   0  1  2")
    if not displayOnly:
        board[row][column] = player
    count=0
    for row in board:
        print(count, row)
        count+=1
    return board
    
    


play = True
player = [1,2]
while play:
    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    gamewon = False
    playerTurns = itertools.cycle([1,2])
    printBoard(board, displayOnly=True)
    while not gamewon:  
        currentPlayer = next(playerTurns)
        print("Player :",currentPlayer)
        columnChoice = int(input("Which column ? "))
        if columnChoice > 2:
            while columnChoice > 2:
                columnChoice = int(input("Select a number between 0 and 2 : "))
        rowChoice = int(input("Which row ? " ))
        if rowChoice > 2:
            while rowChoice > 2:
                rowChoice = int(input("Select a number between 0 and 2 : "))
        while board[rowChoice][columnChoice] != 0:
            print("There's already something here, try another space ! ")
            columnChoice = int(input("Which column ? "))
            if columnChoice > 2:
                while columnChoice > 2:
                    columnChoice = int(input("Select a number between 0 and 2 : "))
            rowChoice = int(input("Which row ? " ))
            if rowChoice > 2:
                while rowChoice > 2:
                    rowChoice = int(input("Select a number between 0 and 2 : "))

        
    
        board=printBoard(currentPlayer,rowChoice,columnChoice)

        if win(board):
            gamewon = True
            play = False
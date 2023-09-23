

def show_board(x,y,z,matrix):

    matrix[x][y]=z
    line=0
    for row in matrix:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        line+=1
        if line<=2:
            print("---------")


def player1(message="(X) Please enter row and column with colon mark:"):
    player1=input(message)
    return player1.replace(":","").strip()

def player2(message="(O)Please enter row and column with colon mark:"):
    player2=input(message)
    return player2.replace(":", "").strip()



m = [[" ", " ", " "], [" ", " "," "], [" ", " ", " "]]
def game(matrix):

    player_1=player1()
    row=int(player_1[0])-1
    column=int(player_1[1])-1
    while matrix[row][column] !=" ":
        player_1 = player1(message="Is not blank.Try again:")
        row = int(player_1[0]) - 1
        column = int(player_1[1]) - 1
    show_board(x=row,y=column,z="X",matrix=matrix)
    game_over = game_check(matrix=matrix)
    if game_over :
        print("Player 1 won")
        return play_again()
    elif is_draw(matrix=matrix):
        print("Draw!")
        return play_again()
    player_2=player2()
    row_2 = int(player_2[0]) - 1
    column_2 = int(player_2[1]) - 1
    while matrix[row_2][column_2] !=" ":
        player_2 = player2(message="Is not blank.Try again:")
        row_2 = int(player_2[0]) - 1
        column_2 = int(player_2[1]) - 1
    show_board(x=row_2, y=column_2, z="O", matrix=matrix)
    game_over = game_check(matrix)
    if game_over:
        print("Player 2 won")
        return play_again()
    elif is_draw(matrix):
        print("Draw")
        return play_again()

    else:
        game(matrix)


def game_check(matrix):
    chk=False
    for row in matrix:
        item=row[0]
        if row.count(item)==len(row) and item!=" ":
            return True
    cond1=True
    item_diag=matrix[0][0]
    item_xdiag=matrix[0][2]
    for i in range(3):
        for j in range(3):
            if i==j:
                if matrix[i][j]!=item_diag or matrix[i][j]==" ":
                    cond1=False
    cond2=True
    for i in range(3):
        for j in range(3):
            if i==j+2 or i==2-j:
                if matrix[i][j]!=item_xdiag or matrix[i][j]==" ":
                    cond2=False

    cond3=False
    for j in range(3):
        listc=[]
        for i in range(3):
            listc.append(matrix[i][j])
        if len(set(listc))==1 and " " not in listc:
            cond3=True

    chk=(cond1 or cond2 or cond3)

    return chk

def is_draw(matrix):
    draw=True
    for row in matrix:
        if " " in row:
            draw=False

    return draw
def play_again():
    replay= input("Are you want to play again (yes/no):")
    if replay == "yes":
        new_m = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        game(matrix=new_m)
    else:
        return "Game ended"

game(matrix=m)

from random import randrange

def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision
    while True :
        try :
            User_Enter = int(input("entrer un nombre entre 1 et 9 : "))
            if User_Enter<1 or User_Enter >9 :
                print("entrer un entier entre 1 et 9 : ")
                continue
            found = False
            for i in range(3):
                for j in range(3):
                    if board[i][j]== User_Enter :
                        board[i][j]='O'
                        found = True
                        break
            if not found :
                print("case occupée ")
                continue
            
            break


        except ValueError :
            print("ERREURR : entrer un entier svp : ")
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    my_list = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                my_list.append((i,j))
    return my_list


def victory_for(board, sign):
    # Vérifier lignes
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return "You are the winner!"

    # Vérifier colonnes
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return "You are the winner!"

    # Vérifier diagonale principale
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return "You are the winner!"

    # Vérifier diagonale secondaire
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return "You are the winner!"

    return "No winner yet."


def draw_move(board):
    # Tant qu'il reste des cases libres, on en choisit une au hasard
    while True:
        i = randrange(3)  # ligne aléatoire entre 0 et 2
        j = randrange(3)  # colonne aléatoire entre 0 et 2
        
        # Vérifie si la case est libre (un nombre)
        if isinstance(board[i][j], int):
            board[i][j] = 'X'
            break


   
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

while True:
    enter_move(board)   # Coup joueur
    display_board(board)
    result = victory_for(board, 'O')
    if result != "No winner yet.":
        print(result)
        break

    draw_move(board)    # Coup ordinateur
    display_board(board)
    result = victory_for(board, 'X')
    if result != "No winner yet.":
        print(result)
        break

    # Vérifier égalité ici (plus de cases libres)
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break


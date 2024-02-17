board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = 'X'
Anexerous = 'O'

def print_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[7] + " | " + board[8] + " | " + board[9])

def spaceisfree(position):
    if board[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if spaceisfree(position):
        board[position] = letter 
        print_board(board)
        if Draw():
            print("Draw!")
            exit() 
        if Win():
            if letter == 'X':
                print("Congratulations!! You won")
                exit()
            else:
                print("Anexerous Wins!!!")
                exit()
        return 
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return  

def Win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False 
    
def checkwinner(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def Draw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove():
    position = int(input("Enter the position: "))
    insertLetter(player, position)
    return 

def Annex():
    bestscore = -1000
    bestmove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = Anexerous
            score = minimax(board, False)
            board[key] = ' '
            if score > bestscore:
                bestscore = score
                bestmove = key
    insertLetter(Anexerous, bestmove)
    return

def minimax(boars, maximizing):
    if checkwinner(Anexerous):
        return 1
    elif checkwinner(player):
        return -1
    elif Draw():
        return 0
    if maximizing:
        bestscore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = Anexerous
                score = minimax(board, False)
                board[key] = ' '
                if score > bestscore:
                    bestscore = score
        return bestscore
    else:
        bestscore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestscore:
                    bestscore = score
        return bestscore


while not Win():
    Annex()
    playerMove()
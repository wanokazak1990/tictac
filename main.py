# -*- coding: utf-8 -*-
X = 'X' 
O = 'O'
EMPTY = ' '
TIE = 'НИЧЬЯ'
NUM_SQUARES = 9

def ask_yes_no(question):
    response = None
    while response not in ('y','n'):
        response = raw_input(question).lower()
    return response

def ask_number(question,low,high):
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no("ХОЧЕШЬ ХОДИТЬ ПЕРВЫМ (y/n)? =>")
    if(go_first == 'y'):
        print('Игрок ходит первым')
        human = X
        computer = O
    else:
        print('Компьютер ходит первым')
        human = O
        computer = X
    return (human,computer)

def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print '\n\t','_____________'
    print "\n\t|",board[0],"|",board[1],"|",board[2],"|"
    print "\n\t","_____________"
    print "\n\t|",board[3],"|",board[4],"|",board[5],"|"
    print "\n\t","_____________"
    print "\n\t|",board[6],"|",board[7],"|",board[8],"|"
    print "\n\t","_____________"
    print "\n"

def legal_moves(board):
    moves = []
    for i in range(NUM_SQUARES):
        if(board[i] == EMPTY):
            moves.append(i)
    return moves

def winner(board):
    COMBO = (
            (0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6)
        )
    for row in COMBO:
        if(board[row[0]] == board[row[1]] == board[row[2]] != EMPTY):
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
            return TIE
    return None

def human_move(board,human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход выбери поле => ",0,NUM_SQUARES)
        if(move not in legal):
            print("Это поле уже занято, выбери другое поле")
    print("Ход засчитан")
    return move

def computer_move(board,computer,human):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    for move in legal_moves(board):
        board[move] = computer

        if(winner(board) == computer):
           print "Компьютер сходил в ячейку =>",move
           return(move)
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if(winner(board) == human):
            print"Компьютер сходил в ячейку =>",move
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print "Компьютер сходил в ячейку =>",move
            return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(win,computer,human):
    if(win != TIE):
        print("3 В РЯД")
    else:
        print("НИЧЬЯ")
    if(win == computer):
        print ("Победу одержал компьютер")
    elif(win == human):
        print("Победу одержал человек")
    elif(win == TIE):
        print ("Ещё партеечку?")

def main():
    human,computer = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if(turn == human):
            move = human_move(board,human)
            board[move] = human
        else:
           move = computer_move(board,computer,human)
           board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    win = winner(board)
    congrat_winner(win,computer,human)

main()

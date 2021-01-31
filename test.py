import numpy as np


def board():
    #create board
    board = [['.']*3]*3
    return board

def valid_input(board, x, y):
    
    #chek for valid input in range len(board)
    if x <= len(board)-1 and y <= len(board)-1 and board[x][y] == '.':
        return True
    else:
        return False
    
def end_check(board):
    
    #chek for Vertical and Horizontal
    for i in range(len(board)):
        
        if board[i][0] != '.' and board[i].count(board[i][0]) == len(board):
            return board[i][0]
        
        transposed=[ list(e) for e in zip(*board)]   
        if transposed[i][0] != '.' and transposed[i].count(transposed[i][0]) == len(board):
            return transposed[i][0]
    
    #chek for diagonal     
    temp1 = np.array(board)
    temp2 = np.flip(temp1, axis=1)
    temp1_diag = list(np.diag(temp1))
    temp2_diag = list(np.diag(temp2))
    
    if temp1_diag[0] != '.' and temp1_diag.count(temp1_diag[0]) == len(board):
        return temp1_diag[0]
    
    if temp2_diag[0] != '.' and temp2_diag.count(temp2_diag[0]) == len(board):
        return temp2_diag[0]
    
    #chek for end game
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                return None     
    

def evaluation_function(board, player_turn, opponent_turn):
    
    opponent_number = 0
    player_number = 0
    
    #chek for Vertical and Horizontal   
    for i in range(len(board)):
        if player_turn in board[i] and opponent_turn not in board[i]:
            player_number += 1 
        if opponent_turn in board[i] and player_turn not in board[i]:
            opponent_number += 1
        if [player_turn, opponent_turn] not in board[i]:
            opponent_number += 1
            player_number += 1
        
        transposed=[ list(e) for e in zip(*board)]
        if player_turn in transposed[i] and opponent_turn not in transposed[i]:
            player_number += 1 
        if opponent_turn in transposed[i] and player_turn not in transposed[i]:
            opponent_number += 1
        if [player_turn, opponent_turn] not in transposed[i]:
            opponent_number += 1
            player_number += 1
    
    #chek for diagonal   
    temp1 = np.array(board)
    temp2 = np.flip(temp1, axis=1)
    temp1_diag = list(np.diag(temp1))
    temp2_diag = list(np.diag(temp2))
    
    if player_turn in temp1_diag and opponent_turn not in temp1_diag:
        player_number += 1 
    if opponent_turn in temp1_diag and player_turn not in temp1_diag:
        opponent_number += 1
    if [player_turn, opponent_turn] not in temp1_diag:
        opponent_number += 1
        player_number += 1
    
    if player_turn in temp2_diag and opponent_turn not in temp2_diag:
        player_number += 1 
    if opponent_turn in temp2_diag and player_turn not in temp2_diag:
        opponent_number += 1
    if [player_turn, opponent_turn] not in temp2_diag:
        opponent_number += 1
        player_number += 1  
        
    return player_number-opponent_number        



def com(board):
    current_board = board
    temp = []
    for i in range(len(current_board)):
        for j in range(len(current_board)):
            if current_board[i][j] == '.':
                current_board[i][j] = 'O'
                temp.append([evaluation_function(current_board, 'X', 'O'),i,j])
                current_board[i][j] = '.'
    
    transposed=[ list(e) for e in zip(*temp)]
    choice = min(transposed[0])
    temp2 = transposed[0].index(choice)            
    return [transposed[1][temp2], transposed[2][temp2]] 
        

def draw_board(board):
    for i in range(0, 3):
        for j in range(0, 3):
            print('{}|'.format(board[i][j]), end=" ")
        print()
    print()



def player(board):
    
    play_board = board
    player_turn = 'X'
    
    while True:
        draw_board(play_board)
        game_status = end_check(play_board)
        
        if game_status != None:
            if game_status == 'X':
                print('The winner is X!')
            elif game_status == 'O':
                print('The winner is O!')
            elif game_status == '.':
                print("It's a tie!")
            break

        
        if player_turn == 'X':
            
            while True:
                
                px = int(input('Insert the X coordinate: '))
                py = int(input('Insert the Y coordinate: '))
                
                
                if valid_input(play_board, px, py):
                    play_board[px][py] = 'X'
                    player_turn = 'O'
                    break
                else:
                    print('The move is not valid! Try again.')
        else:
            temp = com(play_board)
            play_board[temp[0]][temp[1]] = 'O'
            player_turn = 'X'




             
player(board())                
        
        
        
        
        
        
        
        
        
        
        
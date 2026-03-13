from collections import deque

def check_winner(board):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        if board[w[0]]==board[w[1]]==board[w[2]] and board[w[0]]!="":
            return board[w[0]]
    return None
def draw_board(board):
    for i in range(0,9,3):
        print(board[i]," | ",board[i+1]," | ",board[i+2])
    print()
def bfs_ai_move(board,player):
    queue=deque()
    queue.append((board,player,None))
    while queue:
            current_board,current_player,first_move=queue.popleft()
            winner=check_winner(current_board)
            if winner==player:
                 return first_move
            next_player="O"if current_player=="X" else "X"
            for i in range(9):
                 if current_board[i]=="":
                      new_board=current_board.copy()
                      new_board[i]=current_player
                      move=i if first_move is None else first_move
                      queue.append((new_board,next_player,move))
    return None
board=[""]*9
current_player="X"
while True:
     draw_board(board)
     if current_player=="X":
          move=int(input("enter the position(0-8)"))
          if board[move]!="":
               print("invalid move")
               continue
          board[move]="X"
     else:
        move=bfs_ai_move(board,"O")
        if move is None:
             move=board.index("")
        board[move]="O"
        print("ai choose move",move)

     winner=check_winner(board)
     if winner:
          draw_board(board)
          print("winner ",winner)
     if "" not in board:
          draw_board(board)
          print("draw")
     current_player="O"if current_player=="X" else "X"
    


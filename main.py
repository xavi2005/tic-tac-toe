import random
import pygame
# import sys
from constantes import *
from funcionsExtras import *



pygame.init()
pygame.font.init()
pygame.font.Font
screen = pygame.display.set_mode(SIZE)
screen.fill(SCREEN)
pygame.display.set_caption("TRES EN RAYA")
my_font = pygame.font.SysFont('Comic Sans MS', 60)

def draw(row,col,player):
  if player == 1:
    pygame.draw.circle(screen, WHITE , (col*WIDTH_P + WIDTH_P / 2 , row*HEIGHT_P + HEIGHT_P / 2) , HEIGHT_P/2 - RECORT, width = 10)
  elif player == -1:
    pygame.draw.line(screen , BLACK , (col*WIDTH_P + RECORT , row*HEIGHT_P + RECORT ) , (col*WIDTH_P + WIDTH_P -RECORT, row*HEIGHT_P +HEIGHT_P - RECORT ), width= 10)
    pygame.draw.line(screen, BLACK , (col*WIDTH_P + RECORT, row*HEIGHT_P + HEIGHT_P -RECORT  ) , (col*WIDTH_P + (WIDTH_P -RECORT) , row*HEIGHT_P + RECORT) , width=10 )


class Board:
  def __init__(self):
    self.board = BOARD
    self.search_empty()
    
    
    
  
  def is_empty(self ,row , col):
    if self.board[row][col] == 0:
      
      return True
    else:
      return False
  
  def mark_change(self , row , col ,player):
    if self.is_empty(row , col) == True:
       self.board[row][col] = player
       draw(row,col,player)
    else:
      print ( "Espai ocupat")
    
  
  def search_empty(self):
    empty = 0
    for i in range(0,3):
      for j in range(0,3):
        if self.board[i][j] == 0:
          empty += 1
    return empty
  
  def list_empty(self):
    empty = []
    for i in range(0,3):
      for j in range(0,3):
        if self.board[i][j] == 0:
          empty += []
    
    return empty
  
  def color_player(self,player):
    if player == 1:
      return WHITE
    else:
      return BLACK
  
  def check_win(self, player):
    COLOR = self.color_player(player)
    if self.board[0][0] == self.board[0][1] == self.board[0][2]== player:
      pygame.draw.line(screen, COLOR , (0, HEIGHT_P / 2) , (WIDTH, HEIGHT_P/ 2) , width = 5)
      return 1

    if self.board[1][0] == self.board[1][1] == self.board[1][2] == player:
      pygame.draw.line(screen, COLOR , (0, HEIGHT_P / 2 + HEIGHT_P) , (WIDTH, HEIGHT_P/ 2 + HEIGHT_P) , width = 5)
      return 2
    
    if self.board[2][0] == self.board[2][1] == self.board[2][2] == player:
      pygame.draw.line(screen, COLOR , (0, HEIGHT_P / 2 + 2*HEIGHT_P) , (WIDTH, HEIGHT_P/ 2 + 2*HEIGHT_P) , width = 5)
      return 3 
    
    if self.board[0][0] == self.board[1][0] == self.board[2][0] == player:
      pygame.draw.line(screen, COLOR , (WIDTH_P/2, 0) , (WIDTH_P/2, HEIGHT) , width = 5)
      return 4
    
    if self.board[0][1] == self.board[1][1] == self.board[2][1] == player:
      pygame.draw.line(screen, COLOR , (WIDTH_P/2 + WIDTH_P, 0) , (WIDTH_P / 2 + WIDTH_P, HEIGHT) , width = 5)
      return 5 
    if self.board[0][2] == self.board[1][2] == self.board[2][2] == player:
      pygame.draw.line(screen, COLOR , (WIDTH_P/2 + 2*WIDTH_P, 0) , (WIDTH_P / 2 + 2*WIDTH_P, HEIGHT) , width = 5)
      return 6 
    if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
      pygame.draw.line(screen, COLOR , (0,0), (SIZE), width=5 )
      return 7 
    if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
      pygame.draw.line(screen, COLOR , (WIDTH,0), (0, HEIGHT),width=5 )
      return 8   
    
    return None
    
      
# ACTUAL PLAYER 
# 1 -> O
# -1 -> X


class Game:
  def __init__(self):
    self.actual_player = random.choice([-1,1])
    self.board = Board()
    self.next_turn()
    
    
    
  
  def draw_lines(self):

  #draw to vertical line
      pygame.draw.line(screen, COLOR_LINE , ( WIDTH_P , 0 ) , (WIDTH_P, HEIGHT), ANCH)
      pygame.draw.line(screen, COLOR_LINE , (WIDTH_P*2 , 0), (WIDTH_P*2, HEIGHT),ANCH)

  #draw two horitzontal lines

      pygame.draw.line(screen, COLOR_LINE , ( 0 , HEIGHT_P ) , (WIDTH, HEIGHT_P), ANCH)
      pygame.draw.line(screen, COLOR_LINE , (0 , HEIGHT_P*2), (WIDTH, HEIGHT_P*2),ANCH)

  


  def next_turn(self):
    self.actual_player = self.actual_player * -1
     # always it returuns the other number
  
  def to_see_icon(self):
    if self.actual_player == 1:
      return "O"
    else:
      return "X"

class IA:
  def __init__(self,board):
    self.board = board

    pass
def main():
  game = Game()
  board = game.board
  game.draw_lines()

  run = True
  while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          position = event.pos
          row = int(position[1] // HEIGHT_P)
          col = int (position[0] // WIDTH_P)
          board.mark_change(row,col,game.actual_player)
          print_board(board.board)
          
          #if win a player 
          if board.check_win(game.actual_player) != None:
            #do_changes_json(game.actual_player, game.actual_player * -1)
            
            text_surface = my_font.render(f'{game.to_see_icon()}', False, board.color_player(game.actual_player))
            screen.blit(text_surface, (WIDTH/2 ,HEIGHT/2))
            text = my_font.render(" has win ! ", False , BLACK )
            screen.blit(text, (WIDTH/2 -100,HEIGHT/2 + 60))
            
          #if tie
          if board.check_win(game.actual_player) == None and board.search_empty() == 0:
            #do_changes_json(game.actual_player,game.actual_player*-1,True)
            text_surface = my_font.render('tie', False, (0, 0, 0))
            screen.blit(text_surface, (WIDTH/2 -100,HEIGHT/2))
          
          game.next_turn() 
    pygame.display.update()
  pygame.quit()
           
            
if __name__ == "__main__":
    main()


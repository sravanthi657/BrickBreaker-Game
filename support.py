import board
import objects
import format
import random
import Bricks
from colorama import Fore, Back, Style
import time
import os
obj_board=board.Board(format.game_height,format.game_width)
obj_board.board_creation()
start_at=format.game_height-len(format.paddle_body)
obj_paddle=objects.Paddle(format.game_height-10,100,format.paddle_body)
ballrand=random.randrange(100,108)
obj_ball=objects.Ball(format.game_height-11,ballrand,format.ball)   
obj_bricks=Bricks.Bricks(20,40) 
obj_bricks.create_bricks_layout()
def display_info():
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX+Style.BRIGHT+("Basic Brick Breaker").center(124),Style.RESET_ALL, end='\n')
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT + ("SCORE: " + str(obj_ball.count_bricks()*10) + "   |  LIVES: " + str(obj_ball.get_lives()) + "   |  TIME: " +str(format.play_time)).center(124),Style.RESET_ALL, end='\n')
def check_colors():
    k=0
    while k<len(format.bricks_layout):
        if(format.bricks_layout[k].getstrength()>0 and k%3==0 and ((round(time.time()) -round(format.color_change))==1) and format.bricks_layout[k].get_hit_once()==0 ):
            format.bricks_layout[k].setstrength(random.randrange(1,4))
            # os.system('aplay -q ./Sounds/unexpected.wav&')
            format.color_change=time.time()
        if(format.bricks_layout[k].getstrength()==1):
            format.bricks_layout[k].setcolor(Back.RED)
        if(format.bricks_layout[k].getstrength()==2):
            format.bricks_layout[k].setcolor(Back.YELLOW)
        if(format.bricks_layout[k].getstrength()==3):
            format.bricks_layout[k].setcolor(Back.GREEN)
        k+=1
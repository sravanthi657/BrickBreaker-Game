import support
import format
import input
import os
import time
import Bricks
from colorama import Fore, Back, Style
os.system('clear')
support.obj_paddle.obtain()
support.obj_ball.obtain()
support.obj_bricks.print_bricks_layout()
support.display_info()
support.obj_board.board_printing()
format.prev_time=time.time()
format.game_stime=time.time()
format.ball_time=format.prev_time
format.color_change=format.prev_time
i=0
while True:
    format.left_time = format.game_time - (round(time.time()) - round(format.game_stime))
    format.play_time = round(time.time())- round(format.game_stime)
    if(format.left_time == 0 or support.obj_ball.lives <= 0):
        os.system('clear')
        if(format.left_time==0):       
            print(Fore.MAGENTA+Style.BRIGHT+"Time is up! ".center(199)+Style.RESET_ALL)
            print(Fore.WHITE+Style.BRIGHT+"Scored : ".center(199)+Style.RESET_ALL, Fore.MAGENTA+Style.BRIGHT+str(support.obj_ball.count_bricks()*10).center(199)+Style.RESET_ALL)
            os.system('aplay -q ./Sounds/unexpected.wav&')
        if(support.obj_ball.lives <= 0):
            print(Fore.WHITE+Style.BRIGHT+"Scored : ".center(199)+Style.RESET_ALL, Fore.MAGENTA+Style.BRIGHT+str(support.obj_ball.count_bricks()*10).center(199)+Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"and LIVES OVER :(".center(199)+Style.RESET_ALL)
            os.system('aplay -q ./Sounds/finished.wav&')
       
        quit()
    input.move_paddle()
    if(support.obj_ball.count_bricks()==6):
        support.obj_bricks=Bricks.Bricks(20,10)
        support.obj_bricks.create_bricks_layout()
    support.check_colors()
    support.obj_bricks.print_bricks_layout()   
    if time.time() - format.ball_time > support.obj_board.get_ballspeed() and format.move_paddle!=0 and format.move_paddle==1  : 
        support.obj_ball.move_ball()
        format.ball_time=time.time() 
    os.system('clear')
    support.display_info()
    support.obj_board.board_printing()
    i+=1
    

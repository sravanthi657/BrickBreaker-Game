"""Defining input class."""
import sys
import termios
import tty
import signal
import support
import format
import os
from colorama import Fore,Style,Back
class Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass

def move_paddle():
    def alarmHandler(signum, frame):
        """Handling timeouts."""
        raise AlarmException


    def user_input(timeout=0.1):
        """Taking input from user."""
        signal.signal(signal.SIGALRM, alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = Get()()
            signal.alarm(0)
           # print(text)
            return text
        except AlarmException:
            pass

        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None
    pressed=user_input()
    char = pressed
    if(char == 'd'):
        if(support.obj_paddle.y_at()+3 < format.game_width-2-len(format.paddle_body[0])+3):
            os.system('aplay -q ./Sounds/ball_paddle.wav&')
            #print("yes")
            if(format.move_paddle==0):
                support.obj_ball.clear()
                support.obj_ball.move_y(3)
                support.obj_ball.obtain()

            support.obj_paddle.clear()
            support.obj_paddle.move_y(3)
            support.obj_paddle.obtain()
        else:
            support.obj_paddle.move_y(0)
    elif char == 'q':
        os.system('aplay -q ./Sounds/unexpected.wav&')
        os.system('tput reset')
        print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"Pressed q?! Don't Quit!".center(199)+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"Scored: ".center(199)+Style.RESET_ALL,Fore.LIGHTBLUE_EX +Style.BRIGHT+str(support.obj_ball.count_bricks()*10).center(199)+Style.RESET_ALL)
        quit()
    elif(char == 'a'):
        if(support.obj_paddle.y_at()-3 >0):
            os.system('aplay -q ./Sounds/ball_paddle.wav&')
            if(format.move_paddle==0):
                support.obj_ball.clear()
                support.obj_ball.move_y(-3)
                support.obj_ball.obtain()
            support.obj_paddle.clear()
            support.obj_paddle.move_y(-3)
            support.obj_paddle.obtain()
        else:
            support.obj_paddle.move_y(0)
    elif(char==' '):
        format.move_paddle=1
        os.system('aplay -q ./Sounds/ball_released.wav&')

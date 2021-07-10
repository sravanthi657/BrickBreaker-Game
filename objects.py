import support
import format
import time
import os
import math 
import random
from colorama import Fore, Back, Style
class Demop:
    def __init__(self,x,y,shape):
        self._x = x
        self._y = y
        self._body=shape
    def x_at(self):
        return self._x
    def y_at(self):
        return self._y
    def setx(self,x):
        self._x=x
    def sety(self,y):
        self._y=y
    def obtain(self):
        shape_width=len(self._body[0])
        shape_height=len(self._body)
        for i in range(self._x,self._x+shape_height):
            for j in range(self._y,self._y+shape_width):
                if(self._body==format.paddle_body):
                    support.obj_board.grid[i][j]=Back.BLACK+self._body[i-self._x][j-self._y]+Style.RESET_ALL
                else:
                    support.obj_board.grid[i][j]=self._body[i-self._x][j-self._y]
                #print(self._body[i-self._x][j-self._y])
    def clear(self):
        shape_width=len(self._body[0])
        shape_height=len(self._body)
        for i in range(self._x,self._x+shape_height):
            for j in range(self._y,self._y+shape_width):
                support.obj_board.grid[i][j]=" "
    def move_x(self,x):
        self._x+=x
    def move_y(self,y):
        self._y+=y

class Paddle(Demop):
    def __init__(self,x,y,shape):
        Demop.__init__(self,x,y,shape)
        self._centerp=math.floor(len(self._body[0])/2)
    def get_center_in_board(self):
        return self.y_at()+self._centerp
    def get_center(self):
        return self._centerp

class Ball(Demop):
    def __init__(self,x,y,shape):
        Demop.__init__(self,x,y,shape)
        self.score = 0
        self.__xspeed = 1
        self.__yspeed = 1
        self.lives = 7
        self._bricks=0
        self._collided_paddle=0
    def bricks_plus(self):
        self._bricks += 1
    def count_bricks(self):
        return self._bricks
    def dec_lives(self):
        self.lives-=1
    def get_score(self):
        return self.score
    def get_lives(self):
        return self.lives
    def get_xspeed(self):
        return self.__xspeed
    def get_yspeed(self):
        return self.__yspeed
    def set_xspeed(self,c):
        self.__xspeed=c
    def set_yspeed(self,c):
        self.__yspeed=c
    def get_pos(self):
        return self.y_at()-support.obj_paddle.get_center_in_board()


    def move_ball(self):
        if(self.x_at()+1 <=support.obj_paddle.x_at()):
            if(self.x_at()==support.obj_paddle.x_at()-1):
                if( (self.y_at()>=support.obj_paddle.y_at()) and (self.y_at()<=(len(support.obj_paddle._body[0]))+support.obj_paddle.y_at() ) ): 
                    os.system('aplay -q ./Sounds/paddle_hit.wav&')
                    how_far=self.get_pos()
                    self.set_yspeed(how_far)
                    self.set_xspeed(-1)
                if(self.y_at()>=120):
                    os.system('aplay -q ./Sounds/hardest_hit.wav&')
                    self.set_yspeed(-self.get_yspeed())
                if(self.y_at()<=4):
                    os.system('aplay -q ./Sounds/hardest_hit.wav&')
                    self.set_yspeed(abs(self.get_yspeed()))
            else:
                if(self.x_at()<=1):
                    os.system('aplay -q ./Sounds/hardest_hit.wav&')
                    self.set_xspeed(1)
                if(self.y_at()>=120):
                    os.system('aplay -q ./Sounds/hardest_hit.wav&')
                    self.set_yspeed(-self.get_yspeed())
                if(self.y_at()<=4):
                    os.system('aplay -q ./Sounds/hardest_hit.wav&')
                    self.set_yspeed(abs(self.get_yspeed()))
                else:
                    k=0
                    while k<len(format.bricks_layout):
                        if format.bricks_layout[k].x_at()==self.x_at()+1:
                            if format.bricks_layout[k].y_at()<=self.y_at() and format.bricks_layout[k].y_at()+len(format.bricks[0])>=self.y_at():
                                if format.bricks_layout[k].getcolor()==Back.CYAN and format.bricks_layout[k].getstrength()!=0 :
                                    format.bricks_layout[k].setstrength(0)
                                    self.bricks_plus()
                                    self.set_xspeed(-1)
                                    if(k+1<len(format.bricks_layout)and format.bricks_layout[k+1].getstrength()!=0):
                                        format.bricks_layout[k+1].setstrength(0)
                                        self.bricks_plus()
                                    if(k-1>=0 and format.bricks_layout[k-1].getstrength()!=0):                                            
                                        format.bricks_layout[k-1].setstrength(0)
                                        self.bricks_plus()
                                    if(k+10<len(format.bricks_layout)and format.bricks_layout[k+10].getstrength()!=0):
                                        format.bricks_layout[k+10].setstrength(0)
                                        self.bricks_plus()
                                    if(k-10>=0 and format.bricks_layout[k-10].getstrength()!=0):
                                        format.bricks_layout[k-10].setstrength(0)
                                        self.bricks_plus()
                                if(format.bricks_layout[k].getstrength()>1):
                                    format.laser_time=format.prev_time
                                    os.system('aplay -q ./Sounds/hard_hit.wav&')
                                else:
                                    if(format.bricks_layout[k].getstrength()==1):
                                        os.system('aplay -q ./Sounds/brick_ball.wav&')
                                        self.bricks_plus()
                                if(format.bricks_layout[k].getstrength()>0):
                                    format.bricks_layout[k].decstrength()
                                    format.bricks_layout[k].hit_once=1
                                    self.set_xspeed(-1)
                        if format.bricks_layout[k].x_at()==self.x_at()-2: 
                            if format.bricks_layout[k].y_at()<=self.y_at() and format.bricks_layout[k].y_at()+len(format.bricks[0])>=self.y_at():
                                if format.bricks_layout[k].getcolor()==Back.CYAN and format.bricks_layout[k].getstrength()!=0:
                                    format.bricks_layout[k].setstrength(0)
                                    self.bricks_plus()
                                    self.set_xspeed(1)
                                    if(k+1<len(format.bricks_layout) and format.bricks_layout[k+1].getstrength()!=0):
                                        format.bricks_layout[k+1].setstrength(0)
                                        self.bricks_plus()
                                    if(k-1>=0 and format.bricks_layout[k-1].getstrength()!=0):                                            
                                        format.bricks_layout[k-1].setstrength(0)
                                        self.bricks_plus()
                                    if(k+10<len(format.bricks_layout)and format.bricks_layout[k+10].getstrength()!=0):
                                        format.bricks_layout[k+10].setstrength(0)
                                        self.bricks_plus()
                                    if(k-10>=0 and format.bricks_layout[k-10].getstrength()!=0):
                                        format.bricks_layout[k-10].setstrength(0)
                                        self.bricks_plus()
                                if(format.bricks_layout[k].getstrength()>1):
                                    os.system('aplay -q ./Sounds/hard_hit.wav&')
                                else:
                                    if(format.bricks_layout[k].getstrength()==1):
                                        os.system('aplay -q ./Sounds/brick_ball.wav&')
                                        self.bricks_plus()
                                if(format.bricks_layout[k].getstrength()>0):
                                    format.bricks_layout[k].decstrength()
                                    format.bricks_layout[k].hit_once=1
                                    self.set_xspeed(1)
                        k+=1
        else:
            if(self.x_at()>=37):
                os.system('aplay -q ./Sounds/lost_life.wav&')
                self.dec_lives()
                self.clear()
                self.setx(support.obj_paddle.x_at()-1)
                self.sety(random.randrange(support.obj_paddle.y_at(),support.obj_paddle.y_at()+len(format.paddle_body[0])))
                format.move_paddle=0 #you can hold ,move and release the ball by pressing " "
                self.obtain()
                return
        self.clear()
        self.move_x(self.__xspeed)
        self.move_y(self.__yspeed)
        self.obtain()


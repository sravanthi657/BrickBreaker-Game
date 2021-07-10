import format
import support
from colorama import Fore, Back, Style
import os  
import time
class Bricks:
    def __init__(self,x,y):
        self._x=x
        self._y=y
        self.stx=0
        self.sty=0
        self.Weakest=[]
        self.Weak=[]
        self.Strong=[]
        self.unbreakable=[]
        self.blayout_ht=len(format.bricks_strength)
        self.blayout_wd=len(format.bricks_strength[0])
        self.b_ht=len(format.bricks)
        self.b_wd=len(format.bricks[0])
        self.strength=1
        self.contain_powerup=0
        self.hit_once=0
    def x_at(self):
        return self.x
    def y_at(self):
        return self.y
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def setcolor(self,x):
        self.color=x
    def setstrength(self,y):
        self.strength=y
    def getcolor(self):
        return self.color
    def getstrength(self):
        return self.strength
    def decstrength(self):
        self.strength-=1
    def get_hit_once(self):
        return self.hit_once
    def get_powerup_status(self):
        return self.contain_powerup
    def set_powerup_status(self,c):
        self.contain_powerup=c
    def set_stxy(self,stx,sty):
    	self.stx=stx
    	self.sty=sty
    def create_bricks_layout(self):
        for i in range (self.blayout_ht):
            for j in range(self.blayout_wd):
                if(format.bricks_strength[i][j]==1 or format.bricks_strength[i][j]==7):
                    format.bricks_layout.append(Red_Bricks(i*self.b_ht,j*self.b_wd))
                if(format.bricks_strength[i][j]==2 ):
                    format.bricks_layout.append(Yellow_Bricks(i*self.b_ht,j*self.b_wd))
                if(format.bricks_strength[i][j]==3):
                    format.bricks_layout.append(Green_Bricks(i*self.b_ht,j*self.b_wd))
                if(format.bricks_strength[i][j]==2000):
                    format.bricks_layout.append(White_Bricks(i*self.b_ht,j*self.b_wd))
                if(format.bricks_strength[i][j]==1000000):
                    format.bricks_layout.append(Cyan_Bricks(i*self.b_ht,j*self.b_wd))
    def print_bricks_layout(self):
        k=0
        while k<len(format.bricks_layout):
            for i in range(1):
                for  j in range(self.b_wd):
                    # support.obj_board.grid[format.game_height-10][100]=format.bricks_layout[k].getstrength()
                    if(format.bricks_layout[k].getstrength()<=0):
                        support.obj_board.grid[format.bricks_layout[k].x_at()][format.bricks_layout[k].y_at()+j]=format.bricks[0][j]+Style.RESET_ALL
                        support.obj_board.grid[format.bricks_layout[k].x_at()+1][format.bricks_layout[k].y_at()+j]=format.bricks[1][j]+Style.RESET_ALL
                    else:
                        support.obj_board.grid[format.bricks_layout[k].x_at()][format.bricks_layout[k].y_at()+j]=format.bricks_layout[k].getcolor()+format.bricks[0][j]+Style.RESET_ALL
                        support.obj_board.grid[format.bricks_layout[k].x_at()+1][format.bricks_layout[k].y_at()+j]=format.bricks_layout[k].getcolor()+format.bricks[1][j]+Style.RESET_ALL
            k+=1

class Red_Bricks(Bricks):
    def __init__(self,x,y):
        Bricks.__init__(self,x,y)
        self.setx(12+x+self.stx)
        self.sety(30+y+self.sty)
        self.setcolor(Back.RED)
        self.setstrength(1)

class Green_Bricks(Bricks):
    def __init__(self,x,y):
        Bricks.__init__(self,x,y)
        self.setx(12+x+self.stx)
        self.sety(30+y+self.sty)
        self.setcolor(Back.GREEN)
        self.setstrength(3)
        self.set_powerup_status(1)
class Yellow_Bricks(Bricks):
    def __init__(self,x,y):
        Bricks.__init__(self,x,y)
        self.setx(12+x+self.stx)
        self.sety(30+y+self.sty)
        self.setcolor(Back.YELLOW)
        self.setstrength(2)
        self.set_powerup_status(1)
class White_Bricks(Bricks):
    def __init__(self,x,y):
        Bricks.__init__(self,x,y)
        self.setx(12+x+self.stx)
        self.sety(30+y+self.sty)
        self.setcolor(Back.WHITE)
        self.setstrength(2000)
class Cyan_Bricks(Bricks):
    def __init__(self,x,y):
        Bricks.__init__(self,x,y)
        self.setx(12+x+self.sty)
        self.sety(30+y+self.sty)
        self.setcolor(Back.CYAN)
        self.setstrength(2000)
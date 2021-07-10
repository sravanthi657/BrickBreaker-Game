from colorama import Fore,Style,Back
class Board:
    def __init__(self,Row,Column):
        self.__Row=Row
        self.__Column=Column
        self.grid=[]
        self.__layout=Back.BLUE+" "+Style.RESET_ALL 
        self.__vlayout=Back.BLUE+" "+Style.RESET_ALL 
        self._is_speedboard=0
        self._boardspeed=0.1
        self._ballspeed=0.2
        self.powerupspeed=0.3
    def set_ballspeed(self,x):
        self._ballspeed=x
    def get_ballspeed(self):
        return self._ballspeed
    def get_laserspeed(self):
        return self.powerupspeed
    def board_creation(self):
        for r in range(self.__Row):
            if(r==0):
                self.temp=[self.__layout for c in range(self.__Column)]
            elif(r==self.__Row-1):
                self.temp=[self.__layout for c in range(self.__Column)]
            else:
                self.temp= [" " for c in range(self.__Column)]
            self.grid.append(self.temp)
 
    def board_printing(self):
        for r in range(self.__Row):
            for c in range (self.__Column):
                if(c==0 or c==self.__Column-1):
                    self.grid[r][c]=self.__vlayout
                print(self.grid[r][c],end='')
            print()



## To play:
* Execute " python3 main.py " in your terminal and maximise the screen.

# Basic Brick Breaker
* Game time -100 sec
* control keys:
* a- left
* d- right
* ' ' (space) - releases the ball from paddle

##Classes created
### Board :
**location:** board.py
A board with 50*200 is created
### Demop :
**location:** objects.py
A model class for every objects used in this game are inherted from this
## Inheritance
Demop class is created and all objects like 
> Ball
> Paddle
> Bricks
  are inherited from this class
Demop shares attributes with these classes .As Demop is parent class and Ball, Paddle, Bricks are child classes
## Polymorphism
On using the functions created by parent class we define polymorphism
> ***example***
  def clear(self):
        shape_width=len(self._body[0])
        shape_height=len(self._body)
        for i in range(self._x,self._x+shape_height):
            for j in range(self._y,self._y+shape_width):
                support.obj_board.grid[i][j]=" "

## Encapsulation
It is implemntation of abstraction that is hiding the data for outsider(clients).Here every class and object wrapped data .
## Abstraction
Just defining the name for encapsulated/hidden functions or data
> ***example***
  def set_xspeed(self,c,x):
    self.__xspeed=x*c
     and many other are used 


*I've updated the game with sound effects and implemented Rainbow brick feature with mentioned measures

**Rainbow Brick:**
> It is implemented on considereing hit_once variable
  Uptil a hit the brick randomly changes the color and hardness carry with that per each frame.
**Sound effects:**
* I've used *os.system('aplay -q ./Sounds/music.wav&')*
* Sounds which are used in the game were placed in folder named Sounds
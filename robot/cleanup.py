from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while True:
  for n in range(-1,2,2):
  while look() == 'fruit' or left_side() == 'fruit' or right_side() == 'fruit':
    move()
  turn(-)
  move()
  turn(-1)
  
 
  


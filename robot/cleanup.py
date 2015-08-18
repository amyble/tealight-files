from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while touch() == 'fruit' or left_side() == 'fruit' or right_side() == 'fruit':
    move()
 
  


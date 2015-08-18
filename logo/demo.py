from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,100):
  move(i)
  turn(20)
  color(colors[i%])
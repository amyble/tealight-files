from tealight.logo import move, turn

def triangle(side):
  for i in range(0,3):
    move(side)
    turn(120)
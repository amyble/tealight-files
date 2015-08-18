from tealight.logo import move, turn

def triangle(size):
  angle = 360.0 / 3
  for i in range(0, 3):
    move(size)
    turn(angle)
    
triangle(100000)
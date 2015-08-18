from tealight.logo import move, turn

def triangle(side):
  for i in range(0,3):
    move(side)
    turn(120)

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 3.0, detail - 1)
    turn(-60)
    segment(scale / 3.0, detail - 1)
    turn(120)
    segment(scale / 3.0, detail - 1)
    turn(-60)
    segment(scale / 3.0, detail - 1)
    

turn(90)
move(-300)
segment(600,1)
move(-300)
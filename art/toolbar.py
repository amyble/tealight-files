from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)
from tealight.art import (screen_height, screen_width)

def start():
  tools = ["line","bold","circle","bird","stars","italics","triangle","hearts","eraser"]

  text (screen_width - 300, 10, "Toolbar:")
  rectangle(screen_width - 300,35,25,25)
  line(screen_width - 286, 40, screen_width - 286, 52)
  rectangle(screen_width - 275,35,25,25)
  box (screen_width - 264, 37, 5, 20)
  rectangle(screen_width - 250,35,25,25)
  spot (screen_width - 238, 47, 8)
  rectangle(screen_width - 225,35,25,25)
  text(screen_width - 219, 38, "B")
  rectangle(screen_width - 200,35,25,25)
  text(screen_width - 200, 38, "*")
  rectangle(screen_width - 175,35,25,25)
  text(436, 38, "/")
  rectangle(screen_width - 150,35,25,25)
  text(457, 38, "T")
  rectangle(screen_width - 125,35,25,25) 
  text(480, 38, "H")
  rectangle(screen_width - 100,35,25,25) 
  text(505, 38, "X")
start()
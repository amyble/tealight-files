from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)
from tealight.art import (screen_height, screen_width)

def start():
  tools = ["line","bold","circle","bird","stars","italics","triangle","hearts","eraser"]

  text (300, 10, "Toolbar:")
  rectangle(screen_width - 285,35,25,25)
  line(312, 40, 312, 52)
  rectangle(325,35,25,25)
  box (335, 37, 5, 20)
  rectangle(350,35,25,25)
  spot (363, 47, 8)
  rectangle(375,35,25,25)
  text(383, 38, "B")
  rectangle(400,35,25,25)
  text(410, 38, "*")
  rectangle(425,35,25,25)
  text(436, 38, "/")
  rectangle(450,35,25,25)
  text(457, 38, "T")
  rectangle(475,35,25,25) 
  text(480, 38, "H")
  rectangle(500,35,25,25) 
  text(505, 38, "X")
start()
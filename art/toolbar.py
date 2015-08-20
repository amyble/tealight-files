from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)


def start():
  tools = ["line","bold","circle","bird","stars","italics","triangle","hearts","eraser"]

  text (300, 10, "Toolbar:")
  rectangle(300,35,25,25)
  line(312, 40, 312, 52)
  rectangle(325,35,25,25)
  box (335, 37, 5, 20)
  rectangle(350,35,25,25)
  spot (363, 47, 8)
  rectangle(375,35,25,25)
  text(383, 40, "B")
  rectangle(400,35,25,25)
  text(410, 40, "*")
  rectangle(425,35,25,25)
  text(436, 40, "/")
  rectangle(450,35,25,25)
  text(457, 40, "T")
  rectangle(475,35,25,25) 
  text(480, 40, "H")
  rectangle(500,35,25,25) 
  text(505, 40, "X")
start()
from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)


def start():
  tools = ["line","bold","circle","bird","stars","italics","triangle","hearts","eraser"]

  text (300, 25, "Toolbar:")
  rectangle(300,50,25,25)
  line(312, 70, 312, 52)
  rectangle(325,50,25,25)
  box (335, 52, 5, 20)
  rectangle(350,50,25,25)
  spot (363, 62, 8)
  rectangle(375,50,25,25)
  text(383, 55, "B")
  rectangle(400,50,25,25)
  text(410, 55, "*")
  rectangle(425,50,25,25)
  text(436, 55, "/")
  rectangle(450,50,25,25)
  text(490, 55, "T")
  rectangle(475,50,25,25) 
  text(520, 55, "H")
  rectangle(500,50,25,25) 
  text(550, 55, "X")
start()
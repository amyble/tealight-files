from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)
def start():
  tools = ["line","bold","circle","bird","stars","italics","triangle","hearts","eraser"]

  text (300, 25, "Toolbar:")
  rectangle(300,50,25,25)
  line(312, 70, 312, 52)
  rectangle(330,50,25,25)
  box (342, 52, 5, 22)
  rectangle(360,50,25,25)
  spot (375, 66, 10)
  rectangle(390,50,25,25)
  text(400, 55, "B")
  rectangle(420,50,25,25)
  text(430, 55, "*")
  rectangle(450,50,25,25)
  text(465, 55, "/")
  rectangle(480,50,25,25)
  text(490, 55, "T")
  rectangle(510,50,25,25) 
  text(520, 55, "H")
  rectangle(540,50,25,25) 
  text(550, 55, "X")
start()
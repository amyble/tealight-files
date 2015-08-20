from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)
def finishButtons():
  color("green")
  rectangle((screen_width / 2) - 75, screen_height / 2, 150,30)
  text((screen_width / 2) - 32.5, ((screen_height / 2) + 5), "Correct")

  color("red")
  rectangle((screen_width / 2) + 95, screen_height / 2, 150,30)
  text((screen_width / 2) + 132.5, ((screen_height / 2) + 5), "Wrong")
  
def stopButton():  
    color("red")
    rectangle((screen_width - 160), screen_height - 40, 150,30)
    text(screen_width - 85, ((screen_height - 35), "STOP")
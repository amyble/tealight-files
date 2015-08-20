from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)
def finishButtons():
  color("green")
  rectangle((screen_width / 2) - 75, screen_height / 2, 150,30)
  text((screen_width / 2) - 35, ((screen_height / 2) + 5), "P1 Correct")

  color("red")
  rectangle((screen_width / 2) + 95, screen_height / 2, 150,30)
  text((screen_width / 2) + 132.5, ((screen_height / 2) + 5), "P1 Wrong")
  
def stopButton():
    global stopMinX, stopMaxX, stopMinY, stopMaxY  
    color("red")
    rectangle((screen_width - 180), screen_height - 40, 150,30)
    text(screen_width - 85, screen_height - 35, "STOP")
    stopMinX = screen_width - 180
    stopMaxX = screen_width - 30
    stopMinY = screen_height - 40
    stopMaxY = screen_height - 10
    
stopButton()
finishButtons()
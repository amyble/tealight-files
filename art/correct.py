from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)
def finishButtons():
  color("green")
  rectangle((screen_width / 2) - 75, screen_height / 2, 150,30)
  text((screen_width / 2) - 45, ((screen_height / 2) + 5), "P2 Correct")
  rectangle((screen_width / 2) - 75, ((screen_height / 2) + 40), 150,30)
  text((screen_width / 2) - 45, ((screen_height / 2) + 45), "P3 Correct")
  
  color("red")
  rectangle((screen_width / 2) + 95, screen_height / 2, 150,30)
  text((screen_width / 2) + 125, ((screen_height / 2) + 5), "P2 Wrong")
  rectangle((screen_width / 2) + 95, ((screen_height / 2) + 40), 150,30)
  text((screen_width / 2) + 125, ((screen_height / 2) + 45), "P3 Wrong")
  
  p2cMinX = ((screen_width / 2) - 75)
  p2cMaxX = ((screen_width / 2) + 75)
  p2cMinX = ((screen_width / 2) - 75)
  p2cMaxX = ((screen_width / 2) + 75)
  p2wMinY = screen_height / 2
  p2wMaxY = ((screen_height / 2) + 30)
  p3cMinX = ((screen_width / 2) + 95)
  p3cMaxX = ((screen_width / 2) + 245) 
  p3wMinY = ((screen_width / 2) + 40)
  
  
def stopButton():
    global stopMinX, stopMaxX, stopMinY, stopMaxY  
    color("red")
    rectangle((screen_width - 180), screen_height - 40, 150,30)
    text(screen_width - 85, screen_height - 35, "STOP")
    stopMinX = screen_width - 180
    stopMaxX = screen_width - 30
    stopMinY = screen_height - 40
    stopMaxY = screen_height - 10
    
finishButtons()
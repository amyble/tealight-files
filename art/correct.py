from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)
global stopMinX, stopMaxX, stopMinY, stopMaxY

from tealight.art import (screen_width, screen_height)
def finishButtons():
  global p2cMinX,p2cMaxX,p2cMinY,p2cMaxY, p2wMinX, p2wMaxX, p2wMinY, p2wMaxY, p3cMinX, p3cMaxX, p3cMinY, p3cMaxY, p3wMinX, p3wMaxX, p3wMinY, p3wMaxY
  color("green")
  #P2 Correct
  rectangle((screen_width / 2) - 75, screen_height / 2, 150,30)
  text((screen_width / 2) - 45, ((screen_height / 2) + 5), "P2 Correct")
  #P3 Correct
  rectangle((screen_width / 2) - 75, ((screen_height / 2) + 40), 150,30)
  text((screen_width / 2) - 45, ((screen_height / 2) + 45), "P3 Correct")
  
  color("red")
  #P2 Wrong
  rectangle((screen_width / 2) + 95, screen_height / 2, 150,30)
  text((screen_width / 2) + 125, ((screen_height / 2) + 5), "P2 Wrong")
  #P3 Wrong
  rectangle((screen_width / 2) + 95, ((screen_height / 2) + 40), 150,30)
  text((screen_width / 2) + 125, ((screen_height / 2) + 45), "P3 Wrong")
  
  p2cMinX = ((screen_width / 2) - 75)
  p2cMaxX = ((screen_width / 2) + 75)
  p2cMinY = (screen_height / 2)
  p2cMaxY = (screen_height / 2) + 30
  
  p2wMinX = ((screen_width / 2) + 95)
  p2wMaxX = ((screen_width / 2) + 245)
  p2wMinY = (screen_height / 2)
  p2wMaxY = ((screen_height / 2) + 30)
  
  p3cMinX = ((screen_width / 2) - 75)
  p3cMaxX = ((screen_width / 2) + 175) 
  p3cMinY = ((screen_height / 2) + 40)
  p3cMaxY = ((screen_width / 2) + 70)
  
  p3wMinX = ((screen_width / 2) + 95)
  p3wMaxX = ((screen_width / 2) + 245) 
  p3wMinY = ((screen_width / 2) + 40)
  p3wMaxY = ((screen_width / 2) + 70)
  
finishButtons()  
  
 
def stopButton():
    global stopMinX, stopMaxX, stopMinY, stopMaxY  
    color("red")
    rectangle((screen_width - 180), screen_height - 40, 150,30)
    text(screen_width - 85, screen_height - 35, "STOP")
    stopMinX = screen_width - 180
    stopMaxX = screen_width - 30
    stopMinY = screen_height - 40
    stopMaxY = screen_height - 10

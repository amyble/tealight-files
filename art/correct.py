from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)
global stopMinX, stopMaxX, stopMinY, stopMaxY
from tealight.art import (screen_width, screen_height)

def stopButton():
    color("purple")
    rectangle((screen_width - 180), screen_height - 40, 150,30)
    text(screen_width - 85, screen_height - 35, "STOP")
    stopMinX = screen_width - 180
    stopMaxX = screen_width - 30
    stopMinY = screen_height - 40
    stopMaxY = screen_height - 10

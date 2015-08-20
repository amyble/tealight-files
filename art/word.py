from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)
from tealight.art import (screen_width, screen_height)
import random

rectangle(0, screen_height, 20, 5)  
a = ["Dog", "Cat", "Castle", "Voldemort", "Football", "Ice Cream", "Barack Obama", "Snowman"]
print(random.choice(a))
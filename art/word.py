from tealight.art import (color, line, spot, circle, box, rectangle, image, text, background)
from tealight.art import (screen_width, screen_height)
import random

rectangle(10, screen_height - 50, 150, 40)
text(15, screen_height - 50, "Receive word")
a = ["Dog", "Cat", "Castle", "Voldemort", "Barack Obama", "Snowman", "Aeroplane", "Apple"]
print(random.choice(a))
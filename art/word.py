from tealight.art import (font, color, line, spot, circle, box, rectangle, image, text, background)
from tealight.art import (screen_width, screen_height)
import random

rectangle(10, screen_height - 50, 130, 35)
text(15, screen_height - 45, "Play")

rectangle(150, screen_height - 50, 130, 35)
text(15, screen_height - 45, (random.choice(a)))

a = ["Dog", "Cat", "Castle", "Voldemort", "Barack Obama", "Snowman", "Aeroplane", "Apple"]
font("34px Verdana")
print(random.choice(a))

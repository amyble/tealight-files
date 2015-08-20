from tealight.art import (color, line, spot, rectangle, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)


rectangle((screen_width / 2) - 75, screen_height / 2, 150,30)
rectangle((screen_width / 2) + 95, screen_height / 2, 150,30)
text((screen_width / 2) - 75, screen_height / 2, "Correct")
text((screen_width / 2) + 95, screen_height / 2, "Wrong")
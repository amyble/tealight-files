from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 20
height = 10

for i in range(0,width,2):
  for j in range(0,height,2):
    if i % 4 == 0:
      image(x + j * 60, y + i * 60, "misc/YellowFlower.png")
      image(x + j * 60, y + i * 60, "misc/YellowFlower.png")
    else:
      image(x + j * 60, y + i * 60, "misc/Clover.png")
     

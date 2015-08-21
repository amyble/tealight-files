import random
from tealight.art import text
from tealight.art import screen_width, screen_height

def word():
  a = ["Dog", "Cat", "Castle", "Voldemort", "Barack Obama", "Snowman", "Aeroplane", "Apple", "Bible", "Chocolates", "Electricity"]
  text(screen_width / 2, screen_height / 2, random.choice(a))

word()
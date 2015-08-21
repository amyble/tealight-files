import random
from tealight.art import text
from tealight.art import screen_width, screen_height

def word():
  a = ["Dog", "Cat", "Castle", "Voldemort", "Barack Obama", "Snowman", "Aeroplane", "Apple", "Bible", "Chocolates", "Electricity"]
  text(random.choice(a))

import random
from tealight.art import text

def word():
  a = ["Dog", "Cat", "Castle", "Voldemort", "Barack Obama", "Snowman", "Aeroplane", "Apple", "Bible", "Chocolates", "Electricity"]
  text(random.choice(a))

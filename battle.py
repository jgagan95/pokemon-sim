from pokemon import *
from random import choice, randint

print("\n\n\n\n\nRival: Let's check out our pokemon\nCome on! I'll take you on")
print(f"Rival would like to battle. They sent out {rival_party[0]}")


# if (rival["Speed"] > your_party["Speed"]):
#   print("Hey") #placeholder
#   #this person gets priority to attack
# elif rival["Speed"] == your_party["Speed"]:
#   print("Do this") #placeholder
#   #choice deteremines who goes first
# else:
#   print("ney") #placeholder
#   #you go first

game_over = False

def attack():
  rival_attack = choice(rival["Moveset"])

  if rival_attack == "Scratch" or rival_attack == "Tackle":
    your_party["HP"] -= 3
    stat_handling()
  elif rival_attack == "Tail Whip":
    your_party["Defense"] -= 1
    stat_handling()
  else:
    your_party["Attack"] -= 1
    stat_handling()

  return rival_attack

def stat_handling():
  if (rival["Attack"] == 6 or your_party["Attack"] == 6) or (rival["Defense"] == 6 or your_party["Defense"] == 6):
    print("The attack failed!")

print(your_party)
for i in range(9):
  print(attack())
print(your_party)

#need to determine which side goes first, but not a coinflip
#calculating stat reducing with abilities

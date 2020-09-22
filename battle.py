from pokemon import *
from random import choice

print("\n\n\n\n\nRival: Let's check out our pokemon\nCome on! I'll take you on")
print(f"Rival would like to battle. They sent out {rival_party[0]}")

game_over = False

def rival_attack():
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
  if rival["Attack"] <= 7 or rival["Defense"] <= 7:
    print("The attack failed!")
  elif your_party["Defense"] <= 7 or your_party["Attack"] <= 7:
    print("The attack failed!")

def speed():
  if (rival["Speed"] > your_party["Speed"]):
    rival_attack()
  elif rival["Speed"] == your_party["Speed"]:
    random_first_attack
  else:
    my_attack()

def my_attack():
  my_attack = choice(your_party["Moveset"])

  if my_attack == "Scratch" or my_attack == "Tackle":
    rival["HP"] -= 3
    stat_handling()
  elif my_attack == "Tail Whip":
    rival["Defense"] -= 1
    stat_handling()
  else:
    rival["Attack"] -= 1
    stat_handling()

  return my_attack

random_first_attack = choice([rival_attack, my_attack])()

print(random_first_attack)

#need to get code onto pokemon.py then run the battle on this file

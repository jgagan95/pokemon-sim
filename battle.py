from pokemon import *

def game():
  while True:
    if rival["HP"] == 19 and your_party["HP"] == 19:
      my_attack()
      attack = rival_attack()
      print(f'\n\nYour rival used: {attack}')
      print(f'Your HP is: {your_party["HP"]}, Attack is: {your_party["Attack"]}, Defense is: {your_party["Defense"]}')
      print(f'Your Rival\'s HP is: {rival["HP"]}, Attack is: {rival["Attack"]}, Defense is: {rival["Defense"]}')
    else:
      if rival["HP"] <= 0:
        print("YOU WIN")
        break
      elif your_party["HP"] <= 0:
        print("YOU LOSE")
        break
      else:
        my_attack()
        attack = rival_attack()
        print(f'\n\nYour rival used: {attack}')
        print(f'Your HP is: {your_party["HP"]}, Attack is: {your_party["Attack"]}, Defense is: {your_party["Defense"]}')
        print(f'Your Rival\'s HP is: {rival["HP"]}, Attack is: {rival["Attack"]}, Defense is: {rival["Defense"]}')

game()

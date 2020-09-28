from random import randint, choice

pokemon_party = []
rival_party = []

pokemon_stats = {
    'HP': 19,
    'Attack': randint(10, 12),
    'Defense': randint(10, 12),
    'Speed': randint(10, 12)
}

#had to create another dictionary similar to pokemon stats to get randomness on stats
rival_stats = {
    'HP': 19,
    'Attack': randint(10, 12),
    'Defense': randint(10, 12),
    'Speed': randint(10, 12)
}

charmander_moves = ['Scratch', 'Growl']
squirtle_moves = ['Tackle', 'Tail Whip']
bulbasaur_moves = ['Tackle', 'Growl']

#welcome message
print("WELCOME TO BOOTLEG POKEMON")
print("\n\n\n\n\nHere are the three pokemon to select: Bulbasaur, Charmander, and Squirtle.")

while True:
    starter_pokemon = input("Select a pokemon from that list: ").lower()
    if starter_pokemon == "bulbasaur" or starter_pokemon == "charmander" or starter_pokemon == "squirtle":
        print(f"All right! You've chosen {starter_pokemon.capitalize()}!")
        pokemon_party.append(starter_pokemon)
        break
    else:
        print("\nPlease select from the choices given.")

def rival_starter():
  if starter_pokemon == "bulbasaur":
    rival_party.append("Charmander")
    rival_party.append(charmander_moves)
    pokemon_party.append(bulbasaur_moves)
  elif starter_pokemon == "squirtle":
    rival_party.append("Bulbasaur")
    rival_party.append(bulbasaur_moves)
    pokemon_party.append(squirtle_moves)
  else:
    rival_party.append("Squirtle")
    rival_party.append(squirtle_moves)
    pokemon_party.append(charmander_moves)

  return rival_party[0]

rival = {
  'Starter': rival_starter(),
  'Moveset': rival_party[1]
}

your_party = {
  'Starter': pokemon_party[0].capitalize(),
  'Moveset': pokemon_party[1]
}

your_party.update(pokemon_stats)
rival.update(rival_stats)

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

def my_attack():
  while True:
    my_attack = input(f'What attack would you like to use? {your_party["Moveset"][0]} or {your_party["Moveset"][1]}:  ').lower()
    if my_attack == "scratch" or my_attack == "tackle":
      rival["HP"] -= 3
      stat_handling()
      break
    elif my_attack == "tail whip":
      rival["Defense"] -= 1
      stat_handling()
      break
    elif my_attack == "growl":
      rival["Attack"] -= 1
      stat_handling()
      break
    else:
      print("Please select from the choices given.\n")

print("\n\n\nRival: Let's check out our pokemon...\n\nCome on! I'll take you on")
print(f"Rival would like to battle. They sent out {rival_party[0]}")

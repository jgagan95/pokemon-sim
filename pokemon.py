from random import randint
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
        print("\nPlease select from the choices given")

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

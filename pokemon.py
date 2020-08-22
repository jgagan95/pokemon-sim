from random import randint
#welcome message
print("WELCOME TO BOOTLEG POKEMON")

#select a pokmemon and save it to your party
pokemon_party = []
print("\n\n\n\n\nHere are the three pokemon to select: Bulbasaur, Charmander, and Squirtle.")

while True:
    starter_pokemon = input("Select a pokemon from that list: ").lower()
    if starter_pokemon == "bulbasaur" or starter_pokemon == "charmander" or starter_pokemon == "squirtle":
        print(f"All right! You've chosen {starter_pokemon.capitalize()}!")
        pokemon_party.append(starter_pokemon)
        break
    else:
        print("\nPlease select from the choices given")

#determine rival pokemon (opposite of what you select)
rival_party = []
if starter_pokemon == "bulbasaur":
    rival_party.append("Charmander")
elif starter_pokemon == "squirtle":
    rival_party.append("Bulbasaur")
else:
    rival_party.append("Squirtle")

print(f"\n\n\n\n\nMeanwhile, your opponent has chosen {rival_party[0]}!")

#small battle
#assign movesets and stats to pokemon based off of selection
pokemon_stats = {
    'HP': 19,
    'Attack': randint(10, 12),
    'Defense': randint(10, 12),
    'Speed': randint(10, 12)
}

charmander_moves = ['Scratch', 'Growl']

squirtle_moves = ['Tackle', 'Tail Whip']

bulbasaur_moves = ['Tackle', 'Growl']

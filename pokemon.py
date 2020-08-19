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
#small battle

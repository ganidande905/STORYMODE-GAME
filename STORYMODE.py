

# Act1
# These are the items given in the start
# These need to be maintained by the player for survival
level = 1
ruins = 100
water = 100
health = 300
weapon = "Sword"
crimson_tears = 4  # It gives you 200hp


def items():
    global crimson_tears
    weapons = ["Dagger", "Sword", "Axes", "Katana", "Bow"]
    healing = ["Crimson Tears"]
    spells = ["Fire spell", "water spell"]
    print("The list of items available with the merchant:")
    print("1.Weapons\n2.Healing\n3.Spells")
    i = int(input("Enter your option(1,2,3):"))

    if i == 1:
        for j in range(len(weapons)):
            print(f"{j + 1}.{weapons[j]}")
        weapon = input("Select your weapon(Dagger, Sword, Axes, Katana, Bow):")
        print(f"You new weapon is {weapon}")
        print("")
    elif i == 2:
        crimson_tears += 1
        print("Number of Crimson Tears increased.")
        print(f"Current number of Crimson Tears is {crimson_tears}")
        print("")
    elif i == 3:
        for j in range(len(spells)):
            print(f"{j + 1}.{spells[j]}")
        spell = input("Select your spells(1,2):")


def act1():
    print("ACT 1")
    print(" A chosen adventurer, stumbling upon an ancient prophecy in Eldoria,\n"
          " learns of imminent doom and the pivotal role of the shattered Crystal of Luminescence.\n"
          " The quest commences in tranquil yet ominous landscapes, revealing fragments of the crystal.\n"
          " Mysterious beings and cryptic riddles hint at the realm's forgotten history,\n"
          " propelling the adventurer into a grand journey to avert encroaching darkness.\n"
          " The stage is set for a sweeping odyssey through perilous terrains,\n"
          " where the fate of Eldoria hinges on the adventurer's courage and unraveling\n"
          " the secrets held within the shattered crystal.\n")
    flag = True
    while flag:
        q1 = int(input("You are currently in a cave.\nThere are three ways\nPlease enter you option(1,2,3):"))
        print("")
        if q1 == 1:
            q11 = input((
                            "A few steps ahead there is a merchant who is ready to sell many this.\nIf you wish to see the list enter yes:").lower())
            print("")
            if q11 == "yes":
                items()
        elif q1 == 2:
            q12 = input((
                            f"You have come across a goblin use your {weapon} to attack the goblin.\nDo you wish to attack it(yes/no):").lower())
            print("")
            if q12 == "yes":
                print("You slayed the goblin.")
                q121 = input("Do you wish to go proceed forward(yes/no)").lower()
                print("")
                if q121 == "yes":
                    print("You have reached the merchant.")
                    items()
                else:
                    print("You got caught in trap.")
                    print("YOU DIED")
        else:
            print("You entered boss chamber\nMargit the Fallen Omen slayed you")
            print("YOU DIED")
            flag = False
            break

        q2 = int(input(
            f"After being equipped with {weapon} you are more ready to explore the world of Eldoria.\nIn front of you there is two tunnels.\nOn choosing on you will exit the cave(1,2)."))
        print("")
        if q2 == 1:
            print("You exited the cave.")
            print("Landscape is something out of the fantasy book.")
            print("With mystical beasts and birds.")
            print("In order to reach the next POI you can take either a road,bridge or jump across a clifs")  # POI - point of interest

            q21 = int(input("Enter your option(1,2,3):"))
            if q21 == 1:
                print("You have successfully reached the next POI")
                print("")
            elif q21 == 2:
                print("The bridge collapsed and you fell into a river.")
                print("YOU DIED")
                flag = False
                break
            elif q21 == 3:
                print("A wandering solider was hiding between the clifs and attacked you.")
                print("YOU DIED")
        else:
            print("You were blown into bits by a bobby trap.")
            print("YOU DIED")
        

        break
#act1()
def villagers_interaction():
    print("The player talks with the villagers and learns about their troubles.")
    print("Villager: Welcome, traveler! Our village is in need of assistance.")

def village_quest():
    print("The village chief mentions that the fourth crystal shard is located near a volcano.")
    print("Village Chief: To reach the volcano, you must first embark on a quest.")
    print("Village Chief: Our sacred artifact, the 'Flame Amulet,' has been stolen by bandits.")
    print("Village Chief: Retrieve the Flame Amulet, and you will gain passage to the volcano.")
    choice = input("Will you accept the quest? (yes/no): ").lower()
    if choice == "yes":
        print("Village Chief: Good luck, brave adventurer! The bandits are hiding in the Dark Forest to the east.")
        quest_dark_forest()
    else:
        print("Village Chief: May the luminescent crystals guide you on your journey.")

def quest_dark_forest():
    print("The player sets off towards the Dark Forest.")
    print("As the player enters the forest, they encounter eerie sounds and mysterious creatures.")
    print("Choice 1: Follow the winding path deeper into the forest.")
    print("Choice 2: Take a shortcut through the dense thicket.")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("The player follows the winding path, avoiding immediate danger.")
        print("However, they stumble upon a hidden bandit camp.")
        battle_bandits()
    elif choice == "2":
        print("The player takes the shortcut through the dense thicket.")
        print("They encounter aggressive forest creatures but manage to bypass the bandit camp.")
        print("Choice 1: Confront the bandits directly.")
        print("Choice 2: Sneak around the bandit camp.")
        choice = input("Enter your choice (1/2): ")
        if choice == "1":
            battle_bandits()
        elif choice == "2":
            print("The player successfully sneaks around the bandit camp.")
            print("They find the stolen Flame Amulet hidden in a chest.")
            print("Quest complete! The player can now return to the village chief.")

def battle_bandits():
    print("The player confronts the bandits in a fierce battle.")
    print("Choice 1: Fight using the Rusty Sword.")
    print("Choice 2: Use a stealth approach and surprise the bandits.")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("The player fights valiantly with the Rusty Sword.")
        print("Despite facing multiple bandits, they emerge victorious.")
        print("The stolen Flame Amulet is recovered.")
        print("Quest complete! The player can now return to the village chief.")
    elif choice == "2":
        print("The player uses stealth to surprise the bandits.")
        print("A quick and silent attack results in the recovery of the stolen Flame Amulet.")
        print("Quest complete! The player can now return to the village chief.")

# Main storyline function
def main_storyline():
    print("ACT 3")
    print("In a realm veiled in mystery, our protagonist journeyed through untamed landscapes and dense forests. Tired and weary, they stumbled upon a village\n"
          "nestled at the edge of an ancient forest. The air was thick with an otherworldly calmness, and the villagers, sensing the arrival of a stranger, gathered to welcome the weary traveler.\n")
    print()
    print("As the adventurer entered the village, the inhabitants exchanged curious glances but offered warm smiles.\n"
          "Seeking refuge and respite, the traveler engaged in conversations with the villagers, learning about their traditions, customs, and the enigmatic history of the surrounding lands.\n"
          "It wasn't long before the village chief, a wise elder with a knowing gaze, approached the adventurer. The chief sensed a purpose in the traveler's journey and spoke of a local prophecy that\n"
          "foretold the arrival of a hero bearing the mark of luminescent destiny.")

    villagers_interaction()
    village_quest()

# Execute the main storyline
main_storyline()

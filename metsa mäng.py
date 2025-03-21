import random

# Character stats
player_stats = {
    "health": 100,
    "stamina": 100,
    "luck": 50,
    "inventory": []
}

# Very important NPCs
tim_cheese = {
    "name": "Tim Cheese",
    "slogan": "If you're not cheesy, you're not Timmy."
}

john_pork = {
    "name": "John Pork",
    "slogan": "My pig powers are unbeatable!"
}

gyatt = {
    "name": "Gyatt",
    "slogan": "If you’ve got the Gyatt, you’re unstoppable!"
}

rizz = {
    "name": "Rizz",
    "slogan": "You’ve got the Rizz? You can make anyone fall in love!"
}

def intro():
    print("Welcome to the **brainrot** Adventure Game!")
    print("You are standing at the edge of a very confusing and nonsensical land.")
    print("Your goal is to find the treasure hidden deep inside... Or maybe you just want to vibe.")
    print("Choose wisely, because everything here is a meme and you're gonna need the *Rizz* to survive.")

def random_event():
    events = [
        "You encounter Gyatt, and he offers to carry you to the treasure. You accept.",
        "John Pork appears and gives you a piggyback ride, but his pig powers exhaust you.",
        "Tim Cheese throws you a random cheese wheel. It heals you.",
        "A random *frogsplosion* occurs, leaving you temporarily covered in frogs.",
        "You find a Weed plant and smoke it. Vibes are *immaculate*."
    ]
    event = random.choice(events)
    print(f"\nRandom Event: {event}")
    if "Gyatt" in event:
        player_stats["health"] += 50
        player_stats["stamina"] += 20
        print("Gyatt's strength makes you feel unstoppable. You feel stronger and more powerful!")
    elif "John Pork" in event:
        player_stats["health"] -= 5
        player_stats["stamina"] += 10
        print("You get a piggyback ride, but John Pork’s powers drain you a bit.")
    elif "Tim Cheese" in event:
        player_stats["health"] += 20
        print("Tim Cheese is always here to help, tossing you some fresh cheddar.")
    elif "frogsplosion" in event:
        player_stats["health"] -= 15
        print("Frogs. Everywhere. Not ideal.")
    elif "Weed" in event:
        player_stats["health"] += 10
        print("You feel the vibes flow as you relax. Your health is slightly restored.")
        
def use_healing_item():
    print("\nYou have the following healing items in your inventory:")
    for item in player_stats["inventory"]:
        print(f"- {item}")
    
    item_choice = input("Would you like to use a healing item? (Yes/No): ").lower()
    if item_choice == "yes":
        if player_stats["inventory"]:
            item = input("Which item would you like to use? (Weed/Galaxy Gas/Flaming Hot Cheetos): ").lower()
            if item == "weed" and "Weed" in player_stats["inventory"]:
                player_stats["health"] += 20
                player_stats["inventory"].remove("Weed")
                print("You smoke some Weed, and your health rises as you vibe to the music of the universe.")
            elif item == "galaxy gas" and "Galaxy Gas" in player_stats["inventory"]:
                player_stats["health"] += 50
                player_stats["stamina"] += 25
                print("You inhale the cosmic power of Galaxy Gas. Your health and stamina explode into the cosmos!")
            elif item == "flaming hot cheetos" and "Flaming Hot Cheetos" in player_stats["inventory"]:
                player_stats["health"] += 100
                player_stats["stamina"] += 50
                print("You eat the Flaming Hot Cheetos. Your body is infused with unexplainable energy.")
            else:
                print("You don't have that item in your inventory.")
        else:
            print("You have no healing items in your inventory.")
    else:
        print("You decide not to use any items.")

def fight_creature():
    print("\nYou bravely decide to fight the creature.")
    if random.choice([True, False]) and player_stats["stamina"] > 20:
        print("You defeat the creature, but it turns into a giant piece of cheddar cheese. The cheese consumes you.")
        player_stats["inventory"].append("Cheddar Cheese")
        return "You win! ... Or did you?"
    else:
        print("The creature is too strong. John Pork runs away screaming.")
        return "You survived, but barely."

def run_away():
    print("\nYou decide to run away.")
    if random.choice([True, False]):
        print("You run into an army of flamingos. They judge you silently.")
        return "You survived, but with some awkward judgment."
    else:
        print("You trip over a random banana peel and break your ankle. Oof.")
        return "You survive, but now you’re just limping along."

def check_inventory():
    print("\nYour current inventory contains:")
    if player_stats["inventory"]:
        for item in player_stats["inventory"]:
            print(f"- {item}")
    else:
        print("Nothing of value. But who needs value in this world?")
        
def dark_path():
    print("\nYou have chosen the dark path.")
    print("It's very dark and you can barely see anything. Suddenly, you hear a growl behind you!")
    print("You have two options:")
    print("1. Fight the creature.")
    print("2. Run away.")

    choice = input("Enter 1 or 2 to make your choice: ")
    if choice == "1":
        return fight_creature()
    elif choice == "2":
        return run_away()
    else:
        print("Invalid choice. Please choose again.")
        return dark_path()

def mountain_path():
    print("\nYou have chosen the mountain path.")
    print("The climb is tough, but you reach the top where a beautiful view awaits.")
    print("But wait, there seems to be someone following you!")
    print("It's Tim Cheese. He asks you: 'Do you want some cheese?'")
    print("You have two options:")
    print("1. Accept the cheese.")
    print("2. Decline the cheese and continue your journey.")

    choice = input("Enter 1 or 2 to make your choice: ")
    if choice == "1":
        print("You accept the cheese. It's the best cheese you've ever tasted.")
        player_stats["health"] += 10
        player_stats["inventory"].append("Cheese")
        return "You continue your journey, more powerful than ever!"
    elif choice == "2":
        print("You decline the cheese. Tim Cheese is disappointed and leaves.")
        return "You continue your journey, but you've missed a great opportunity."
    else:
        print("Invalid choice. Please choose again.")
        return mountain_path()

def gyatt_path():
    print("\nYou encounter **Gyatt**.")
    print("Gyatt flexes his muscles and gives you a motivational speech about self-improvement.")
    print("You have two options:")
    print("1. Listen to Gyatt's motivational speech and gain strength.")
    print("2. Ignore Gyatt and continue your journey.")
    
    choice = input("Enter 1 or 2 to make your choice: ")
    if choice == "1":
        player_stats["health"] += 50
        player_stats["stamina"] += 30
        print("You feel unstoppable now! Gyatt's words have made you stronger.")
        return "You are now a beast on this journey!"
    elif choice == "2":
        print("Gyatt gives you a nod of respect and continues flexing.")
        return "You keep moving, but you missed a great chance to get stronger."
    else:
        print("Invalid choice. Please choose again.")
        return gyatt_path()

def rizz_path():
    print("\nYou encounter **Rizz**.")
    print("Rizz approaches with unmatched confidence and charm, and he gives you a wink.")
    print("You have two options:")
    print("1. Attempt to match Rizz’s charm and gain charisma.")
    print("2. Ignore Rizz and move on.")

    choice = input("Enter 1 or 2 to make your choice: ")
    if choice == "1":
        player_stats["luck"] += 30
        print("You feel like a true master of charm now. Your luck increases dramatically.")
        return "You now have the Rizz!"
    elif choice == "2":
        print("Rizz smiles and walks away, his confidence leaving an aura behind.")
        return "You keep moving, but you missed out on some serious charm."
    else:
        print("Invalid choice. Please choose again.")
        return rizz_path()

def first_choice():
    print("\nYou have four paths to choose from:")
    print("1. The dark path that leads into the forest.")
    print("2. The well-lit path that leads up a mountain where Tim Cheese awaits.")
    print("3. A mysterious path that leads to Gyatt, the motivational powerhouse.")
    print("4. The smooth path that leads to Rizz, the King of Charm.")

    choice = input("Enter 1, 2, 3, or 4 to make your choice: ")
    if choice == "1":
        return dark_path()
    elif choice == "2":
        return mountain_path()
    elif choice == "3":
        return gyatt_path()
    elif choice == "4":
        return rizz_path()
    else:
        print("Invalid choice. Please choose again.")
        return first_choice()

def game_loop():
    while True:  # Infinite loop, ensuring the game never ends
        intro()
        result = first_choice()
        print(result)

        random_event()  # Trigger a random event
        check_inventory()  # Display the player's inventory
        print(f"Current Health: {player_stats['health']}, Stamina: {player_stats['stamina']}, Luck: {player_stats['luck']}")
        
        if player_stats["health"] <= 0 or player_stats["stamina"] <= 0:
            print("\nUh-oh! Your health or stamina is low, but don’t worry! Keep going!")
            continue

if __name__ == "__main__":
    game_loop()  # This starts the endless game loop

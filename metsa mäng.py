import random

def intro():
    print("Welcome to the Adventure Game!")
    print("You are standing at the edge of a dark forest.")
    print("Your goal is to find the treasure hidden deep inside.")
    print("Choose wisely and survive the challenges along the way!")

def first_choice():
    print("\nYou have two paths to choose from:")
    print("1. The dark path that leads into the forest.")
    print("2. The well-lit path that leads up a mountain.")
    
    choice = input("Enter 1 or 2 to make your choice: ")
    if choice == "1":
        return dark_path()
    elif choice == "2":
        return mountain_path()
    else:
        print("Invalid choice. Please choose again.")
        return first_choice()

def dark_path():
    print("\nYou have chosen the dark path.")
    print("It's very dark and you can barely see anything.")
    print("Suddenly, you hear a growl behind you!")
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
    print("You have two options:")
    print("1. Confront the stranger.")
    print("2. Try to escape down the other side of the mountain.")
    
    choice = input("Enter 1 or 2 to make your choice: ")
    if choice == "1":
        return confront_stranger()
    elif choice == "2":
        return escape_mountain()
    else:
        print("Invalid choice. Please choose again.")
        return mountain_path()

def fight_creature():
    print("\nYou bravely decide to fight the creature.")
    if random.choice([True, False]):
        print("You defeat the creature and find the treasure hidden behind it!")
        return "You win! Congratulations!"
    else:
        print("The creature is too strong. You lose.")
        return "Game Over."

def run_away():
    print("\nYou decide to run away.")
    if random.choice([True, False]):
        print("You manage to escape safely, but you don't find the treasure.")
        return "Game Over."
    else:
        print("You run into a trap and fall into a pit.")
        return "Game Over."

def confront_stranger():
    print("\nYou confront the stranger.")
    if random.choice([True, False]):
        print("The stranger is friendly and gives you a map to the treasure!")
        return "You win! Congratulations!"
    else:
        print("The stranger turns out to be an enemy and attacks you.")
        return "Game Over."

def escape_mountain():
    print("\nYou try to escape down the other side of the mountain.")
    if random.choice([True, False]):
        print("You successfully escape but find no treasure.")
        return "Game Over."
    else:
        print("You fall down the mountain and get injured.")
        return "Game Over."

if __name__ == "__main__":
    intro()
    result = first_choice()
    print(result)

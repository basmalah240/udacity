import time
import random

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro(enemy):
    print_pause("You find yourself in a vast meadow,")
    print_pause("the breeze dancing through tall grass and bursts of golden wildflowers.")
    print_pause(f"Whispers from the nearby village tell of a {enemy} causing chaos.")
    print_pause("Ahead of you stands a rickety old cottage.")
    print_pause("To your right? A shadowy cave mouth yawns like it's daring you to step in.")
    print_pause("Clutched in your hand is your trusty (though unimpressive) butter knife.")

def cave(inventory):
    print_pause("You step cautiously into the cave, half-expecting bats.")
    print_pause("Turns out it’s just a cozy, tiny cavern.")
    if "sword" in inventory:
        print_pause("You've already taken the Blade of Zynthar. There's nothing else here.")
    else:
        print_pause("Something metallic catches your eye behind a boulder...")
        print_pause("Score! You’ve discovered the Blade of Zynthar!")
        print_pause("You toss your old dagger into the shadows.")
        inventory.append("sword")
    print_pause("You walk back into the field, glowing with confidence.")

def cottage(enemy, inventory):
    print_pause("You approach the door of the cottage.")
    print_pause("Just as you raise your hand to knock, the door creaks open...")
    print_pause(f"... and boom! Out pops the {enemy}!")
    print_pause(f"Yikes! This is the {enemy}'s hideout!")
    print_pause(f"The {enemy} screeches and lunges at you.")

    while True:
        choice = input("Do you want to (1) fight or (2) run away?\n")
        if choice == "1":
            if "sword" in inventory:
                print_pause("You unsheath the Blade of Zynthar!")
                print_pause("The blade hums with power as you brace for battle.")
                print_pause(f"The {enemy} stares at your weapon... and bolts!")
                print_pause(f"You've rid the village of the {enemy}. Victory is yours! 🎉")
            else:
                print_pause("You do your best...")
                print_pause("But your butter knife flails more than it slashes.")
                print_pause(f"The {enemy} easily defeats you. Oof.")
            break
        elif choice == "2":
            print_pause("You run back into the field. Thankfully, you're not followed.")
            break
        else:
            print_pause("Please enter 1 or 2.")

def play_game():
    enemies = ["mischievous rogue", "shapeshifter", "pirate", "mad warlock", "vengeful banshee"]
    enemy = random.choice(enemies)
    inventory = []

    intro(enemy)

    while True:
        choice = input("Enter 1 to knock on the door of the cottage.\n"
                       "Enter 2 to sneak a peek inside the cave.\n"
                       "What’s your move, adventurer?\n"
                       "(Please enter 1 or 2.)\n")
        if choice == "1":
            cottage(enemy, inventory)
            break
        elif choice == "2":
            cave(inventory)
        else:
            print_pause("Please enter 1 or 2.")

    while True:
        again = input("Would you like to play again? (yes/no)\n").lower()
        if again == "yes":
            print_pause("Sweet! Restarting the adventure...\n")
            play_game()
            break
        elif again == "no":
            print_pause("Thanks for playing, legend. Until your next quest! ✨")
            break
        else:
            print_pause("Please enter 'yes' or 'no'.")

play_game()
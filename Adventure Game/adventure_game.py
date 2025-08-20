import time
import random

weapons_list = ["Dagger", "Rusty Spoon", "Broken Bottle", "Banana Peel"]
enemies_list = ["Shadow Thief", "Cursed Knight", "Goblin Warlord", "Undead Mage"]


def delayed_print(msg, delay=1):
    print(msg)
    time.sleep(delay)


def valid_input(prompt, valid_options):
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        print(f"Invalid input! Please enter one of: {', '.join(valid_options)}")


def main_game():
    delayed_print("⚔️ Welcome to the Adventure Game! ⚔️")
    game_loop()


def intro(current_enemy):
    delayed_print("\nYou stand in an eerie forest clearing.")
    delayed_print(f"Rumors speak of a {current_enemy} terrorizing the nearby village.")
    delayed_print("To your left stands a dark, foreboding house.")
    delayed_print("To your right, a mysterious cave entrance glows faintly.\n")


def cottage_path(has_sword, current_enemy):
    delayed_print(f"\nYou approach the {current_enemy}'s hideout...")
    delayed_print("The door bursts open! The enemy attacks!\n")

    if has_sword:
        delayed_print("You draw your glowing sword!")
        delayed_print(f"The {current_enemy} staggers back in fear!")
        delayed_print("With one mighty swing, you defeat the villain!")
        delayed_print("\n💫 YOU WIN! The village is saved! 💫")
        return "win"
    else:
        delayed_print("You only have your pitiful starter weapon...")
        choice = valid_input("Do you (1) Fight bravely or (2) Run away? ", ("1", "2"))
        if choice == "1":
            delayed_print("\nYou try to fight but your weapon shatters!")
            delayed_print(f"The {current_enemy} laughs and defeats you easily.")
            delayed_print("\n☠️ YOU LOSE! Try finding a better weapon first. ☠️")
            return "lose"
        else:
            delayed_print("\nYou wisely retreat to fight another day!")
            delayed_print("Maybe that cave has something useful...")
            return "retreat"


def cave_path(already_visited):
    if already_visited:
        delayed_print("\nYou return to the cave...")
        delayed_print("But it's empty now. Just echoes and dust.")
        delayed_print("You find nothing new here.\n")
        return False
    else:
        delayed_print("\nYou enter the glowing cave...")
        delayed_print("Ancient runes line the walls.")
        delayed_print("There! Embedded in stone - a magical sword!")
        delayed_print("\n⚔️ You acquired the SWORD OF LEGENDS! ⚔️\n")
        return True


def game_loop():
    while True:
        current_enemy = random.choice(enemies_list)
        has_sword = False
        cave_visited = False

        delayed_print(f"\nYour journey begins with only a {random.choice(weapons_list)}...")
        intro(current_enemy)

        while True:
            choice = valid_input(
                "\nWhere will you go?\n"
                "1 - Approach the enemy's house\n"
                "2 - Explore the cave\n"
                "Choose (1 or 2): ",
                ("1", "2")
            )

            if choice == "1":
                result = cottage_path(has_sword, current_enemy)
                if result == "retreat":
                    continue
                break
            elif choice == "2":
                got_sword = cave_path(cave_visited)
                if got_sword:
                    has_sword = True
                cave_visited = True

        play_again = valid_input("\nPlay again? (yes/no): ", ("yes", "no"))
        if play_again != "yes":
            delayed_print("\nThanks for playing! Until your next adventure!")
            break


main_game()
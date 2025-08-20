import time
import random


weapons = ["Dagger", "Rusty Spoon", "Broken Bottle", "Banana Peel"]
enemies = ["Shadow Thief", "Cursed Knight", "Goblin Warlord", "Undead Mage"]


def valid_input(prompt, valid_options):
    """Validate user input against a list of allowed options.
    
    Args:
        prompt (str): The input prompt to display.
        valid_options (list): List of valid input choices.
        
    Returns:
        str: The user's valid choice.
    """
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        print(
            f"Invalid input! Please enter one of: {', '.join(valid_options)}"
        )


def main_game():
    """Start the adventure game."""
    print("⚔ Welcome to the Adventure Game! ⚔")
    time.sleep(1)
    game_loop()


def intro(current_enemy):
    """Display the game introduction with the current enemy.
    
    Args:
        current_enemy (str): The randomly selected enemy.
    """
    print("\nYou stand in an eerie forest clearing.")
    time.sleep(1)
    print(f"Rumors speak of a {current_enemy} terrorizing the nearby village.")
    time.sleep(1)
    print("To your left stands a dark, foreboding house.")
    time.sleep(1)
    print("To your right, a mysterious cave entrance glows faintly.\n")
    time.sleep(1)


def cottage_path(has_sword, current_enemy):
    """Handle the cottage path encounter.
    
    Args:
        has_sword (bool): Whether the player has the sword.
        current_enemy (str): The current enemy.
        
    Returns:
        str: "win", "lose", or "retreat".
    """
    print(f"\nYou approach the {current_enemy}'s hideout...")
    time.sleep(1)
    print("The door bursts open! The enemy attacks!\n")
    time.sleep(1)

    if has_sword:
        print("You draw your glowing sword!")
        time.sleep(1)
        print(f"The {current_enemy} staggers back in fear!")
        time.sleep(1)
        print("With one mighty swing, you defeat the villain!")
        time.sleep(1)
        print("\n💫 YOU WIN! The village is saved! 💫")
        return "win"
    else:
        print("You only have your pitiful starter weapon...")
        time.sleep(1)
        choice = valid_input(
            "Do you (1) Fight bravely or (2) Run away? ", ("1", "2")
        )
        if choice == "1":
            print("\nYou try to fight but your weapon shatters!")
            time.sleep(1)
            print(f"The {current_enemy} laughs and defeats you easily.")
            time.sleep(1)
            print("\n☠ YOU LOSE! Try finding a better weapon first. ☠")
            return "lose"
        else:
            print("\nYou wisely retreat to fight another day!")
            time.sleep(1)
            print("Maybe that cave has something useful...")
            return "retreat"


def cave_path(already_visited):
    """Handle the cave exploration path.
    
    Args:
        already_visited (bool): Whether the player has been here before.
        
    Returns:
        bool: True if the player finds the sword, False otherwise.
    """
    if already_visited:
        print("\nYou return to the cave...")
        time.sleep(1)
        print("But it's empty now. Just echoes and dust.")
        time.sleep(1)
        print("You find nothing new here.\n")
        return False
    else:
        print("\nYou enter the glowing cave...")
        time.sleep(1)
        print("Ancient runes line the walls.")
        time.sleep(1)
        print("There! Embedded in stone - a magical sword!")
        time.sleep(1)
        print("\n⚔ You acquired the SWORD OF LEGENDS! ⚔\n")
        return True


def game_loop():
    """Main game loop controlling the gameplay flow."""
    while True:
        current_enemy = random.choice(enemies)
        has_sword = False
        cave_visited = False
        starter_weapon = random.choice(weapons)

        print(f"\nYour journey begins with only a {starter_weapon}...")
        time.sleep(1)
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
            print("\nThanks for playing! Until your next adventure!")
            break


if __name__ == "__main__":
    main_game()
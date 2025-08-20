import time
import random

weapons_list = ["Dagger", "Rusty Spoon", "Broken Bottle", "Banana Peel"]
enemies_list = [
    "Shadow Thief",
    "Cursed Knight",
    "Goblin Warlord",
    "Undead Mage"
]


def add_delay(msg, delay):
    print(msg)
    time.sleep(delay)


def valid_input(prompt, valid_options):
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        print(
             f"Invalid input! Please enter one of: {', '.join(valid_options)}"
        )


def main_game():
    add_delay("⚔️ Welcome to the Adventure Game! ⚔️", 1)
    game_loop()


def intro(current_enemy):
    add_delay("\nYou stand in an eerie forest clearing.", 1)
    add_delay(
        f"Rumors speak of a {current_enemy} terrorizing the nearby village.",
        1
    )
    add_delay("To your left stands a dark, foreboding house.", 1)
    add_delay("To your right, a mysterious cave entrance glows faintly.\n", 1)


def cottage_path(has_sword, current_enemy):
    add_delay(f"\nYou approach the {current_enemy}'s hideout...", 1)
    add_delay("The door bursts open! The enemy attacks!\n", 1)

    if has_sword:
        add_delay("You draw your glowing sword!", 1)
        add_delay(f"The {current_enemy} staggers back in fear!", 1)
        add_delay("With one mighty swing, you defeat the villain!", 1)
        add_delay("\n💫 YOU WIN! The village is saved! 💫", 1)
        return "win"
    else:
        add_delay("You only have your pitiful starter weapon...", 1)
        choice = valid_input(
              "Do you (1) Fight bravely or (2) Run away? ",
              ("1", "2")
        )
        if choice == "1":
            add_delay("\nYou try to fight but your weapon shatters!", 1)
            add_delay(f"The {current_enemy} laughs and defeats you easily.", 1)
            add_delay(
                "\n☠️ YOU LOSE! Try finding a better weapon first ☠️",
                1
            )
            return "lose"
        else:
            add_delay("\nYou wisely retreat to fight another day!", 1)
            add_delay("Maybe that cave has something useful...", 1)
            return "retreat"


def cave_path(already_visited):
    if already_visited:
        add_delay("\nYou return to the cave...", 1)
        add_delay("But it's empty now. Just echoes and dust.", 1)
        add_delay("You find nothing new here.\n", 1)
        return False
    else:
        add_delay("\nYou enter the glowing cave...", 1)
        add_delay("Ancient runes line the walls.", 1)
        add_delay("There! Embedded in stone - a magical sword!", 1)
        add_delay("\n⚔️ You acquired the SWORD OF LEGENDS! ⚔️\n", 1)
        return True


def game_loop():
    while True:
        current_enemy = random.choice(enemies_list)
        has_sword = False
        cave_visited = False

        add_delay(
            f"\nYour journey begins with only a "
            f"{random.choice(weapons_list)}...",
            1
        )
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
            add_delay("\nThanks for playing! Until your next adventure!", 1)
            break


main_game()

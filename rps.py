import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        """Each player must implement this method"""
        pass

    def learn(self, my_move, their_move):
        """Optional method to remember past moves"""
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = random.choice(moves)

    def move(self):
        return self.their_last_move

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = random.choice(moves)

    def move(self):
        index = moves.index(self.my_last_move)
        next_index = (index + 1) % len(moves)
        return moves[next_index]

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


class HumanPlayer(Player):
    def move(self):
        while True:
            user_input = input(
                "Enter your move (rock, paper, scissors): "
                ).lower()
            if user_input in moves:
                return user_input
            print(
                "Invalid input!"
                "Please enter 'rock', 'paper', or 'scissors'."
                )


def beats(one, two):
    return (
        (one == 'rock' and two == 'scissors') or
        (one == 'scissors' and two == 'paper') or
        (one == 'paper' and two == 'rock')
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, round_num):
        print(f"\nRound {round_num + 1}:")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} | Player 2: {move2}")

        if beats(move1, move2):
            print("** Player 1 wins the round! **")
            self.p1_score += 1
        elif beats(move2, move1):
            print("** Player 2 wins the round! **")
            self.p2_score += 1
        else:
            print("** It's a tie! **")

        print(
            f"Score => Player 1: {self.p1_score} | Player 2: {self.p2_score}"
            )

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\n🎮 Game start! Best of 3 rounds.")
        for round_num in range(3):
            self.play_round(round_num)

        print("\n🏁 Game Over!")
        print(
            f"Final Score => Player 1: {self.p1_score} |"
            f" Player 2: {self.p2_score}"
            )
        if self.p1_score > self.p2_score:
            print("🎉 Winner: Player 1!")
        elif self.p2_score > self.p1_score:
            print("🤖 Winner: Player 2!")
        else:
            print("🫱🫲 It's a tie!")


if __name__ == '__main__':
    opponents = [RockPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    opponent = random.choice(opponents)
    game = Game(HumanPlayer(), opponent)
    game.play_game()

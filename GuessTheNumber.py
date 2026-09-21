import random


class ForceExit(Exception):
    pass


def ask(message):
    answer = input(message).strip().lower()
    if answer == "exit":
        raise ForceExit()
    return answer


def ask_int(prompt, *, min_value=None, max_value=None, greater_than=None):
    while True:
        value = ask(prompt)
        try:
            parsed = int(value)
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        if min_value is not None and parsed < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.\n")
            continue

        if max_value is not None and parsed > max_value:
            print(f"Please enter a number less than or equal to {max_value}.\n")
            continue

        if greater_than is not None and parsed <= greater_than:
            print(f"Please enter a number greater than {greater_than}.\n")
            continue

        return parsed


def choose_difficulty():
    difficulty_map = {
        "easy": {"attempts": 12, "range": 50},
        "medium": {"attempts": 8, "range": 100},
        "hard": {"attempts": 5, "range": 200},
    }

    while True:
        level = ask("Choose difficulty (easy/medium/hard): ").lower()
        if level in difficulty_map:
            return level, difficulty_map[level]
        print('Please choose "easy", "medium", or "hard".\n')


def get_number_range(level_settings):
    max_default = level_settings["range"]
    while True:
        minimum = ask_int("Enter the minimum number to guess: ")
        maximum = ask_int(
            f"Enter the maximum number to guess (must be greater than {minimum}): ",
            greater_than=minimum,
        )

        if maximum <= max_default:
            return minimum, maximum

        print(
            f"The range is too large for this difficulty. Try a maximum value up to {max_default}.\n"
        )


def play_round(score):
    level, settings = choose_difficulty()
    minimum, maximum = get_number_range(settings)
    secret_number = random.randint(minimum, maximum)
    attempts_left = settings["attempts"]

    print(f"\nYou chose {level} mode. Guess the number between {minimum} and {maximum}.\n")

    while attempts_left > 0:
        user_guess = ask_int(
            f"Guess the number between {minimum} and {maximum} ({attempts_left} attempts left): ",
            min_value=minimum,
            max_value=maximum,
        )

        if user_guess == secret_number:
            print("You did it!\n")
            score["wins"] += 1
            return score

        if user_guess < secret_number:
            print("Too low! Try again!\n")
        else:
            print("Too high! Try again!\n")

        if level in {"easy", "medium"} and attempts_left % 2 == 0:
            print("Hint: the secret number is " + ("higher" if user_guess < secret_number else "lower") + " than your guess.\n")

        attempts_left -= 1

    score["losses"] += 1
    print(f"Out of attempts! The secret number was {secret_number}.\n")
    return score


def guessNumber():
    score = {"wins": 0, "losses": 0}

    try:
        print("Welcome to Guess The Number!\nYou will be guessing!\n")

        while True:
            score = play_round(score)
            print(f"Current score: {score['wins']} wins, {score['losses']} losses\n")

            while True:
                retry = ask("Play again? y/n\n").lower()
                if retry == "y":
                    print("\n")
                    break
                if retry == "n":
                    print(f"Thanks for playing! Final score: {score['wins']} wins, {score['losses']} losses")
                    return
                print('Please enter "y" or "n"\n')

    except ForceExit:
        print("\nYou typed exit. Quitting from function...")
        return


guessNumber()

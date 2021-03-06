"""
Students:
Paul Seong Uk Yeon (A00990811)
April Sin Hau Cheng (A01261858)

1510 Assignment 4
"""
import itertools
from itertools import count
from random import randint, choice
from time import sleep
import doctest
import os
from coolname import generate
import art


# Player Specifications
def PLAYER_NAME_CHOICES():
    return ["I would like to choose this name!", "I would like to choose another one at random",
            "I would like to choose my own name!"]


def PLAYER_BASE_HP() -> int:
    """Return player base health point as a number 20.

    :return: player base health point as an integer 20
    """
    return 20


def PLAYER_HEAL_HP() -> int:
    """Return player maximum heal health point as a number 4.

    :return: player heal health point as an integer 4
    """
    return 4


def PLAYER_STARTING_POSITION() -> list:
    """Return the player's starting position as coordinate [0, 0].

    :return: player's starting position coordinate as a list with two elements that are integers
    """
    return [0, 0]


def PLAYER_EXPERIENCE_GAIN() -> int:
    """Return player experience gain as 100.

    :return: player's experience gain as integer
    """
    return 100


# Class Specification
def MAGE_HP_INCREMENT() -> int:
    """Return Mage class health increment as 10.

    :return: Mage class health point increment as integer 10
    """
    return 5


def THIEF_HP_INCREMENT() -> int:
    """Return Thief class health increment as 10.

    :return: Thief class health point increment as integer 10
    """
    return 20


def RANGER_HP_INCREMENT() -> int:
    """Return Ranger class health increment as 10.

    :return: Ranger class health point increment as integer 10
    """
    return 10


def WARRIOR_HP_INCREMENT() -> int:
    """Return Warrior class health increment as 10.

    :return: Warrior class health point increment as integer 10
    """
    return 30


def MAGE() -> dict:
    """Return Mage class dictionary.

    The key represents the player's level, which changes the specifications when the player levels up.
    Each level indicates it own specifications including level name, experience required to level up,
    attack names available per level, player's max HP, player's minimum and maximum damage amount,
    and the player's accuracy rate for the respective level.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Mage", "experience_needed": 300, "attack_name": "Fireball",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 15, "base_damage_max": 20, "accuracy_rate": 45},
        2: {"level": 2, "level_name": "Mage", "experience_needed": 600, "attack_name": "Firestorm",
            "max_hp": PLAYER_BASE_HP() + MAGE_HP_INCREMENT(), "base_damage_min": 20, "base_damage_max": 25,
            "accuracy_rate": 55},
        3: {"level": 3, "level_name": "Arch Mage", "attack_name": "Hellfire",
            "max_hp": PLAYER_BASE_HP() + (MAGE_HP_INCREMENT() * 2), "base_damage_min": 25, "base_damage_max": 35,
            "accuracy_rate": 70}
    }


def THIEF() -> dict:
    """Return Thief class dictionary.

    The key represents the player's level, which changes the specifications when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Thief", "experience_needed": 200, "attack_name": "Pickpocket",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 5, "base_damage_max": 10, "accuracy_rate": 65},
        2: {"level": 2, "level_name": "Bandit", "experience_needed": 500, "attack_name": "Boomerang Step",
            "max_hp": PLAYER_BASE_HP() + THIEF_HP_INCREMENT(), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 75},
        3: {"level": 3, "level_name": "Hermit", "attack_name": "Assassinate",
            "max_hp": PLAYER_BASE_HP() + (THIEF_HP_INCREMENT() * 2), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 80}
    }


def RANGER() -> dict:
    """Return Ranger class dictionary.

    The key represents the player's level, which changes the specifications when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Ranger", "experience_needed": 300, "attack_name": "Iron Arrow",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 5, "base_damage_max": 10, "accuracy_rate": 85},
        2: {"level": 2, "level_name": "Sniper", "experience_needed": 600, "attack_name": "Mortal Blow",
            "max_hp": PLAYER_BASE_HP() + RANGER_HP_INCREMENT(), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 90},
        3: {"level": 3, "level_name": "Marksman", "attack_name": "Dragon's Breath",
            "max_hp": PLAYER_BASE_HP() + (RANGER_HP_INCREMENT() * 2), "base_damage_min": 15, "base_damage_max": 20,
            "accuracy_rate": 95}
    }


def WARRIOR() -> dict:
    """Return Warrior class dictionary.

    The key represents the player's level, which change the player's status when they level up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Warrior", "experience_needed": 400, "attack_name": "Threaten",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 5, "base_damage_max": 10, "accuracy_rate": 50},
        2: {"level": 2, "level_name": "Knight", "experience_needed": 700, "attack_name": "Power Crash",
            "max_hp": PLAYER_BASE_HP() + WARRIOR_HP_INCREMENT(), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 50},
        3: {"level": 3, "level_name": "Paladin", "attack_name": "Heaven's Hammer",
            "max_hp": PLAYER_BASE_HP() + (WARRIOR_HP_INCREMENT() * 2), "base_damage_min": 15, "base_damage_max": 20,
            "accuracy_rate": 50}
    }


# Monster Specification
def BASE_MONSTER_HP() -> int:
    """Return the monster's base health point as 10.

    :return: monster's base health point as an integer 10
    """
    return 10


def MONSTER_HP_INCREMENT() -> int:
    """Return the monster's health point increment as 5.

    :return: monster's health point increment as an integer 5
    """
    return 7


def MONSTER_BASE_MINIMUM_DAMAGE():
    """Return monster's base minimum damage as 5

    :return: monster's base minimum damage as an integer 5
    """
    return 5


def MONSTER_BASE_DAMAGE() -> int:
    """Return monster's base damage as 10.

    The number is used in the roll_die function to give an output of 1 - 10 inclusive.

    :return: monster's base damage as an integer 10
    """
    return 10


def MONSTER_DAMAGE_INCREMENT() -> int:
    """Return the monster's damage increment as 5.

    :return: monster's damage increment as an integer 5
    """
    return 5


def MONSTER_HP_AND_DAMAGE() -> dict:
    """Return monster health point dictionary.

    The key represents the player's level, and the value is a dictionary that indicates the monster new health point
    when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "hp": BASE_MONSTER_HP(), "min_damage": MONSTER_BASE_MINIMUM_DAMAGE(),
            "max_damage": MONSTER_BASE_DAMAGE()},
        2: {"level": 2, "hp": BASE_MONSTER_HP() + MONSTER_HP_INCREMENT(),
            "min_damage": MONSTER_BASE_MINIMUM_DAMAGE() + MONSTER_DAMAGE_INCREMENT(),
            "max_damage": MONSTER_BASE_DAMAGE() + MONSTER_DAMAGE_INCREMENT()},
        3: {"level": 3, "hp": BASE_MONSTER_HP() + (MONSTER_HP_INCREMENT() * 2),
            "min_damage": MONSTER_BASE_MINIMUM_DAMAGE() + (MONSTER_DAMAGE_INCREMENT() * 2),
            "max_damage": MONSTER_BASE_DAMAGE() + (MONSTER_DAMAGE_INCREMENT() * 2)}
    }


def LIST_OF_MONSTERS() -> list:
    """Return the list of monster names.

    The list is put through the random module to pick a random name.

    :return: a list
    """
    return ["Amputator", "Bone Breaker", "Dark Cultist", "Fallen Shaman", "Flesh Harvester", "Terror Bat",
            "Dust Imp", "Demonic Hellflyer"]


def LIST_OF_MONSTER_TYPES() -> list:
    """Return the list of possible monster types.

    The list is put through the random module to pick a random type.

    :return: a list
    """
    return ["Cave of Alcarnus", "Necropolis Mines", "River of Kehjan", "Black Canyon Mines", "Ureh Caverns"]


def LIST_OF_MONSTER_ATTACKS() -> list:
    """Return a list of attack names.

    :return: a list
    """
    return ['Bite', 'Slash', 'Poisonous Trap']


# Boss Specifications
def LIST_OF_BOSS_NAME() -> list:
    """Return a list of boss names.

    :return: a list
    """
    return ["Kalzeruth", "Mandrasath", "Claughuth", "Felscathor"]


def BOSS_MAX_HP() -> int:
    """Return boss health point as 30.

    :return: an integer 30
    """
    return 60


def BOSS_MAX_DAMAGE() -> int:
    """Return boss damage as 10.

    :return: an integer 10
    """
    return 20


def BOSS_POSITION() -> list:
    """Return boss' fixed position as [25, 25]

    :return: a list with two number elements
    """
    return [14, 14]


def RANDOM_BOSS_ATTACK() -> list:
    """Return a list of attack names.

    :return: a list
    """
    return ['Massacre', "Demolish", "Torture", "Execute", "Harvest"]


# Game helper functions
def RUN_AWAY_PROBABILITY() -> int:
    """Return the number for probability of running away.

    The number is used in the roll_die function to simulate a 20% chance.

    :return: an integer 5
    """
    return 5


def RUN_AWAY_DAMAGE_RANGE() -> int:
    """Return the maximum run away damage as 4.

    The number is used in the roll_die function to give an output of 1 - 4 inclusive.

    :return: an integer 4
    """
    return 4


def INITIAL_ATTACK_PROBABILITY() -> int:
    """Return the number 100.

    The number is used in the roll_die function to give an output of 1 - 100 inclusive.

    :return: an integer 100
    """
    return 100


def BATTLE_CHANCE_PROBABILITY() -> int:
    """Return the probability of encountering an enemy upon movement.

    The number is used in the roll_die function to simulate a 20% chance.

    :return: an integer 5
    """
    return 5


def BOARD_SIZE() -> int:
    """Return the size of the board.

    The number is used as the width and height to create a board.

    :return: an integer
    """
    return 25


def CLASS_LIST() -> list:
    """Return the list of possible class choices.

    The list is put through the input checker function to allow the player to choose.

    :return: a list
    """
    return ["Mage", "Thief", "Ranger", "Warrior"]


def YES_OR_NO() -> list:
    """Return a Yes or No list.

    The list is put through the input checker function to allow the player to choose.

    :return: a list
    """
    return ["Yes", "No"]


def LOCATION_DESCRIPTION() -> list:
    """Return list of location description.

    :return: a list
    """
    return [
        """The room is lit by the light seeping through from the previous location, but you instantly feel the
             difference in the atmosphere already. For some reason, you are just a bit more cold.""",
        """You start to move on an instinct as the seeping light no longer covers the entirety of the room
             anymore. You start to feel a shiver up your spine every step you take.""",
        """This room is surprisingly warm... You wonder why...""",
        """You start to feel more paranoid as time passes, and keep thinking back on your life and whether
             or not you'll be able to get out of here alive""",
        """Your steps seem to have slowed down and without confidence...""",
        """There's water dripping from the top, but you don't know why because you can't see how far up the
             ceiling is in this dark.""",
        """You start to feel more paranoid as time passes, and keep thinking back on your life and whether
             or not you'll be able to get out of here alive""",
        """The room makes you regret ever starting this journey. Every step feels more tiring than before.""",
        """The room is lighted by torches along the sides of the walls. You feel warmer than before.""",
        """The room is filled with fog, but you aren't sure what exactly they are. You only know that it isn't
             a pleasant feeling. You want to exit the room as soon as you can.""",
        """You are starting to consider quitting. This isn't what you expected. Nothing is worth this pain.""",
        """There's a small pond in the middle of the room. You think about drinking from the pond, but upon
             further inspection, you find that the water has skeletal remains in it. You feel sick.""",
        """This room is extremely cold. You are likely to get a frostbite in this weather.""",
        """The room seems to have some type of wildlife, as you hear the cicadas crying somewhere in the room.""",
        """This room has plants growing all around. You can also see mushrooms growing beneath the biggest tree
             in the room. Although you are exhausted and hungry, you aren't sure these are safe to eat.""",
        """The room is pitch dark and makes you want to give up everything."""
    ]


def color_string_green(given_string):
    """Return a string wrapped in ANSI escape code for green.

    :param given_string: a string
    :return: a string

    >>> string = "Paul"
    >>> test_string = '\x1b[32;1mPaul\x1b[0m'
    >>> test_string == color_string_green(string)
    True
    """
    return f"\u001b[32;1m{given_string}\u001b[0m"


def color_string_red(given_string):
    """Return a string wrapped in ANSI escape code for red.

    :param given_string: a string
    :return: a string

    >>> string = "April"
    >>> test_string = '\x1b[31mApril\x1b[0m'
    >>> test_string == color_string_red(string)
    True
    """
    return f"\u001b[31m{given_string}\u001b[0m"


def color_string_yellow(given_string):
    """Return a string wrapped in ANSI escape code for yellow.

    :param given_string: a string
    :return: a string

    >>> string = "Zelda"
    >>> test_string = '\x1b[33;1mZelda\x1b[0m'
    >>> test_string == color_string_yellow(string)
    True
    """
    return f"\u001b[33;1m{given_string}\u001b[0m"


def underline_string(given_string):
    """Return a string wrapped in ANSI escape code for underline.

    :param given_string: a string
    :return: a string

    >>> string = "NickFurry"
    >>> test_string = '\x1b[4mNickFurry\x1b[0m'
    >>> test_string == underline_string(string)
    True
    """
    return f"\033[4m{given_string}\u001b[0m"


def make_board() -> dict:
    """Generate game board as a dictionary.

    Function generates a dictionary with coordinate tuples as keys and location description as values.

    :return: dictionary with coordinate tuples as keys and location description as values
    """
    cycle_location = itertools.cycle(LOCATION_DESCRIPTION())
    board = {(row, column): {"location_description": next(cycle_location)} for row in range(BOARD_SIZE())
             for column in range(BOARD_SIZE())}
    return board


def input_checker(dict_of_options: dict) -> str:
    """Generate user choice from provided dictionary.

    The function will take the provided dictionary, and ask the user for input. It will then match the user input
    with the corresponding number so the user can choose by number.

    :param dict_of_options: a dictionary
    :precondition: the dictionary must have the correct key/value pair, where the key is a number and value is a string
    :postcondition: correctly matches the user choice for key and returns the corresponding value
    :return: value of the chosen key as a string
    """
    print(str(dict_of_options).replace(",", "\n"))
    user_input = input("\nPlease choose from the following list of options by typing in the corresponding number: \n")
    while (user_input.isnumeric() is False) or (int(user_input) not in dict_of_options):
        print("That's not in the list of options. Please choose again!")
        print(str(dict_of_options).replace(",", "\n"))
        user_input = input("\nPlease choose from the following list of options by typing in the corresponding "
                           "number: \n")
    return dict_of_options[int(user_input)]


def delayed_message(message: str, delay: float):
    """Add delays to string prints.

    :param message: a string
    :param delay: a number
    :precondition: delay has to be a positive number
    :postcondition: prints the message with delay correctly
    """
    print(message)
    sleep(delay)


def press_enter_to_continue():
    """Generate prompt to allow player to control the pace of the game.

    The function will ask user to type enter to continue. This allows the player to control the pace of the game,
    compared to determined delayed gameplay. The user can only type enter, and will not allow any other inputs.
    """
    user_input = input("\nPress enter to continue the game!: \n")
    while user_input != "":
        print("Please press enter!")
        user_input = input("Press enter to continue the game!: ")


def random_name_generator() -> str:
    """Generate random name.

    The function will generate a random name and the player has the choice to either keep the name, choose another name
    at random, or choose make own name.

    :return: user's choice in string
    """
    random_name = ' '.join(name.capitalize() for name in generate())
    print(f"{color_string_green(random_name)} was created randomly! Would you like to choose your own name or create"
          f" another at random?\n")
    choices = {int(keys): names for keys, names in enumerate(PLAYER_NAME_CHOICES(), 1)}
    user_choice = input_checker(choices)
    while user_choice == "I would like to choose another one at random":
        random_name = ' '.join(name.capitalize() for name in generate())
        print(f"\n{color_string_green(random_name)} was created randomly! Would you like to choose your own name or "
              f"create another at random?\n")
        user_choice = input_checker(choices)
    if user_choice == "I would like to choose this name!":
        user_choice = random_name
    return user_choice


def player_name_generator() -> str:
    """Create a name based on user input.

    :postcondition: gets user input and assigns it to variable
    :return: a string
    """
    user_input = random_name_generator()
    if user_input == "I would like to choose my own name!":
        user_input = input("What will your name be for this game?: ")
        while user_input == "":
            print("You can't have nothing for your name, but anything else works! Try again.")
            user_input = input("What will your name be for this game?: ")
    print(f"\nWelcome to the game, {color_string_green(user_input)}\n")
    sleep(1)
    return user_input


def player_class_generator(player: dict):
    """Designate player class based on user choice.

    :param player: a dictionary
    :precondition: dictionary should include a key called "class"
    :postcondition: correctly gets the user input and assigns a class to the player's dictionary
    :return: a string the player's selected class
    """
    print("Below is the list of characters you can choose to play in the game. Choose wisely so that you'll be able "
          "to win the game successfully... \n")
    choices = {int(keys): characters for keys, characters in zip(count(start=1, step=1), CLASS_LIST())}
    user_input = input_checker(choices)
    player["class"] = user_input
    print(f"\n{user_input} is a great choice!\n")
    sleep(1)


def player_class_dictionary(player: dict):
    """Change the "class_dictionary" value depending on player's class.

    The function will check the player's "class_dictionary" value based on the player's class choice.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with key "class_dictionary" and key "class"
    :postcondition: correctly change the "class_dictionary" value depending on the player's key "class"

    >>> player_info = {"class": "Mage", "experience": 500, "class_dictionary": ""}
    >>> player_class_dictionary(player_info)
    >>> print(player_info) #doctest: +NORMALIZE_WHITESPACE
    {'class': 'Mage', 'experience': 500, 'class_dictionary': {'level': 2, 'level_name': 'Mage',
    'experience_needed': 600, 'attack_name': 'Firestorm', 'max_hp': 25, 'base_damage_min': 20,
    'base_damage_max': 25, 'accuracy_rate': 55}, 'level': 2}
    """
    current_dictionary = return_class_dictionary(player)
    level = check_level(player)
    player["class_dictionary"] = current_dictionary[level]


def return_class_dictionary(player: dict) -> dict:
    """Return the class dictionary depending on user class.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with key "class"
    :postcondition: correctly return the corresponding class dictionary
    :return: a dictionary

    >>> player_info = {"class": "Thief"}
    >>> return_class_dictionary(player_info) #doctest: +NORMALIZE_WHITESPACE
    {1: {'level': 1, 'level_name': 'Apprentice Thief', 'experience_needed': 200, 'attack_name': 'Pickpocket',
    'max_hp': 20, 'base_damage_min': 5, 'base_damage_max': 10, 'accuracy_rate': 65}, 2: {'level': 2,
    'level_name': 'Bandit', 'experience_needed': 500, 'attack_name': 'Boomerang Step', 'max_hp': 40,
    'base_damage_min': 10, 'base_damage_max': 15, 'accuracy_rate': 75}, 3: {'level': 3, 'level_name': 'Hermit',
    'attack_name': 'Assassinate', 'max_hp': 60, 'base_damage_min': 10, 'base_damage_max': 15, 'accuracy_rate': 80}}
    """
    if player["class"] == "Mage":
        return MAGE()
    elif player["class"] == "Thief":
        return THIEF()
    elif player["class"] == "Ranger":
        return RANGER()
    else:
        return WARRIOR()


def check_level(player: dict) -> int:
    """Change the player's level depending on user experience, and return the level.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with key "experience" and key "class"
    :postcondition: correctly return the changed level
    :return: an integer

    >>> player_info = {"class": "Mage", "experience": 0}
    >>> check_level(player_info)
    1

    >>> player_info = {"class": "Mage", "experience": 500}
    >>> check_level(player_info)
    2

    >>> player_info = {"class": "Mage", "experience": 1000}
    >>> check_level(player_info)
    3
    """
    class_dictionary = return_class_dictionary(player)
    level = 1
    if player["experience"] >= class_dictionary[1]["experience_needed"]:
        level += 1
    if player["experience"] >= class_dictionary[2]["experience_needed"]:
        level += 1
    player["level"] = level
    return level


def make_player() -> dict:
    """Create a dictionary that contains player name, class, hp, position, player level/exp, category, and class
    dictionary.

    The function creates a dictionary from different inputs and constants.

    :postcondition: gets user input and creates player dictionary
    :return: a dictionary
    """
    player = {"name": color_string_green(player_name_generator()),
              "class": "",
              "hp": PLAYER_BASE_HP(),
              "position": PLAYER_STARTING_POSITION(),
              "level": 1,
              "experience": 0,
              "category": "player",
              "class_dictionary": ""}
    player_class_generator(player)
    player_class_dictionary(player)
    return player


def display_map(player: dict, boss: dict):
    """Print player's and boss' position on the map.

    Player's position will be printed as green, whereas the boss' position will be printed as red.

    :param player: a dictionary
    :param boss: a dictionary
    :precondition: player and boss must be a proper dictionary with the key "position"
    :precondition: player and boss position in the dictionary must be a list with two integer elements
    :postcondition: print the correct player's and boss' position on a correctly sized map
    """
    for row in range(BOARD_SIZE()):
        for column in range(BOARD_SIZE()):
            if player["position"] == [row, column]:
                print(color_string_green("[X]"), end="")
            elif boss["position"] == [row, column]:
                print(color_string_red("[#]"), end="")
            else:
                print("[ ]", end="")
        print()


def display_info(player: dict, board: dict):
    """Print player's position, location description, health point, level, class name, and experience point.

    :param player: a dictionary
    :param board: a dictionary
    :precondition: player and board must be a proper dictionary with correct character and information
    :postcondition: correctly prints the f strings of player position, location description, hp, level, class name,
    and experience
    """
    coordinate = player["position"]
    print(f'Location: {player["position"]}')
    print(f'Description: {board[tuple(coordinate)]["location_description"]}')
    print(f'Health point: {player["hp"]}/{player["class_dictionary"]["max_hp"]}')
    print(f'Level: {player["level"]}, {player["class_dictionary"]["level_name"]}')
    print(f'Experience: {player["experience"]}')


def player_movement_change(current_position: list, user_direction: str):
    """Change the current_position to the desired direction.

    :param current_position: a list
    :param user_direction: a string
    :precondition: the list must contain two numbers within the range of 0 and 4 inclusive
    :precondition: the string must be either "West", "East", "South", "North"
    :postcondition: the player's position will correctly change according to user_direction
    :return: a changed list of the player's new position

    >>> position = [2, 2]
    >>> direction = "West"
    >>> player_movement_change(position, direction)
    >>> position
    [2, 1]
    >>> position = [2, 2]
    >>> direction = "South"
    >>> player_movement_change(position, direction)
    >>> position
    [3, 2]
    """
    if user_direction == "West":
        current_position[1] -= 1
    elif user_direction == "East":
        current_position[1] += 1
    elif user_direction == "South":
        current_position[0] += 1
    elif user_direction == "North":
        current_position[0] -= 1
    else:
        game_over()


def filter_direction(valid_direction: dict) -> bool:
    """Return boolean True or False based on available directions.

    Function accepts a dictionary of direction and position of the player's x or y coordinate.
    If direction moves off the board, then return False, else True.

    :param valid_direction: a dictionary
    :precondition: a dictionary with directions as key and position as value
    :postcondition: correctly returns True if the direction is on the board, else False if direction is off the board
    :return: boolean True or False

    >>> direction = {"direction": "West", "position": 0}
    >>> filter_direction(direction)
    False

    >>> direction = {"direction": "North", "position": 0}
    >>> filter_direction(direction)
    False

    >>> direction = {"direction": "Quit", "position": 0}
    >>> filter_direction(direction)
    True
    """
    if valid_direction["direction"] == "West" and valid_direction["position"] == 0:
        return False
    elif valid_direction["direction"] == "East" and valid_direction["position"] == BOARD_SIZE() - 1:
        return False
    elif valid_direction["direction"] == "South" and valid_direction["position"] == BOARD_SIZE() - 1:
        return False
    elif valid_direction["direction"] == "North" and valid_direction["position"] == 0:
        return False
    else:
        return True


def change_dict_to_list(direction_dictionary: list) -> list:
    """Change dictionary values into a list.

    Function takes in a list with multiple dictionaries and generate a single list with key "direction" values.

    :param direction_dictionary: a list with multiple dictionaries within
    :precondition: direction_dictionary elements must be dictionaries with keys being "direction" and values being the
                   directions
    :postcondition: correctly returns a list of directions
    :return: a list with different directions

    >>> test_list = [{'direction': 'West'}, {'direction': 'East'}, {'direction': 'South'}, {'direction': 'Quit'}]
    >>> change_dict_to_list(test_list)
    ['West', 'East', 'South', 'Quit']
    """
    possible_directions_list = []
    for key_pair in direction_dictionary:
        possible_directions_list.append(key_pair["direction"])
    return possible_directions_list


def move_character(player: dict, board: dict, boss: dict):
    """Change the position of the player to a new position based on user input.

    :param player: a dictionary
    :param board: a dictionary
    :param boss: a dictionary
    :precondition: player, board, and boss must be a proper dictionary with correct character and information
    :postcondition: the player's position will correctly change according to the user's input
    :return: a changed player's new position in a list
    """
    display_map(player, boss)
    display_info(player, board)
    direction_validation = [{"direction": "West", "position": player["position"][1]},
                            {"direction": "East", "position": player["position"][1]},
                            {"direction": "South", "position": player["position"][0]},
                            {"direction": "North", "position": player["position"][0]},
                            {"direction": "Quit"}]
    possible_directions = list(filter(filter_direction, direction_validation))
    new_direction_list = {int(keys): jobs for keys, jobs in enumerate(change_dict_to_list(possible_directions), 1)}
    user_input = input_checker(new_direction_list)
    player_movement_change(player["position"], user_input)


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """Generate a sum of the number_of_rolls and their results.

    The function will roll a die a certain amount of times and generate a random number based on the number_of_sides
    given, then sum the total results.

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls and number_of_sides must be positive integers greater than 0
    :postcondition: a correct sum of each result
    :return: the sum of each result as an integer
    """
    total_result = 0
    for number in range(number_of_rolls):
        total_result += randint(1, number_of_sides)
    return total_result


def battle_chance(player: dict, monster: dict):
    """Roll a die to determine if the player will meet an enemy.

    The player has a 20% chance to meet an enemy everytime they move. This is determined by rolling a 5 sided die once,
    and if the rolled number is less than or equal to 1, it will lead to the combat_round function. Else, heal_player
    function.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly lead to corresponding functions depending on situation
    """
    battle_chance_number = roll_die(1, BATTLE_CHANCE_PROBABILITY())
    if battle_chance_number == 1:
        delayed_message("There's someone lurking in the dark!", 1)
        combat_round(player, monster)
    else:
        heal_player(player)


def heal_player(player: dict):
    """Increase player hp by integer 4.

    The function will heal the player's hp by integer 4. The heal amount will only be up to the player's maximum
    hp for the particular level.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly changes the value of player's hp
    :return: the changed hp value in the dictionary

    #heal player with low hp, healed amount should be 10
    >>> player_info = {'hp': 6, 'class_dictionary': {'max_hp': 20}}
    >>> heal_player(player_info)
    It seems like there's no one in the room. You are healed by 4 hp!
    <BLANKLINE>
    >>> player_info["hp"]
    10

    #heal player with high hp, healed amount should be 20
    >>> player_info = {'hp': 18, 'class_dictionary': {'max_hp': 20}}
    >>> heal_player(player_info)
    It seems like there's no one in the room. You are healed by 4 hp!
    <BLANKLINE>
    >>> player_info["hp"]
    20

    #heal player with different max hp, healed amount should be 22
    >>> player_info = {'hp': 18, 'class_dictionary': {'max_hp': 25}}
    >>> heal_player(player_info)
    It seems like there's no one in the room. You are healed by 4 hp!
    <BLANKLINE>
    >>> player_info["hp"]
    22
    """
    delayed_message("It seems like there's no one in the room. You are healed by 4 hp!\n", 1)
    if 0 <= player["hp"] <= player["class_dictionary"]["max_hp"]:
        player["hp"] += PLAYER_HEAL_HP()
        if player["hp"] > player["class_dictionary"]["max_hp"]:
            player["hp"] = player["class_dictionary"]["max_hp"]


def random_monster(player: dict) -> dict:
    """Create a dictionary of random monster, random monster type, and hp.

    The function will pick a random monster from a list of tuples. The player's dictionary is used to change monster
    damage and hp depending on player's level.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly chooses random name, type, and attacks and puts them into a monster dictionary
    :return: a dictionary
    """
    random_monster_name = choice(LIST_OF_MONSTERS())
    random_monster_type = choice(LIST_OF_MONSTER_TYPES())
    monster = {"name": color_string_yellow(random_monster_name),
               "type": random_monster_type,
               "hp": "",
               "category": "monster",
               "damage": "",
               "attack_name": LIST_OF_MONSTER_ATTACKS()}
    check_monster_hp_and_damage(player, monster)
    return monster


def check_monster_hp_and_damage(player, monster):
    """Updates monster hp and damage level depending on the level of the player.

    As the player levels up, the monster hp and damage amount also increases incrementally.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly updates the monster' "hp" and "damage" value in the monster's dictionary
    """
    player_current_level = check_level(player)
    monster_dictionary = MONSTER_HP_AND_DAMAGE()
    monster["hp"] = monster_dictionary[player_current_level]["hp"]
    monster["damage"] = randint(monster_dictionary[player_current_level]["min_damage"],
                                monster_dictionary[player_current_level]["max_damage"])


def fight_or_run_decision(monster: dict) -> str:
    """Return user choice for combat initiation when meeting an enemy.

    The function asks the player if they would like to fight when encountering an enemy.

    :param monster: a dictionary
    :precondition: monster must be a proper dictionary with correct character and information
    :postcondition: return the correct choice from the list of options, Yes or No
    :return: a string
    """
    print(f"\nYou have encountered {monster['name']}! Would you like to fight?\n")
    user_battle_decision = {int(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    return user_choice


def combat_round(player: dict, monster: dict):
    """Direct the player to different functions based on their input.

    This function gives the user an option to run or fight. Either options will send the user to other functions.
    The battle_start has a while loop implemented to keep the battle going until one of their hp values reach 0.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly leads to corresponding functions depending on situation
    """
    if fight_or_run_decision(monster) == "Yes":
        while player["hp"] > 0 and monster["hp"] > 0:
            battle_start(player, monster, battle_attack_order())
            if run_away_monster(monster, player) and (monster["hp"] > 0 and player["hp"] > 0):
                break
            if (monster["hp"] > 0 and player["hp"] > 0) and run_or_fight_again() == "No":
                run_away_player(player, monster)
                break
            else:
                continue
        press_enter_to_continue()
    else:
        run_away_player(player, monster)


def run_away_player(player: dict, monster: dict):
    """Roll a die to determine if the player will get damaged while fleeing.

    The player has a 20% chance to avoid damage while running away. This is determined by rolling a 5 sided die once,
    and if the rolled number is 1, player will be damaged. The damage amount will be determined by rolling a 4 sided die
    once, and the player hp is updated by the damage amount. Else, no damage taken while fleeing.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly changed hp depending on situation
    :return: changed player's hp value if attack is successful in a dictionary
    """
    run_away_number = roll_die(1, RUN_AWAY_PROBABILITY())
    if run_away_number == 1:
        run_away_damage = roll_die(1, RUN_AWAY_DAMAGE_RANGE())
        player["hp"] -= run_away_damage
        delayed_message(f"You've been damaged {underline_string(run_away_damage)} hp by {monster['name']} while "
                        f"running away!\nYou only have {player['hp']} hp left! Be careful {player['name']}!", 1)
    else:
        delayed_message(f"You've run away successfully from {monster['name']}!\n"
                        f"You were very lucky this time...\n", 1)


def run_or_fight_again() -> str:
    """Return the user choice for continuation of combat after one round.

    The function asks the player if they would like to continue fighting after every round.

    :postcondition: return the correct choice from the list of options, Yes or No
    :return: a string
    """
    print(f"\nWould you like to keep fighting?\n")
    user_battle_decision = {int(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    return user_choice


def run_away_monster(monster: dict, player: dict) -> bool:
    """Return boolean based on the monster and player hp value, or the result of roll_die.

    The function will first check if either characters are alive, if not, it will return False. If they are both alive,
    the function will roll a die to see if the monster has succeeded in running away from combat. The monster runaway
    chance will happen at the end of every round.

    :param monster: a dictionary
    :param player: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly return boolean value depending on situation
    :return: a boolean
    """
    if monster["hp"] < 1 or player["hp"] < 1:
        return False
    else:
        run_away_number = roll_die(1, RUN_AWAY_PROBABILITY())
        if run_away_number == 1:
            delayed_message(f"{monster['name']} ran away!", 1)
            return True
        else:
            return False


def battle_attack_order() -> bool:
    """Determine who will attack first.

    The function will roll a 100 sided die twice, and determine the attack order of the player and monster. The function
    has a while loop implemented, so it would keep rolling the dice if the roll results are the same. It will return
    a boolean value depending on who will attack first.

    :precondition: player and monster_info must be a proper dictionary with correct character and information
    :postcondition: return the correct boolean value determining the correct battle order and invoking the battle order
                    for the round
    :return: a boolean
    """
    delayed_message("Let's see who gets to attack first this round!\n", 0.5)
    user_initial_attack = roll_die(1, INITIAL_ATTACK_PROBABILITY())
    enemy_initial_attack = roll_die(1, INITIAL_ATTACK_PROBABILITY())
    while user_initial_attack == enemy_initial_attack:
        user_initial_attack = roll_die(1, INITIAL_ATTACK_PROBABILITY())
        enemy_initial_attack = roll_die(1, INITIAL_ATTACK_PROBABILITY())
    if user_initial_attack > enemy_initial_attack:
        return True
    else:
        return False


def battle_start(player: dict, monster: dict, attacker: bool):
    """Simulate a battle between two characters.

    The function identifies who attacks first based on the boolean value, if the opponent is still alive then the
    opponent will attack after. If the monster dies, then the leveling_package function runs to update player's
    information.

    :param player: a dictionary
    :param monster: a dictionary
    :param attacker: a boolean
    :precondition: player must be a dictionary with correct player information and with key "hp"
    :precondition: monster must be a dictionary with correct monster information and with key "hp" and "damage"
    :postcondition: correctly changes the "hp" of both characters if bother are alive
    :postcondition: correctly changes the "experience" and or "level" of player if kill monster
    """
    if attacker:
        attacking_round(player, monster, player_damage(player))
        if monster['hp'] > 0:
            attacking_round(monster, player, roll_die(1, monster["damage"]))
        else:
            player["experience"] += PLAYER_EXPERIENCE_GAIN()
    else:
        attacking_round(monster, player, roll_die(1, monster["damage"]))
        if player['hp'] > 0:
            attacking_round(player, monster, player_damage(player))
        if monster['hp'] < 1:
            player["experience"] += PLAYER_EXPERIENCE_GAIN()


def leveling_package(player: dict):
    """Change exp value and the player's dictionary values depending on the level.

    The function will add 100 exp everytime the monster is dead. The function will check the exp needed for each level
    to change the player's level and class_dictionary.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: add correct amount to player's experience points
    :postcondition: correctly change the player's level and class_dictionary based on experience accumulated

    >>> player_info = {'category': 'player', 'class': 'Warrior',
    ... 'class_dictionary': {'accuracy_rate': 50, 'attack_name': 'Threaten', 'base_damage_max': 12,
    ... 'base_damage_min': 7, 'experience_needed': 200, 'level': 1, 'level_name': 'Apprentice Warrior',
    ... 'max_hp': 20}, 'experience': 0, 'hp': 20, 'level': 1, 'name': 'Leo', 'position': [0, 0]}
    >>> leveling_package(player_info)
    >>> print(player_info) #doctest: +NORMALIZE_WHITESPACE
    {'category': 'player', 'class': 'Warrior', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
    'experience_needed': 400, 'attack_name': 'Threaten', 'max_hp': 20, 'base_damage_min': 5, 'base_damage_max': 10,
    'accuracy_rate': 50}, 'experience': 0, 'hp': 20, 'level': 1, 'name': 'Leo', 'position': [0, 0]}
    """
    check_level(player)
    player_class_dictionary(player)


def player_damage(player: dict) -> int:
    """Return player's damage for the round.

    The function first picks a random number to assess if the player successful in the attack depending on their
    accuracy rate. It will return 0 if they fail, otherwise, return the correct damage value.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with keys "class_dictionary", "accuracy_rate",
                   "base_damage_min", and "base_damage_max"
    :postcondition: return correct damage integer depending the dice roll result
    :return: zero or a positive integer
    """
    accuracy_roll = randint(1, 101)
    if accuracy_roll <= player["class_dictionary"]["accuracy_rate"]:
        damage = randint(player["class_dictionary"]["base_damage_min"],
                         player["class_dictionary"]["base_damage_max"])
    else:
        damage = 0
    return damage


def attacking_round(attacker: dict, opponent: dict, damage_amount: int):
    """Simulate a single attack to the opponent.

    This function runs a combat simulation that changes the opponent's hp value.

    :param attacker: a dictionary
    :param opponent: a dictionary
    :param damage_amount: an integer
    :precondition: attacker must be a dictionary with key "name"
    :precondition: opponent must be a dictionary with key "name" and key "hp"
    :precondition: damage_amount must be an zero or positive integer
    :postcondition: correctly change "hp" value of the opponent in a dictionary
    :return: changed hp value of opponent in a dictionary

    >>> player_info = {"name": "Leo"}
    >>> monster_info = {"name": "Zelda", "hp": 10}
    >>> attacking_round(player_info, monster_info, 0)
    <BLANKLINE>
    Leo has missed the attack!
    <BLANKLINE>

    >>> player_info = {"name": "Leo", "category": "player", 'class_dictionary': {'attack_name': 'Pet the head'}}
    >>> monster_info = {"name": "Zelda", "hp": 10, "category": "monster", 'attack_name': 'Scratch'}
    >>> attacking_round(player_info, monster_info, 5)
    Leo has used Pet the head and has done \033[4m5\u001b[0m damage to Zelda!
    Zelda has 5 hp left!
    <BLANKLINE>
    """
    if damage_amount == 0:
        delayed_message(f"\n{attacker['name']} has missed the attack!\n", 0.5)
    else:
        if attacker['category'] == 'player':
            opponent['hp'] -= damage_amount
            delayed_message(f"{attacker['name']} has used {attacker['class_dictionary']['attack_name']} "
                            f"and has done {underline_string(damage_amount)} damage to {opponent['name']}!"
                            f"\n{opponent['name']} has {opponent['hp']} hp left!\n", 0.5)
        else:
            opponent['hp'] -= damage_amount
            delayed_message(f"{attacker['name']} has used {choice(attacker['attack_name'])} and "
                            f"has done {underline_string(damage_amount)} damage to {opponent['name']}!"
                            f"\n{opponent['name']} has {opponent['hp']} hp left!\n", 0.5)


def make_boss() -> dict:
    """Create a dictionary of boss that contain boss name, hp, damage, and position.

    The function creates a dictionary from different constants.

    :return: a dictionary
    """
    boss_name = choice(LIST_OF_BOSS_NAME())
    boss = {"name": color_string_red(boss_name),
            "category": "boss",
            "hp": BOSS_MAX_HP(),
            "damage": BOSS_MAX_DAMAGE(),
            "position": BOSS_POSITION(),
            "attack_name": RANDOM_BOSS_ATTACK()}
    return boss


def fight_or_run_decision_boss_round(boss: dict) -> str:
    """Return user choice for combat initiation when meeting boss.

    The function asks the player if they would like to fight when encountering the boss. This has a different prompt
    than the regular decision making function to give the player more detail about the boss round.

    :param boss: a dictionary
    :precondition: boss must be a proper dictionary with correct character and information
    :postcondition: return the correct choice from the list of options
    :return: a string
    """
    delayed_message(f"\nYou have encountered {boss['name']}!\nThe boss hp is {boss['hp']}, and the damage is "
                    f"{boss['damage']}.\nIf you beat him, you will finish the game with a victory, if you fail however,"
                    f" the game will be finished.\nYou can choose to run away anytime you'd like and come back when you"
                    f" believe you are ready to defeat the boss!\n", 1)
    delayed_message(f"\nWould you like to fight?\n(We recommend going up against the boss at level 3, as you will have"
                    f" higher chances of winning)", 1)
    user_battle_decision = {int(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    return user_choice


def fight_boss(player: dict, boss: dict):
    """Direct the user to different functions based on their input.

    This function will give the user an option to run or fight when meeting boss. Either options will send the user to
    other functions. The fight_boss has a while loop implemented to keep the battle going until one of their hp values
    reach 0.

    :param player: a dictionary
    :param boss: a dictionary
    :precondition: player and boss must be a proper dictionary with correct character and information
    :postcondition: correctly leads to corresponding functions depending on situation
    """
    if fight_or_run_decision_boss_round(boss) == "Yes":
        while player["hp"] > 0 and boss["hp"] > 0:
            battle_start(player, boss, battle_attack_order())
            if (boss["hp"] > 0 and player["hp"] > 0) and run_or_fight_again() == "No":
                run_away_player(player, boss)
                boss["hp"] = BOSS_MAX_HP()
                break
            else:
                continue
        press_enter_to_continue()
    else:
        run_away_player(player, boss)


def game_over():
    """Print ASCII art to end the game.

    The function will run when the player chooses "quit" in move_character function. It will use the art module to
    print out the string as ASCII art, and then terminate.
    """
    art.tprint("\n\n\nThanks for playing!\nSee you later!")
    input("\nType anything and press enter to close the game!")
    quit()


def game_win_art():
    """Print ASCII art to congratulate the player for winning the game.

    The function will run when the player succeeds in defeating the boss. It will use the art module to print out the
    string as ASCII art, and then terminate.
    """
    art.tprint("\n\n\nCongrats!\nYou've won!")
    input("\nType anything and press enter to close the game!")
    quit()


def player_dead_art():
    """Print ASCII art to notify the player when they are dead.

    The function will run when the player is dead at any point in game. It will use the art module to print out the
    string as ASCII art, and then terminate.
    """
    art.tprint("\n\n\nOh no!\nYou're dead!\nTry again!")
    input("\nType anything and press enter to close the game!")
    quit()


def game():
    """Execute the game.

    The function consists of all the functions previously written. It runs a while loop to continue the game until the
    player types "quit" or achieves the goal of beating the boss.
    """
    print("""
    Welcome player, I hope you are ready for an epic adventure! There's nothing too difficult about navigating
    around the game. Keep in mind that you will only be allowed to input numbers that correspond to the items. If you
    choose the option "quit" when prompted to move, the game will end. The game will end if your hp reaches 0 or if you
    defeat the boss.\n
    The monsters have a chance to run after each round, and you will also have a change to run after every round as
    well\n
    Once you reach the boss location, you will be prompted to the boss round. Although the boss will not be able to
    run, you have an option to run after each round. If you decide to leave and come back, the boss hp will be
    refreshed to the max when you come back.\n
    I wish you the best of luck!\n\n\n""")
    board = make_board()
    player = make_player()
    boss = make_boss()
    while player["hp"] > 0 and boss["hp"] > 0:
        leveling_package(player)
        move_character(player, board, boss)
        if player["position"] == boss["position"]:
            fight_boss(player, boss)
        else:
            battle_chance(player, random_monster(player))
    if boss["hp"] < 1:
        game_win_art()
    player_dead_art()


def main():
    """Execute the program"""
    should_run_doctest = os.getenv("RUN_DOCTEST")
    if should_run_doctest:
        doctest.testmod(verbose=True)
    os.system("")
    game()


if __name__ == "__main__":
    main()

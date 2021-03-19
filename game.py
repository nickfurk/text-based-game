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
from functools import partial
from colorama import init, Fore, Style
from typing import Union


# Player Specifications
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


# Class Specification
def MAGE_HP_INCREMENT() -> int:
    """Return Mage class health increment as 10.

    :return: Mage class health point increment as integer 10
    """
    return 10


def THIEF_HP_INCREMENT() -> int:
    """Return Thief class health increment as 10.

    :return: Thief class health point increment as integer 10
    """
    return 10


def RANGER_HP_INCREMENT() -> int:
    """Return Ranger class health increment as 10.

    :return: Ranger class health point increment as integer 10
    """
    return 10


def WARRIOR_HP_INCREMENT() -> int:
    """Return Warrior class health increment as 10.

    :return: Warrior class health point increment as integer 10
    """
    return 10


def MAGE() -> dict:
    """Return Mage class dictionary.

    The key represents the player's level, which changes the specifications when the player levels up.
    Each level indicates it own specifications including level name, experience required to level up,
    attack names available per level, player's max HP, player's minimum and maximum damage amount,
    and the player's accuracy rate for the respective level.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Mage", "experience_needed": 500, "attack_name": "Fireball",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 15, "base_damage_max": 20, "accuracy_rate": 25},
        2: {"level": 2, "level_name": "Mage", "experience_needed": 1000, "attack_name": "Firestorm",
            "max_hp": PLAYER_BASE_HP() + MAGE_HP_INCREMENT(), "base_damage_min": 20, "base_damage_max": 25,
            "accuracy_rate": 40},
        3: {"level": 3, "level_name": "Arch Mage", "attack_name": "Hellfire",
            "max_hp": PLAYER_BASE_HP() + (MAGE_HP_INCREMENT() * 2), "base_damage_min": 25, "base_damage_max": 30,
            "accuracy_rate": 50}
    }


def THIEF() -> dict:
    """Return Thief class dictionary.

    The key represents the player's level, which changes the specifications when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Thief", "experience_needed": 100, "attack_name": "Pickpocket",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 1, "base_damage_max": 5, "accuracy_rate": 85},
        2: {"level": 2, "level_name": "Bandit", "experience_needed": 300, "attack_name": "Boomerang Step",
            "max_hp": PLAYER_BASE_HP() + THIEF_HP_INCREMENT(), "base_damage_min": 5, "base_damage_max": 10,
            "accuracy_rate": 95},
        3: {"level": 3, "level_name": "Hermit", "attack_name": "Assassinate",
            "max_hp": PLAYER_BASE_HP() + (THIEF_HP_INCREMENT() * 2), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 100}
    }


def RANGER() -> dict:
    """Return Ranger class dictionary.

    The key represents the player's level, which changes the specifications when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Ranger", "experience_needed": 500, "attack_name": "Iron Arrow",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 5, "base_damage_max": 10, "accuracy_rate": 50},
        2: {"level": 2, "level_name": "Sniper", "experience_needed": 1000, "attack_name": "Mortal Blow",
            "max_hp": PLAYER_BASE_HP() + RANGER_HP_INCREMENT(), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 60},
        3: {"level": 3, "level_name": "Marksman", "attack_name": "Dragon's Breath",
            "max_hp": PLAYER_BASE_HP() + (RANGER_HP_INCREMENT() * 2), "base_damage_min": 15, "base_damage_max": 20,
            "accuracy_rate": 75}
    }


def WARRIOR() -> dict:
    """Return Warrior class dictionary.

    The key represents the player's level, which change the player's status when they level up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "level_name": "Apprentice Warrior", "experience_needed": 200, "attack_name": "Threaten",
            "max_hp": PLAYER_BASE_HP(), "base_damage_min": 7, "base_damage_max": 12, "accuracy_rate": 50},
        2: {"level": 2, "level_name": "Knight", "experience_needed": 1000, "attack_name": "Power Crash",
            "max_hp": PLAYER_BASE_HP() + WARRIOR_HP_INCREMENT(), "base_damage_min": 12, "base_damage_max": 18,
            "accuracy_rate": 50},
        3: {"level": 3, "level_name": "Paladin", "attack_name": "Heaven's Hammer",
            "max_hp": PLAYER_BASE_HP() + (WARRIOR_HP_INCREMENT() * 2), "base_damage_min": 18, "base_damage_max": 24,
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
    return 5


def MONSTER_HP() -> dict:
    """Return monster health point dictionary.

    The key represents the player's level, and the value is a dictionary that indicates the monster new health point
    when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "hp": BASE_MONSTER_HP()},
        2: {"level": 2, "hp": BASE_MONSTER_HP() + MONSTER_HP_INCREMENT()},
        3: {"level": 3, "hp": BASE_MONSTER_HP() + (MONSTER_HP_INCREMENT() * 2)}
    }


def MONSTER_BASE_DAMAGE() -> int:  # need to get rid of at the end
    """Return monster's base damage as 10.

    The number is used in the roll_die function to give an output of 1 - 10 inclusive.

    :return: Monster's base damage as an integer 10
    """
    return 10


def MONSTER_DAMAGE_INCREMENT() -> int:
    """Return the monster's damage increment as 5.

    :return: Monster's damage increment as an integer 5
    """
    return 5


def MONSTER_DAMAGE() -> dict:
    """Return monster damage dictionary.

    The key represents the player's level, and the value is a dictionary that indicates the monster's new damage limit
    when the player levels up.

    :return: a dictionary
    """
    return {
        1: {"level": 1, "damage": MONSTER_BASE_DAMAGE()},
        2: {"level": 2, "damage": MONSTER_BASE_DAMAGE() + MONSTER_DAMAGE_INCREMENT()},
        3: {"level": 3, "damage": MONSTER_BASE_DAMAGE() + (MONSTER_DAMAGE_INCREMENT() * 2)},
    }


# Boss Specifications
def PICK_RANDOM_BOSS_NAME() -> str:
    """Return a random string from the list of strings.

    The function will pick a random name from the provided list of boss names.

    :return: a string
    """
    boss_names = ["Boss Zelda", "Boss Link", "Boss Bowser"]
    return choice(boss_names)


def BOSS_MAX_HP() -> int:
    """Return boss health point as 30.

    :return: an integer 30
    """
    return 30


def BOSS_MAX_DAMAGE() -> int:
    """Return boss damage as 10.

    :return: an integer 10
    """
    return 10


def BOSS_POSITION() -> list:
    """Return boss' fixed position as [25, 25]

    :return: a list with two number elements
    """
    return [15, 15]


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


def BATTLE_CHANCE() -> int:
    """Return the probability of encountering an enemy upon movement.

    The number is used in the roll_die function to simulate a 20% chance.

    :return: an integer 5
    """
    return 2


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


def DIRECTION_LIST() -> list:
    """Return the list of possible direction choices.

    The list is put through the input checker function to allow the player to choose.

    :return: a list
    """
    return ["W", "E", "S", "N", "quit"]


def YES_OR_NO() -> list:
    """Return a Yes or No list.

    The list is put through the input checker function to allow the player to choose.

    :return: a list
    """
    return ["Yes", "No"]


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


def make_board() -> dict:
    """Generate game board as a dictionary.

    Function generates a dictionary with coordinate tuples as keys and location description as values.

    :return: dictionary with coordinate tuples as keys and location description as values
    """
    location_description = [
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
    cycle_location = itertools.cycle(location_description)
    board = {(row, column): {"location_description": next(cycle_location)} for row in range(BOARD_SIZE())
             for column in range(BOARD_SIZE())}
    return board


def input_checker(list_of_options: dict) -> str:
    """Generate user choice from provided dictionary.

    The function will take the provided dictionary, and ask the user for input. It will then match the user input
    with the corresponding number so the user can choose by number.

    :param list_of_options: a dictionary
    :precondition: the dictionary must have the correct key/value pair, where the key is a number and value is a string
    :postcondition: correctly matches the user choice for key and returns the corresponding value
    :return: value of the chosen key as a string
    """
    print(str(list_of_options).replace(",", "\n"))
    user_input = input("\nPlease choose from the following list of options by typing in the corresponding number: \n")
    for keys, values in list_of_options.items():
        if user_input == keys:
            user_choice = values
            return user_choice


def delayed_message(message: str, delay: float) -> None:
    """Add delays to string prints.

    :param message: a string
    :param delay: a number
    :precondition: delay has to be a positive number
    :postcondition: prints the message with delay correctly
    """
    sleep(delay)
    print(message)


def press_enter_to_continue() -> None:
    """Generate prompt to allow player to control the pace of the game.

    The function will ask user to type enter to continue. This allows the player to control the pace of the game,
    compared to determined delayed gameplay. The user can only type enter, and will not allow any other inputs.
    """
    user_input = input("\nPress enter to continue the game!: \n")
    while user_input != "":
        print("Please press enter!")
        user_input = input("Press enter to continue the game!: ")


def game_over() -> None:
    """Generate a prompt to end the game."""
    print("\nThanks for playing! The game is over, goodbye!")
    input("Press enter to end the game :)")
    quit()


def player_name_generator() -> str:
    """Create a name based on user input.

    :postcondition: gets user input and assigns it to variable
    :return: a string
    """
    user_input = input("What will your name be for this game?: ")
    capitalized_input = user_input.title()
    while capitalized_input == "":
        print("You can't have nothing for your name, but anything else works! Try again.")
        user_input = input("What will your name be for this game?: ")
    print(f"\nWelcome to the game, {capitalized_input}. \n")
    sleep(1)
    return capitalized_input


def player_class_generator(player: dict) -> str:
    """Designate player class based on user choice.

    :param player: a dictionary
    :precondition: dictionary should include a key called "class"
    :postcondition: correctly gets the user input and assigns a class to the player's dictionary
    :return: a string the player's selected class
    """
    print("Below is the list of characters you can choose to play in the game. Choose wisely so that you'll be able "
          "to win the game successfully... \n")
    new_list_for_user = {str(keys): characters for keys, characters in zip(count(start=1, step=1), CLASS_LIST())}
    player_class = input_checker(new_list_for_user)
    while player_class not in CLASS_LIST():
        print("That's not in the list of jobs you can choose from!")
        player_class = input_checker(new_list_for_user)
    player["class"] = player_class
    delayed_message(f"\n{player_class} is a great choice!\n", 0.75)
    return player_class


def player_class_dictionary(player: dict) -> None:
    """Change the class_dictionary depending on player's level.

    The function will check the player's current level and change the class_dictionary accordingly.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly change the class_dictionary depending on player's level
    """
    current_dictionary = return_class_dictionary(player)
    level = check_level(player)
    player["class_dictionary"] = current_dictionary[level]


def return_class_dictionary(player: dict) -> dict:
    """Return the class dictionary depending on user class.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly return the corresponding class dictionary
    :return: a dictionary
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
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly return the changed level
    :return: an integer
    """
    class_dictionary = return_class_dictionary(player)
    level = 1
    if player["experience"] >= class_dictionary[1]["experience_needed"]:
        level += 1
    elif player["experience"] >= class_dictionary[2]["experience_needed"]:
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
    player = {"name": player_name_generator(),
              "class": "",
              "hp": PLAYER_BASE_HP(),
              "position": PLAYER_STARTING_POSITION(),
              "level": 1,
              "experience": 0,
              "category": "player",
              "class_dictionary": ""}
    player["class"] = player_class_generator(player)
    player_class_dictionary(player)
    return player


def display_map(player: dict, boss: dict) -> None:
    """Print player's position on a map.

    :param player: a dictionary
    :param boss: a dictionary
    :precondition: player and boss must be a proper dictionary with correct character and information
    :precondition: player position in the dictionary must be a list
    :return: print player's position on a map
    """
    for row in range(BOARD_SIZE()):
        for column in range(BOARD_SIZE()):
            if player["position"] == [row, column]:
                print(Fore.GREEN + "[X]" + Style.RESET_ALL, end="")
            elif boss["position"] == [row, column]:
                print(Fore.RED + "[#]" + Style.RESET_ALL, end="")
            else:
                print("[ ]", end="")
        print()


def filter_information(player: dict, items: str) -> tuple:
    """Filter player dictionary by the items string.

    The function is used for filtering through taking the parameter, items, and matching with the keys in player to
    return the correct key/value pairs from the dictionary.

    :param player: a dictionary
    :param items: a string
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly returns the correct filtered elements
    :return: the correct filtered elements in a tuple
    """
    return player[0] == items


def display_info(player: dict, board: dict) -> None:
    """Print player's position, location description, health point, level, class name, and experience point.

    :param player: a dictionary
    :param board: a dictionary
    :precondition: player and board must be a proper dictionary with correct character and information
    :postcondition: correctly prints the f strings of player position, location description, hp, level, class name,
    and exp
    """
    coordinate = player["position"]
    print(f'Location: {list(filter(partial(filter_information, items="position"), player.items()))[0][1]}')
    print(f'Description: {board[tuple(coordinate)]["location_description"]}')
    print(f'Health point: {list(filter(partial(filter_information, items="hp"), player.items()))[0][1]}'
          f'/{list(filter(partial(filter_information, items="class_dictionary"), player.items()))[0][1]["max_hp"]}')
    print(f'Level: {list(filter(partial(filter_information, items="level"), player.items()))[0][1]}, '
          f'{list(filter(partial(filter_information, items="class_dictionary"), player.items()))[0][1]["level_name"]}')
    print(f'Experience: {list(filter(partial(filter_information, items="level"), player.items()))[0][1]}')


# #testing function
# player_test = {"position": (2, 2), "description": "huanted room", "hp": 30, "level": 2, "experience": 800}
# print(display_info(player_test, make_board()))


def validate_move(current_position: list, user_direction: str) -> bool:
    """Determine if user_direction is possible from the current_position.

    The player will not be able to go outside the map, and the function will validate whether the desired movement is
    within the boundaries of the map. The directions will be chosen through numbers, where "W", "E", "S", and "N" or
    "quit" to end the game.

    :param current_position: a list
    :param user_direction: a string
    :precondition: the list must contain two numbers within the range of 0 and 4 inclusive
    :precondition: the string must be either "W", "E", "S", "N", "quit"
    :postcondition: correctly determine if the user_direction is possible
    :return: a boolean that determines if the user_direction is possible

    >>> position = [0, 0]
    >>> direction = "E"
    >>> validate_move(position, direction)
    False
    >>> position = [0, 0]
    >>> direction = "W"
    >>> validate_move(position, direction)
    True
    >>> position = [0, 0]
    >>> direction = "N"
    >>> validate_move(position, direction)
    True
    >>> position = [0, 1]
    >>> direction = "quit"
    >>> validate_move(position, direction)
    False
    """
    if user_direction == "W" and current_position[1] == 0:
        return True
    elif user_direction == "E" and current_position[1] == 24:
        return True
    elif user_direction == "S" and current_position[0] == 24:
        return True
    elif user_direction == "N" and current_position[0] == 0:
        return True
    else:
        return False


def player_movement_change(current_position: list, user_direction: str) -> Union[list, None]:
    """Change the current_position to the desired direction.

    :param current_position: a list
    :param user_direction: a string
    :precondition: the list must contain two numbers within the range of 0 and 4 inclusive
    :precondition: the string must be either "W", "E", "S", "N"
    :postcondition: the player's position will correctly change according to user_direction
    :return: a changed list of the player's new position

    >>> position = [0, 0]
    >>> direction = "E"
    >>> player_movement_change(position, direction)
    [0, 1]
    >>> position = [0, 0]
    >>> direction = "S"
    >>> player_movement_change(position, direction)
    [1, 0]
    """
    if user_direction == "W":
        current_position[1] -= 1
        return current_position
    elif user_direction == "E":
        current_position[1] += 1
        return current_position
    elif user_direction == "S":
        current_position[0] += 1
        return current_position
    elif user_direction == "N":
        current_position[0] -= 1
        return current_position
    else:
        game_over()


def move_character(player: dict, board: dict, boss: dict) -> list:
    """Change the position of the player to a new position based on user input.

    :param player: a dictionary
    :param board: a dictionary
    :param boss: a dictionary
    :precondition: player, board, and boss must be a proper dictionary with correct character and information
    :postcondition: the player's position will correctly change according to user input
    :return: a changed player's new position in a list
    """
    player_game_descriptions(player, board, boss)
    if player["hp"] > 0:
        new_direction_list = {str(keys): jobs for keys, jobs in enumerate(DIRECTION_LIST(), 1)}
        user_input = input_checker(new_direction_list)
        while user_input not in DIRECTION_LIST() or validate_move(player['position'], user_input):
            print("\nYou can't go that way! Choose again wisely.")
            user_input = input_checker(new_direction_list)
        player_movement_change(player["position"], user_input)
        return player["position"]


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


def battle_chance(player: dict, monster: dict) -> None:
    """Roll a die to determine if the player will meet an enemy.

    The player has a 40% chance to meet an enemy everytime they move. This is determined by rolling a 10 sided die once,
    and if the rolled number is less than or equal to 4, it will lead to the combat_round function. Else, heal_player
    function.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly lead to corresponding functions depending on situation
    """
    battle_chance_number = roll_die(1, BATTLE_CHANCE())
    if battle_chance_number == 1:
        delayed_message("There's someone lurking in the dark!", 1)
        combat_round(player, monster)
    else:
        heal_player(player)


def heal_player(player: dict) -> None:
    """Update character_info based on their current hp.

    The function will heal the player's hp based on their current amount. The heal amount will only be up to the
    player's maximum hp which increases every level.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly changes the value of character's hp
    :return: the changed hp value in the dictionary

    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 10, "position": [1, 2], "level": {"level": 1, "exp": 0},
     "damage": 10, "run_away_chance": 3}
    >>> heal_player(players)
    >>> players["hp"]
    14
    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 18, "position": [1, 2], "level": {"level": 1, "exp": 0},
     "damage": 10, "run_away_chance": 3}
    >>> heal_player(players)
    >>> players["hp"]
    20
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
    :postcondition: correctly chooses random elements and puts them into a dictionary
    :return: a dictionary
    """
    random_monster_name = choice(LIST_OF_MONSTERS())
    random_monster_type = choice(LIST_OF_MONSTER_TYPES())
    monster = {"name": random_monster_name,
               "type": random_monster_type,
               "hp": "",
               "category": "monster",
               "damage": ""}
    check_monster_hp(player, monster)
    check_monster_damage(player, monster)
    return monster


def check_monster_hp(player: dict, monster: dict) -> None:
    """Check the player level to change the maximum monster hp.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly change the monster's hp value
    """
    player_current_level = check_level(player)
    monster_hp_dictionary = MONSTER_HP()
    monster["hp"] = monster_hp_dictionary[player_current_level]["hp"]


def check_monster_damage(player: dict, monster: dict) -> None:
    """Check the player level to change the maximum monster damage.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly change the monster's maximum damage value
    """
    player_current_level = check_level(player)
    monster_damage_dictionary = MONSTER_DAMAGE()
    monster["damage"] = monster_damage_dictionary[player_current_level]["damage"]


def fight_or_run_decision(monster: dict) -> str:
    """Return user choice for combat initiation when meeting enemy.

    The function asks the player if they would like to fight when encountering an enemy.

    :param monster: a dictionary
    :precondition: monster must be a proper dictionary with correct character and information
    :postcondition: return the correct choice from the list of options
    :return: a string
    """
    print(f"\nYou have encountered {monster['name']}! Would you like to fight?\n")
    user_battle_decision = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    while user_choice not in YES_OR_NO():
        print(f"{user_choice} is not a valid choice!, Please choose again: ")
        user_choice = input_checker(user_battle_decision)
    return user_choice


def combat_round(player: dict, monster: dict) -> Union[dict, None]:
    """Direct the user to different functions based on their input.

    This function will give the user an option to run or fight. Either options will send the user to other functions.
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
                return player
            elif monster["hp"] > 0 and player["hp"] > 0:
                if run_or_fight_again() == "No":
                    run_away_player(player, monster)
                    return player
                else:
                    continue
            elif monster["hp"] < 1 and player["hp"] > 0:
                continue
        press_enter_to_continue()
    else:
        run_away_player(player, monster)


def run_away_player(player: dict, monster: dict) -> dict:
    """Roll a die to determine if the player will get damaged while fleeing.

    The player has a 20% chance to avoid damage while running away. This is determined by rolling a 5 sided die once,
    and if the rolled number is 1, they will be damaged. The damage amount will be determined by rolling a 4 sided die
    once, and the player hp is updated by the damage amount. Else, no damage taken while fleeing.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player and monster must be a proper dictionary with correct character and information
    :postcondition: correctly changed hp depending on situation
    :return: changed player's hp value if attack is successful in a dictionary

    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 10, "position": [1, 2], "level": {"level": 1, "exp": 0},
     "damage": 10, "run_away_chance": 3}
    >>> monster_info = {"name": "Fallen Shamen", "type": "Ureh Caverns", "hp": 10, "damage": 10}
    >>> run_away_player(players, monster)
    >>> run_away_number == 1
    >>> players["hp"] < 10
    True
    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 14, "position": [1, 2], "level": {"level": 1, "exp": 0},
     "damage": 10, "run_away_chance": 3}
    >>> monster_info = {"name": "Fallen Shamen", "type": "Ureh Caverns", "hp": 10, "damage": 10}
    >>> run_away_player(players, monster)
    >>> run_away_number == 3
    >>> players["hp"] == 14
    True
    """
    run_away_number = roll_die(1, RUN_AWAY_PROBABILITY())
    if run_away_number == 1:
        run_away_damage = roll_die(1, RUN_AWAY_DAMAGE_RANGE())
        player["hp"] -= run_away_damage
        delayed_message(f"You've been damaged {run_away_damage} hp by {monster['name']} while running away!"
                        f"\nYou only have{player['hp']} hp left! Be careful {player['name']}!", 1)
        press_enter_to_continue()
        return player
    else:
        delayed_message(f"You've run away successfully from {monster['name']}!\n"
                        f"You were very lucky this time...\n", 1)
        press_enter_to_continue()
        return player


def run_or_fight_again() -> str:
    """Return the user choice for continuation of combat after rounds.

    The function asks the player if they would like to continue fighting after every round.

    :postcondition: return the correct choice from the list of options
    :return: a string
    """
    print(f"\nWould you like to keep fighting?\n")
    user_battle_decision = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    while user_choice not in YES_OR_NO():
        print(f"{user_choice} is not a valid choice!, Please choose again: ")
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
    if monster["hp"] < 1:
        return False
    elif player["hp"] < 1:
        return False
    else:
        run_away_number = roll_die(1, RUN_AWAY_PROBABILITY())
        if run_away_number == 1:
            delayed_message(f"{monster['name']} ran away!", 1)
            press_enter_to_continue()
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


def battle_start(player: dict, monster: dict, attacker: bool) -> None:
    """Simulate a battle between two characters.

    The function identifies the player through attacker boolean value, then runs the attacking_round in a correct order,
    and also implementing the correct damage amount. If the monster dies, it will also run the leveling_package function
    to change the player's information.

    :param player: a dictionary
    :param monster: a dictionary
    :param attacker: a boolean
    :precondition: first_attack and second_attack must be a proper dictionary with correct character and information
    :postcondition: correctly continue to run the round until one of the characters are dead
    :postcondition: correctly lead to leveling_package if the monster is dead
    """
    if attacker:
        attacking_round(player, monster, player_damage(player))
        if monster['hp'] > 0:
            attacking_round(monster, player, roll_die(1, monster["damage"]))
        else:
            leveling_package(player)
    elif attacker is False:
        attacking_round(monster, player, roll_die(1, monster["damage"]))
        if player['hp'] > 0:
            attacking_round(player, monster, player_damage(player))
        if monster['hp'] < 1:
            leveling_package(player)


def leveling_package(player: dict) -> None:
    """Change exp value and the player's dictionary values depending on the level.

    The function will add 100 exp everytime the monster is dead. The function will check the exp needed for each level
    to change the player's level and class_dictionary.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: add correct amount to player's experience points
    :postcondition: correctly change the player's level and class_dictionary based on experience accumulated
    """
    player["experience"] += 100
    check_level(player)
    player_class_dictionary(player)


def player_damage(player: dict) -> int:
    """Return player's damage for the round.

    The function first picks a random number to assess if the player succeeded in the attack depending on their accuracy
    rates. It will return 0 if they fail, otherwise, the correct damage value depending on situation.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correct damage number depending on situation
    :return: an integer
    """
    accuracy_roll = randint(1, 100)
    if accuracy_roll <= player["class_dictionary"]["accuracy_rate"]:
        damage = randint(player["class_dictionary"]["base_damage_min"],
                         player["class_dictionary"]["base_damage_max"])
    else:
        damage = 0
    return damage


def attacking_round(attacker: dict, opponent: dict, damage_amount: int) -> dict:
    """Simulate a single attack to the opponent.

    This function runs a combat simulation that changes the opponent's hp value.

    :param attacker: a dictionary
    :param opponent: a dictionary
    :param damage_amount: an integer
    :precondition: attacker and damaged must be a proper dictionary with correct character and information
    :precondition: damage_amount must be a positive integer
    :postcondition: correctly changed hp of opponent
    :return: changed hp value of opponent in a dictionary
    """
    if damage_amount == 0:
        delayed_message(f"\n{attacker['name']} has missed the attack!\n", 0.5)
    else:
        opponent['hp'] -= damage_amount
        delayed_message(f"{attacker['name']} has done {damage_amount} damage to {opponent['name']}!"
                        f"\n{opponent['name']} has {opponent['hp']} hp left!\n", 0.5)
    return opponent


def player_game_descriptions(player: dict, board: dict, boss: dict) -> None:
    """Direct to different functions that return game information for player.

    The function packages different helper functions that return different game information for player. The function is
    used to help distinguish which functions are being called to give the player game information.

    :param player: a dictionary
    :param board: a dictionary
    :param boss: a dictionary
    :precondition: player, board, and boss must be a proper dictionary with correct character and information
    :postcondition: correctly run different functions that return game information
    """
    display_map(player, boss)
    display_info(player, board)


def make_boss() -> dict:
    """Create a dictionary of boss that contain boss name, hp, damage, and position.

    The function creates a dictionary from different constants.

    :return: a dictionary
    """
    boss = {"name": PICK_RANDOM_BOSS_NAME(),
            "hp": BOSS_MAX_HP(),
            "damage": BOSS_MAX_DAMAGE(),
            "position": BOSS_POSITION()}
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
                    f"the game will be finished.\nYou can choose to run away anytime you'd like and come back when you"
                    f"believe you are ready to defeat the boss!\n", 1)
    delayed_message(f"\nWould you like to fight?\n(We recommend going up against the boss at level 3, as you will have"
                    f"higher chances of winning)", 1)
    user_battle_decision = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    while user_choice not in YES_OR_NO():
        print(f"{user_choice} is not a valid choice!, Please choose again: ")
        user_choice = input_checker(user_battle_decision)
    return user_choice


def fight_boss(player: dict, boss: dict) -> Union[dict, None]:
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
            if boss["hp"] > 0 and player["hp"] > 0:
                if run_or_fight_again() == "No":
                    run_away_player(player, boss)
                    return player
                else:
                    continue
            elif boss["hp"] < 1 and player["hp"] > 0:
                continue
        press_enter_to_continue()
    else:
        run_away_player(player, boss)


def game_win_art() -> None:
    """Print ASCII art to congratulate the player for winning the game."""
    print("you win!")
    press_enter_to_continue()
    quit()


def game() -> None:
    """Execute the game.

    The function consists of all the functions previously written. It runs a while loop to continue the game until the
    player types "quit" or achieves the goal of beating the boss.
    """
    print("Welcome player, I hope you are ready for an epic adventure!\n"
          "There's nothing too difficult about navigating around the game.\n"
          "You will only be allowed to input numbers that correspond to the items.\n"
          "The game will end when you defeat the boss or type quit during movements or your hp becomes 0.\n")
    board = make_board()
    player = make_player()
    boss = make_boss()
    move_character(player, board, boss)
    while player['hp'] > 0:
        battle_chance(player, random_monster(player))
        move_character(player, board, boss)
        if player["position"] == boss["position"]:
            fight_boss(player, boss)
            if boss["hp"] < 1:
                game_win_art()
            move_character(player, board, boss)
    game_over()


def main():
    """Execute the program"""
    # doctest.testmod(verbose=True)
    init()
    game()


if __name__ == "__main__":
    main()

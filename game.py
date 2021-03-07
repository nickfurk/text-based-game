"""
Your name: Paul Seong Uk Yeon
Your student number: A00990811

All of your code must go in this file.
Beginning of exam, not a single line of code has been written here previously.
"""
import itertools
from itertools import count
from random import randint, choice
from time import sleep
import doctest


def BASE_MAGE_HP():
    return 20


def MAGE_HP_INCREMENT():
    return 10


def BASE_THIEF_HP():
    return 20


def THIEF_HP_INCREMENT():
    return 10


def BASE_RANGER_HP():
    return 20


def RANGER_HP_INCREMENT():
    return 10


def BASE_WARRIOR_HP():
    return 20


def WARRIOR_HP_INCREMENT():
    return 10


# def MAX_MONSTER_HP():
#     return 10


# def MONSTER_HP_INCREMENT():
#     return 5


# def MAX_MONSTER_DAMAGE():
#     return 10


# def MONSTER_DAMAGE_INCREMENT():
#     return 5


def MAGE():
    return {
        1: {"level": 1, "level_name": "Apprentice Mage", "experience_needed": 500, "attack_name": "Fireball",
            "max_hp": BASE_MAGE_HP(), "base_damage_min": 15, "base_damage_max": 20, "accuracy_rate": 25},
        2: {"level": 2, "level_name": "Mage", "experience_needed": 1000, "attack_name": "Firestorm",
            "max_hp": BASE_MAGE_HP() + MAGE_HP_INCREMENT(), "base_damage_min": 20, "base_damage_max": 25,
            "accuracy_rate": 40},
        3: {"level": 3, "level_name": "Arch Mage", "attack_name": "Hellfire",
            "max_hp": BASE_MAGE_HP() + (MAGE_HP_INCREMENT() * 2), "base_damage_min": 25, "base_damage_max": 30,
            "accuracy_rate": 50}
    }


def THIEF():
    return {
        1: {"level": 1, "level_name": "Apprentice Thief", "experience_needed": 100, "attack_name": "Pickpocket",
            "max_hp": BASE_THIEF_HP(), "base_damage_min": 1, "base_damage_max": 5, "accuracy_rate": 85},
        2: {"level": 2, "level_name": "Bandit", "experience_needed": 300, "attack_name": "Boomerang Step",
            "max_hp": BASE_THIEF_HP() + THIEF_HP_INCREMENT(), "base_damage_min": 5, "base_damage_max": 10,
            "accuracy_rate": 95},
        3: {"level": 3, "level_name": "Hermit", "attack_name": "Assassinate",
            "max_hp": BASE_THIEF_HP() + (THIEF_HP_INCREMENT() * 2), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 100}
    }


def RANGER():
    return {
        1: {"level": 1, "level_name": "Apprentice Ranger", "experience_needed": 500, "attack_name": "Iron Arrow",
            "max_hp": BASE_RANGER_HP(), "base_damage_min": 5, "base_damage_max": 10, "accuracy_rate": 50},
        2: {"level": 2, "level_name": "Sniper", "experience_needed": 1000, "attack_name": "Mortal Blow",
            "max_hp": BASE_RANGER_HP() + RANGER_HP_INCREMENT(), "base_damage_min": 10, "base_damage_max": 15,
            "accuracy_rate": 60},
        3: {"level": 3, "level_name": "Marksman", "attack_name": "Dragon's Breath",
            "max_hp": BASE_RANGER_HP() + (RANGER_HP_INCREMENT() * 2), "base_damage_min": 15, "base_damage_max": 20,
            "accuracy_rate": 75}
    }


def WARRIOR():
    return {
        1: {"level": 1, "level_name": "Apprentice Warrior", "experience_needed": 200, "attack_name": "Threaten",
            "max_hp": BASE_WARRIOR_HP(), "base_damage_min": 7, "base_damage_max": 12, "accuracy_rate": 50},
        2: {"level": 2, "level_name": "Knight", "experience_needed": 1000, "attack_name": "Power Crash",
            "max_hp": BASE_WARRIOR_HP() + WARRIOR_HP_INCREMENT(), "base_damage_min": 12, "base_damage_max": 18,
            "accuracy_rate": 50},
        3: {"level": 3, "level_name": "Paladin", "attack_name": "Heaven's Hammer",
            "max_hp": BASE_WARRIOR_HP() + (WARRIOR_HP_INCREMENT() * 2), "base_damage_min": 18, "base_damage_max": 24,
            "accuracy_rate": 50}
    }


# def MONSTER_DAMAGE():
#     return {
#         1: {"level": 1, "damage": MAX_MONSTER_DAMAGE()},
#         2: {"level": 2, "damage": MAX_MONSTER_DAMAGE() + MONSTER_HP_INCREMENT()},
#         3: {"level": 3, "damage": MAX_MONSTER_DAMAGE() + (MONSTER_HP_INCREMENT() * 2)},
#     }


# def MONSTER_HP():
#     return {
#         1: {"level": 1, "hp": MAX_MONSTER_HP()},
#         2: {"level": 2, "hp": MAX_MONSTER_HP() + MONSTER_HP_INCREMENT()},
#         3: {"level": 3, "hp": MAX_MONSTER_HP() + (MONSTER_HP_INCREMENT() * 2)}
#     }


def PLAYER_STARTING_POSITION():
    """Set the player's starting position as [0, 0].

    :return: a list
    """
    return [0, 0]


def STARTING_PLAYER_DAMAGE():
    """Set the maximum player damage as 20.

    The number is used in the roll_die function to give an output of 1 - 20 inclusive.

    :return: an integer
    """
    return 10


def MAX_MONSTER_DAMAGE():
    """Set the maximum monster damage as 20.

    The number is used in the roll_die function to give an output of 1 - 10 inclusive.

    :return: an integer
    """
    return 10


def RUN_AWAY_PROBABILITY():
    """Set the number for probability of running away.

    The number is used in the roll_die function to simulate a 20% chance.

    :return: an integer
    """
    return 5


def RUN_AWAY_DAMAGE_PROBABILITY():
    """Set the maximum shiv damage as 4.

    The number is used in the roll_die function to give an output of 1 - 4 inclusive.

    :return: an integer
    """
    return 4


def INITIAL_ATTACK_PROBABILITY():
    """Set the number as 100.

    The number is used in the roll_die function to give an output of 1 - 100 inclusive.

    :return: an integer
    """
    return 100


def MAX_PLAYER_HP():
    """Set the player's max health as 20.

    :return: an integer
    """
    return 20


def MAX_MONSTER_HP():
    """Set the monster's max health as 10.

    :return: an integer
    """
    return 10


def DUNGEON_LIST():
    """Provide a dictionary of coordinates and dungeon descriptions.

    :return: a dictionary
    """
    dungeon_list = {
        (0, 0): "You've started your journey from this room.\nYou feel safer here for some reason.\n",
        (0, 1): "The room is lit by the light seeping through from the previous location, but you instantly feel the "
                "difference in the atmosphere already.\nFor some reason, you are just a bit more cold.\n",
        (0, 2): "You start to move on an instinct as the seeping light no longer covers the entirety of the room "
                "anymore.\nYou start to feel a shiver up your spine every step you take.\n",
        (0, 3): "This room is surprisingly warm... You wonder why...\n",
        (0, 4): "You start to feel more paranoid as time passes, and keep thinking back\non your life and whether "
                "or not you'll be able to get out of here alive\n",
        (1, 0): "The room is lit by the light seeping through from the previous location, but you instantly feel the "
                "difference\nin the atmosphere already. For some reason, you are just a bit more cold.\n",
        (1, 1): "Your steps seem to have slowed down and without confidence...\n",
        (1, 2): "You start to move on an instinct as the seeping light no longer covers the entirety of the room "
                "anymore.\nYou start to feel a shiver up your spine every step you take.\n",
        (1, 3): "There's water dripping from the top,\nbut you don't know why because you can't see how far up the "
                "ceiling is in this dark.\n",
        (1, 4): "You start to feel more paranoid as time passes, and keep thinking back on your life\nand whether "
                "or not you'll be able to get out of here alive\n",
        (2, 0): "The room makes you regret ever starting this journey.\nEvery step feels more tiring than before.\n",
        (2, 1): "The room is lighted by torches along the sides of the walls.\nYou feel warmer than before.\n",
        (2, 2): "The room is filled with fog, but you aren't sure what exactly they are.\nYou only know that it isn't "
                "a pleasant feeling.\nYou want to exit the room as soon as you can.\n",
        (2, 3): "You are starting to consider quitting.\nThis isn't what you expected. Nothing is worth this pain.\n",
        (2, 4): "There's a small pond in the middle of the room.\nYou think about drinking from the pond, but upon "
                "further inspection,\nyou find that the water has skeletal remains in it.\nYou feel sick.\n",
        (3, 0): "This room is extremely cold.\nYou are likely to get a frostbite in this weather.\n",
        (
        3, 1): "The room seems to have some type of wildlife,\nas you hear the cicadas crying somewhere in the room.\n",
        (3, 2): "This room has plants growing all around.\nYou can also see mushrooms growing beneath the biggest tree "
                "in the room. Although you are exhausted and hungry, you aren't sure these are safe to eat.\n",
        (3, 3): "The room is pitch dark and makes you want to give up everything.\n",
        (3, 4): "You see the glimpse of light shining through the next room.\nYou become excited as you feel that you "
                "are almost at the end of your journey.\n",
        (4, 0): "There's water dripping from the top, but you don't know why\nbecause you can't see how far up the "
                "ceiling is in this dark.\n",
        (4, 1): "You start to feel more paranoid as time passes, and keep\nthinking back on your life and whether "
                "or not you'll be able to get out of here alive\n",
        (4, 2): "This room is surprisingly warm... You wonder why...\n",
        (4, 3): "You see the glimpse of light shining through the next room.\nYou become excited as you feel that you "
                "are almost at the end of your journey.\n",
        (4, 4): "You have arrived at end of the rooms!\nYou can see that you've returned to the initial place you've "
                "entered from,\nand life was continuing... You swear never to go on a journey ever again.\n"}
    return dungeon_list


def BATTLE_CHANCE():
    return 1


def BOARD_SIZE():
    return 25


def JOB_LIST():
    return ["Mage", "Thief", "Ranger", "Warrior"]


def DIRECTION_LIST():
    return ["W", "E", "S", "N", "quit"]


def LIST_OF_MONSTERS():
    return ["Amputator", "Bone Breaker", "Dark Cultist", "Fallen Shaman", "Flesh Harvester", "Terror Bat",
            "Dust Imp", "Demonic Hellflyer"]


def LIST_OF_MONSTER_TYPES():
    return ["Cave of Alcarnus", "Necropolis Mines", "River of Kehjan", "Black Canyon Mines", "Ureh Caverns"]


def YES_OR_NO():
    return ["Yes", "No"]


def make_board():
    """Generate game board as a dictionary.

    Function generates a dictionary with coordinate tuples as keys and location description as values.

    :return: dictionary with coordinate tuples as keys and location description as values
    """
    location_description = [
        """This room has a cage in the center.""",
        """This room has a well in the center""",
        """This room looks like a bar.""",
        """There are zombies in the opposite corner of you.""",
        """This room has a wooden chair in the center.""",
        """This room has a man hanging upside down from the ceiling."""
    ]
    cycle_location = itertools.cycle(location_description)
    board = {(row, column): {"location_description": next(cycle_location)} for row in range(BOARD_SIZE())
             for column in range(BOARD_SIZE())}
    return board


def input_checker(list_of_options):
    """Generate user choice from provided dictionary.

    The function will take the provided dictionary, and ask for the user for input. It will then match the user input
    with the corresponding number so the user can choose by number.

    :param list_of_options: a dictionary
    :precondition: the dictionary must have the correct key/value pair, where the key is a number and value is a string
    :postcondition: correctly matches the user choice for key and returns the corresponding value
    :return: value of the chosen key as a string
    """
    print(str(list_of_options).replace(",", "\n"))
    sleep(1)
    user_input = input("\nPlease choose from the following list of options by typing in the corresponding number: \n")
    for keys, values in list_of_options.items():
        if user_input == keys:
            user_choice = values
            return user_choice


def delayed_message(message, delay):
    """Add delays to string prints.

    :param message: a string
    :param delay: a number
    :precondition: delay has to be a positive number
    :postcondition: prints the message with delay correctly
    :return: a string
    """
    sleep(delay)
    return print(message)


def press_enter_to_continue():
    user_input = input("\nPress enter to continue the game!: \n")
    while user_input != "":
        print("Please press enter!")
        user_input = input("Press enter to continue the game!: ")


def player_name_generator():
    """Create a name based on user input.

    :postcondition: gets user input and assigns it to variable
    :return: a string
    """
    user_input = input("What will your name be for this game?: ")
    while user_input == "":
        print("You can't have nothing for your name, but anything else works! Try again.")
        user_input = input("What will your name be for this game?: ")
    print(f"\nWelcome to the game, {user_input}. \n")
    sleep(1)
    return user_input


def player_job_generator(player):
    """Designate player job based on user choice.

    :postcondition: gets user input and assigns it to variable
    :return: a string
    """
    print("Below is the list of jobs you can choose to play throughout the game. Choose wisely so that you'll be able "
          "to win the game successfully... \n")
    new_list_for_user = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), JOB_LIST())}
    player_job = input_checker(new_list_for_user)
    while player_job not in JOB_LIST():
        print("That's not in the list of jobs you can choose from!")
        player_job = input_checker(new_list_for_user)
    player["class"] = player_job
    delayed_message(f"\n{player_job} is a great choice!\n", 0.75)
    return player_job


def make_player():
    """Create a dictionary that contains player name, player job, player hp, player position, player level/exp, damage,
       and number of run away chances available.

    :postcondition: gets user input and creates player information dictionary
    :return: a dictionary
    """
    # player_name = player_name_generator()
    # player_hp = MAX_PLAYER_HP()
    # player_position = PLAYER_STARTING_POSITION()
    # player_damage = STARTING_PLAYER_DAMAGE()
    player = {"name": player_name_generator(),
              "class": "",
              "hp": MAX_PLAYER_HP(),
              "position": PLAYER_STARTING_POSITION(),
              "level": 1,
              "damage": STARTING_PLAYER_DAMAGE(),
              "experience": 0}
    player["class"] = player_job_generator(player)
    return player


def display_map(player):
    """Print player's position on a map.

    :param player: must be a dictionary with player's position as coordinate tuples
    :precondition: player must bet a dictionary with player's position as coordinates
    :return: print player's position on a map
    """
    for row in range(BOARD_SIZE()):
        line = ""
        for column in range(BOARD_SIZE()):
            symbol = "[ ]"
            if player["position"] == [row, column]:
                symbol = "[X]"
            line += symbol + ""
        print(line)


# #testing function
# player = {"position": (1, 1)}
# display_map(player)


def display_info(player, board):
    """Print player's position, location description, health point, level and experience point.

    :param player: a dictionary with player's position, health point, level and experience
    :param board: a dictionary with loc
    :return:
    """
    coordinate = player["position"]
    print(f'Location: {player["position"]}')
    print(f'Description: {board[tuple(coordinate)]["location_description"]}')
    print(f'Health point: {player["hp"]}')
    print(f'Level: {player["level"]}')
    print(f'Experience: {player["experience"]}')


# #testing function
# player_test = {"position": (2, 2), "description": "huanted room", "hp": 30, "level": 2, "experience": 800}
# print(display_info(player_test, make_board()))


# def dungeon(player_info):
#     """Print the map of the player's current position.
#
#     The map will be a 5x5 dungeon, where "#" will represent the player's current position within the map. The function
#     will print the map based on the player's current position.
#
#     :param player_info: a list
#     :precondition: player_info must be a proper list with correct character and information
#     :precondition: the list must contain two numbers within the range of 0 and 4 inclusive
#     :postcondition: prints the correct current position of the player in the dungeon as a string
#
#     >>> player_information = {"name": "Paul", "job": "Witch Doctor", "hp": 20, "position": [1, 2], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
#     >>> dungeon(player_information["position"])
#     [ ][ ][ ][ ][ ]
#     [ ][ ][#][ ][ ]
#     [ ][ ][ ][ ][ ]
#     [ ][ ][ ][ ][ ]
#     [ ][ ][ ][ ][ ]
#     """
#     for location in range(5):
#         if location == player_info["position"][0]:
#             print(("[ ]" * player_info["position"][1]) + "[#]" + ("[ ]"
#                   * (4 - player_info["position"][1])))
#         else:
#             print("[ ]" * 5)


def validate_move(current_position, user_direction):
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


def player_movement_change(current_position, user_direction):
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


def game_over():
    """Generate a prompt to end the game."""
    print("\nThanks for playing! The game is over, goodbye!")
    input("Press enter to end the game :)")
    quit()


def move_character(player, board):
    """Change the position of the player to a new position based on user input.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: the player's position will correctly change according to user input
    :return: a changed player's new position in a list or "quit" as a string
    """
    player_game_descriptions(player, board)
    if player["hp"] > 0:
        new_direction_list = {str(keys): jobs for keys, jobs in enumerate(DIRECTION_LIST(), 1)}
        user_input = input_checker(new_direction_list)
        while user_input not in DIRECTION_LIST() or validate_move(player['position'], user_input):
            print("\nYou can't go that way! Choose again wisely.")
            user_input = input_checker(new_direction_list)
        player_movement_change(player["position"], user_input)
        return player["position"]


def dungeon_description(player):
    """Generate a story for the room.

    The function will go through the dictionary and print description according to the player's position.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: a correct map description correspondant to the player position
    :return: description of map as a string

    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 20, "position": [4, 2], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
    >>> dungeon_description(players["position"])
    "This room is surprisingly warm... You wonder why...\n"

    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 20, "position": [1, 1], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
    >>> dungeon_description(players["position"])
    "Your steps seem to have slowed down and without confidence...\n"
    """
    list_of_map_descriptions = DUNGEON_LIST()
    for keys, values in list_of_map_descriptions.items():
        if tuple(player["position"]) == keys:
            user_position_dungeon_description = values
            return user_position_dungeon_description


def roll_die(number_of_rolls, number_of_sides):
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


def battle_chance(player, monster):
    """Roll a die to determine if the player will meet an enemy.

    The player has a 40% chance to meet an enemy everytime they move. This is determined by rolling a 10 sided die once,
    and if the rolled number is less than or equal to 4, it will lead to the combat_round function. Else, heal_player
    function.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly lead to corresponding functions depending on situation
    """
    battle_chance_number = roll_die(1, BATTLE_CHANCE())
    if battle_chance_number == 1:
        delayed_message("There's someone lurking in the dark!", 1)
        combat_round(player, monster)
    else:
        heal_player(player)


def heal_player(player):
    """Update character_info based on their current hp.

    The function will heal the player's hp based on their current amount. The heal amount will only be up to 20.

    :param player: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly changes the value of character's hp
    :return: the changed hp value in the dictionary

    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 10, "position": [1, 2], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
    >>> heal_player(players)
    >>> players["hp"]
    14
    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 18, "position": [1, 2], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
    >>> heal_player(players)
    >>> players["hp"]
    20
    """
    delayed_message("It seems like there's no one in the room. You are healed by 4 hp!\n", 1)
    initial_health = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    target_health = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20, 20]
    for health in range(len(initial_health)):
        if health == player["hp"]:
            player["hp"] = target_health[health]
            return player


def random_monster():
    """Create a dictionary of random monster, random monster type, and hp.

    The function will pick a random monster from a list of tuple, and their type from a list of tuple. It will assign
    hp, then put them into a dictionary.

    :postcondition: correctly chooses random elements and puts them into a dictionary
    :return: a dictionary
    """
    random_monster_name = choice(LIST_OF_MONSTERS())
    random_monster_type = choice(LIST_OF_MONSTER_TYPES())
    monster_hp = MAX_MONSTER_HP()
    monster_damage = MAX_MONSTER_DAMAGE()
    monster_info = {"name": random_monster_name, "type": random_monster_type, "hp": monster_hp,
                    "damage": monster_damage}
    return monster_info


def fight_or_run_decision(monster):
    print(f"\nYou have encountered {monster['name']}! Would you like to fight?\n")
    user_battle_decision = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    while user_choice not in YES_OR_NO():
        print(f"{user_choice} is not a valid choice!, Please choose again: ")
        user_choice = input_checker(user_battle_decision)
    return user_choice


def combat_round(player, monster):
    """Direct the user to different functions based on their input.

    This function will give the user an option to run or fight. Either options will send the user to other functions. If
    the player's run_away_chance is 0, they will be forced to fight even if they choose "No". The battle_start has a
    while loop implemented to keep the battle going until one of their hp values reach 0.

    :param player: a dictionary
    :param monster: a dictionary
    :precondition: player must be a proper dictionary with correct character and information
    :postcondition: correctly leads to corresponding functions depending on situation
    """
    # print(f"\nYou have encountered {monster['name']}! Would you like to fight?\n")
    # user_battle_decision = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    # user_choice = input_checker(user_battle_decision)
    # while user_choice not in YES_OR_NO():
    #     print(f"{user_choice} is not a valid choice!, Please choose again: ")
    #     user_choice = input_checker(user_battle_decision)
    if fight_or_run_decision(monster) == "Yes":
        while player["hp"] > 0 and monster["hp"] > 0:
            battle_start(player, monster, battle_attack_order())
            if run_away_monster(monster) and monster["hp"] > 0 and player["hp"] > 0:
                return player
            elif monster["hp"] > 0 and player["hp"] > 0:
                if run_or_fight_again() == "No":
                    run_away_player(player, monster)
                    return player
                else:
                    continue
        press_enter_to_continue()
    else:
        run_away_player(player, monster)


def run_away_player(player, monster):
    """Roll a die to determine if the player will get damaged while fleeing.

    The player has a 20% chance to avoid damage while running away. This is determined by rolling a 5 sided die once,
    and if the rolled number is 1, they will be damaged. The damage amount will be determined by rolling a 4 sided die
    once, and the player hp is updated by the damage amount. Else, no damage taken while fleeing.

    :param player: a dictionary
    :param monster_info: a dictionary
    :precondition: player and monster_info must be a proper dictionary with correct character and information
    :postcondition: correctly changed hp depending on situation
    :return: changed player's hp value if attack is successful in a dictionary

    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 10, "position": [1, 2], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
    >>> monster = {"name": "Fallen Shamen", "type": "Ureh Caverns", "hp": 10, "damage": 10}
    >>> run_away_player(players, monster)
    >>> run_away_number == 1
    >>> players["hp"] < 10
    True
    >>> players = {"name": "Paul", "job": "Witch Doctor", "hp": 14, "position": [1, 2], "level": {"level": 1, "exp": 0}, "damage": 10, "run_away_chance": 3}
    >>> monster = {"name": "Fallen Shamen", "type": "Ureh Caverns", "hp": 10, "damage": 10}
    >>> run_away_player(players, monster)
    >>> run_away_number == 3
    >>> players["hp"] == 14
    True
    """
    run_away_number = roll_die(1, RUN_AWAY_PROBABILITY())
    if run_away_number == 1:
        run_away_damage = roll_die(1, RUN_AWAY_DAMAGE_PROBABILITY())
        player["hp"] -= run_away_damage
        delayed_message(f"You've been damaged {run_away_damage} hp by {monster['name']} while running away!"
                        f"\nYou only have{player['hp']} hp left! Be careful {player['name']}!", 1)
        press_enter_to_continue()
        return player
    else:
        delayed_message(f"You've run away successfully from {monster['name']}!"
                        f"You were very lucky this time...\n", 1)
        press_enter_to_continue()
        return player


def run_or_fight_again():
    print(f"\nWould you like to keep fighting?\n")
    user_battle_decision = {str(keys): jobs for keys, jobs in zip(count(start=1, step=1), YES_OR_NO())}
    user_choice = input_checker(user_battle_decision)
    while user_choice not in YES_OR_NO():
        print(f"{user_choice} is not a valid choice!, Please choose again: ")
        user_choice = input_checker(user_battle_decision)
    return user_choice


def run_away_monster(monster):
    run_away_number = roll_die(1, RUN_AWAY_PROBABILITY())
    if run_away_number == 1:
        delayed_message(f"{monster['name']} ran away!", 1)
        press_enter_to_continue()
        return True
    else:
        return False


def battle_attack_order():
    """Determine who will attack first.

    The function will roll a 100 sided die twice, and determine the attack order of the player and monster. The function
    has a recursion implemented, so it would keep rolling the dice if the roll results are the same. It will lead to
    different situations. The order of attack will change each round.

    :precondition: player and monster_info must be a proper dictionary with correct character and information
    :postcondition: determines correct battle order and invokes the battle order for the round
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


def battle_start(player, monster_info, attacker):
    """Simulate a battle between two characters.

    The function identifies the player through attacker boolean value, then runs the attacking_round in a correct order,
    and also implementing the correct damage amount. If the monster dies, it will also run the leveling_package function
    to change the player's information.

    :param player: a dictionary
    :param monster_info: a dictionary
    :param attacker: a boolean
    :precondition: first_attack and second_attack must be a proper dictionary with correct character and information
    :postcondition: correctly continue to run the round until one of the characters have 0 hp value
    :postcondition: correctly lead to leveling_package if the monster_info hp is 0
    """
    # sleep(1)
    # if attacker:
    #     attacking_round(player, monster_info, STARTING_PLAYER_DAMAGE())
    #     if monster_info['hp'] > 0:
    #         attacking_round(monster_info, player, MAX_MONSTER_DAMAGE())
    # elif attacker is False:
    #     attacking_round(monster_info, player, MAX_MONSTER_DAMAGE())
    #     if player['hp'] > 0:
    #         attacking_round(player, monster_info, STARTING_PLAYER_DAMAGE())
    # elif monster_info['hp'] <= 0:
    #     player["experience"] += 100
    #     check_level(player)
    #     #leveling_package(player)

    sleep(1)
    if attacker:
        attacking_round(player, monster_info, STARTING_PLAYER_DAMAGE())
        if monster_info['hp'] > 0:
            attacking_round(monster_info, player, MAX_MONSTER_DAMAGE())
        else:
            player["experience"] += 100
            check_level(player)
    elif attacker is False:
        attacking_round(monster_info, player, MAX_MONSTER_DAMAGE())
        if player['hp'] > 0:
            attacking_round(player, monster_info, STARTING_PLAYER_DAMAGE())
        if monster_info['hp'] < 0:
            player["experience"] += 100
            check_level(player)
    # elif monster_info['hp'] <= 0:
    #     player["experience"] += 100
    #     check_level(player)


def attacking_round(attacker, opponent, damage_amount):
    """Simulate a single attack to the opponent.

    This function runs a combat simulation that changes the damaged's hp value.

    :param attacker: a dictionary
    :param opponent: a dictionary
    :param damage_amount: an integer
    :precondition: attacker and damaged must be a proper dictionary with correct character and information
    :precondition: damage_amount must be a positive integer
    :postcondition: correctly changed hp of damaged
    :return: changed hp value of damaged in a dictionary
    """
    damage = roll_die(1, damage_amount)
    opponent['hp'] -= damage
    delayed_message(f"{attacker['name']} has done {damage} damage to {opponent['name']}!"
                    f"\n{opponent['name']} has {opponent['hp']} hp left!\n", 0.5)
    return opponent


def return_class_dictionary(player):
    if player["class"] == "mage":
        return MAGE()
    elif player["class"] == "Thief":
        return THIEF()
    elif player["class"] == "Ranger":
        return RANGER()
    else:
        return WARRIOR()


def check_level(player):
    class_dictionary = return_class_dictionary(player)
    level = 1
    if player["experience"] >= class_dictionary[1]["experience_needed"]:
        level += 1
    if player["experience"] >= class_dictionary[2]["experience_needed"]:
        level += 1
    # return level
    player["level"] = level


# def leveling_package(player):
#     """Change the values of player level and damage based on experience value.
#
#     The function will record the amount of experience the player receives, and if it reaches the threshold of 500, it
#     will change the player's level and damage, then change the value of experience back to 0.
#
#     :param player: a dictionary
#     :precondition: player must be a proper dictionary with correct character and information
#     :return: changed player level and damage value depending on situation in a dictionary
#     """
#     if player["level"]["exp"] == 400:
#         player["level"]["exp"] = 0
#         player["level"]["level"] += 1
#         player["damage"] += 2
#         return player
#     else:
#         player["level"]["exp"] += 100
#         return player


def player_game_descriptions(player, board):
    display_map(player)
    display_info(player, board)


def game():
    """Execute the game.

    The function consists of all the functions previously written. It runs a while loop to continue the game until the
    player types "quit" or achieves the goal of reaching [4, 4] on the map.
    """
    print("Welcome player, I hope you are ready for an epic adventure!\n"
          "There's nothing too difficult about navigating around the game.\n"
          "You will only be allowed to input numbers that correspond to the items.\n"
          "The game will end when you reach [4, 4] or type quit during movements or your hp becomes 0.\n"
          "If you take a look at the list, you will see your name, then your job, \n"
          "followed by you hp values noted as [current hp, max hp], and your current location.\n"
          "I hope you have fun playing! Let the journey begin!\n")
    board = make_board()
    player = make_player()
    # player_game_descriptions(player, board)
    player_move = move_character(player, board)
    while player_move != "quit" and player['hp'] > 0 and player['position'] != [4, 4]:
        # delayed_message("\n" + dungeon_description(player), 1)
        battle_chance(player, random_monster())
        # player_game_descriptions(player, board)
        # display_map(player)
        # display_info(player, board)
        if player['hp'] > 0:
            player_move = move_character(player, board)
        else:
            game_over()
    game_over()


def main():
    """Execute the program"""
    # doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()

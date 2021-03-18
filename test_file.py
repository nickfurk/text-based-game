import itertools


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

def MAX_MONSTER_HP():
    return 10

def MONSTER_HP_INCREMENT():
    return 5
# print(MAX_MONSTER_HP() + (MONSTER_HP_INCREMENT() * 2))

def MAX_MONSTER_DAMAGE():
    return 10

def MONSTER_DAMAGE_INCREMENT():
    return 5
# print(MAX_MONSTER_DAMAGE() + (MONSTER_DAMAGE_INCREMENT() * 2))


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
        1: {"level": 1, "level_name": "Apprentice Thief", "experience_needed": 500, "attack_name": "Pickpocket",
            "max_hp": BASE_THIEF_HP(), "base_damage_min": 1, "base_damage_max": 5, "accuracy_rate": 85},
        2: {"level": 2, "level_name": "Bandit", "experience_needed": 1000, "attack_name": "Boomerang Step",
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
        1: {"level": 1, "level_name": "Apprentice Warrior", "experience_needed": 500, "attack_name": "Threaten",
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
#         2: {"level": 2, "damage": MAX_MONSTER_DAMAGE() + MONSTER_DAMAGE_INCREMENT()},
#         3: {"level": 3, "damage": MAX_MONSTER_DAMAGE() + (MONSTER_DAMAGE_INCREMENT() * 2)},
#     }

def MONSTER_HP():
    return {
        1: {"level": 1, "hp": MAX_MONSTER_HP()},
        2: {"level": 2, "hp": MAX_MONSTER_HP() + MONSTER_HP_INCREMENT()},
        3: {"level": 3, "hp": MAX_MONSTER_HP() + (MONSTER_HP_INCREMENT() * 2)}
    }

# def check_class_choice(user_choice):
#     if user_choice == "Mage":
#         return MAGE()
#     elif user_choice == "Thief":
#         return THIEF()
#     elif user_choice == "Ranger":
#         return RANGER()
#     elif user_choice == "Warrior":
#         return WARRIOR()


def return_class_dictionary(player):
    if player["class"] == "Mage":
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
    return level
# #testing function
# player_info = {"class": "warrior", "experience": 600}
# print(check_level(player_info))


def change_player_class_dictionary(player):
    current_dictionary = return_class_dictionary(player)
    current_level = check_level(player)
    player["class_dictionary"] = current_dictionary[current_level]
# #testing function
player_info = {"class": "warrior", "class_dictionary": "placeholder", "experience": 1000}
change_player_class_dictionary(player_info)
# print(player_info)


def update_monster_hp(monster, player):
    player_current_level = check_level(player)
    monster_hp_dictionary = MONSTER_HP()
    monster["hp"] = monster_hp_dictionary[player_current_level]["hp"]
# #testing function
monster_info = {"hp": 10}
player_info = {"class": "warrior", "experience": 1000}
update_monster_hp(monster_info, player_info)
print(monster_info)

def MONSTER_DAMAGE():
    return {
        1: {"level": 1, "damage": MAX_MONSTER_DAMAGE()},
        2: {"level": 2, "damage": MAX_MONSTER_DAMAGE() + MONSTER_DAMAGE_INCREMENT()},
        3: {"level": 3, "damage": MAX_MONSTER_DAMAGE() + (MONSTER_DAMAGE_INCREMENT() * 2)},
    }

def make_boss():
    boss = {"name": PICK_RANDOM_BOSS_NAME(),
            "hp": MAX_BOSS_HP(),
            "damage": MAX_BOSS_DAMAGE(),
            "position": [2, 2]}
    return boss

def random_monster(player):
    monster_info = {"name": random_monster_name,
                    "type": random_monster_type,
                    "hp": "",
                    "category": "monster",
                    "damage": monster_damage}
    check_monster_hp(player, monster_info)
    return monster_info

def update_monster_damage(monster, player):
    player_current_level = check_level(player)
    monster_damage_dictionary = MONSTER_DAMAGE()
    monster["damage"] = monster_damage_dictionary[player_current_level]["damage"]
# #testing function
# monster_info = {"hp": 10}
# player_info = {"class": "warrior", "experience": 800}
# update_monster_damage(monster_info, player_info)
# print(monster_info)


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
    user_input = input("\nPlease choose from the following list of options by typing in the corresponding number: \n")
    for keys, values in list_of_options.items():
        if user_input == keys:
            user_choice = values
            return user_choice


def player_job_generator():
    """Designate player job based on user choice.

    :postcondition: gets user input and assigns it to variable
    :return: a string
    """
    print("Below is the list of jobs you can choose to play throughout the game. Choose wisely so that you'll be able "
          "to win the game successfully... \n")
    job_list = ["Mage", "Thief", "Ranger", "Warrior"]
    new_list_for_user = {str(keys): jobs for keys, jobs in zip(itertools.count(start=1, step=1), job_list)}
    player_job = input_checker(new_list_for_user)
    while player_job not in job_list:
        print("That's not in the list of jobs you can choose from!")
        player_job = input_checker(new_list_for_user)
    print(f"\n{player_job} is a great choice!\n")
    job_dictionary = return_class_dictionary(player_job)
    return job_dictionary


import random

def attacking_round(attacker, opponent):
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
    if attacker["category"] == "player":
        accuracy_roll = random.randint(1, 100)
        if accuracy_roll <= attacker["class_dictionary"]["accuracy_rate"]:
            player_damage = random.randint(attacker["class_dictionary"]["base_damage_min"], attacker["class_dictionary"]["base_damage_max"])
            opponent["hp"] -= player_damage
        else: print(f'poor accuracy!')
    else:
        monster_damage = random.randint(1, attacker["damage"]) #switch to roll_dice function for this in production
        opponent["hp"] -= monster_damage
    # delayed_message(f"{attacker['name']} has done {damage} damage to {opponent['name']}!"
    #                 f"\n{opponent['name']} has {opponent['hp']} hp left!\n", 0.5)
    return opponent
#testing function
# monster_info = {"damage": 10, "hp": 20, "category": "monster"}
# player_info = {'name': 'leo', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'damage': 10, 'experience': 0, 'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior', 'experience_needed': 200, 'attack_name': 'Threaten', 'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12, 'accuracy_rate': 50}}
# print(attacking_round(player_info, monster_info))
#NEED TO ADD CATEGORY INTO BOTH PLAYER AND MONSTER LIST



def choices(x, y):
    return x + " : " + y

numbers = ["1", "2", "3", "4"]
types = ["Mage", "Warrior", "Horse", "Duck"]

result = map(choices, numbers, types)
print(list(result))

#
# def addition(x, y):
#     return print(f'{x}:{y}')
#
# numbers1 = [5, 6, 2, 8]
# numbers2 = [7, 1, 4, 9]
# result = map(addition, numbers1, numbers2)
# print(list(result))

# def player():
#     player_info = {"class_dictionary": player_job_generator()[0], "exp": 200}
#     return player_info


# def main():
#     # print(player())
#     # print(leveling_package({"class": WARRIOR()[0], "exp": 200}))
#
#
# if __name__ == "__main__":
#     main()
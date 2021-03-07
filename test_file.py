import itertools


def BASE_MAGE_HP():
    return 20

def MAGE_HP_INCREMENT(hp):
    return hp + 10

def BASE_THIEF_HP():
    return 20

def THIEF_HP_INCREMENT(hp):
    return hp + 10

def BASE_RANGER_HP():
    return 20

def RANGER_HP_INCREMENT(hp):
    return hp + 10

def BASE_WARRIOR_HP():
    return 20

def WARRIOR_HP_INCREMENT(hp):
    return hp + 10

def MAX_MONSTER_HP():
    return 10

def MONSTER_HP_INCREMENT(hp):
    return hp + 5
# print(MONSTER_HP_INCREMENT(MAX_MONSTER_HP()))

def MAX_MONSTER_DAMAGE():
    return 10

def MONSTER_DAMAGE_INCREMENT(damage):
    return damage + 5


def MAGE():
    return {
        1: {"Level": 1, "Level_name": "Apprentice Mage", "Experience_needed": 500,
                         "Attack_name": "Fireball", "Max_HP": BASE_MAGE_HP(), "Base_damage_min": 15,
                         "Base_damage_max": 20, "Accuracy_rate": 25},
        2: {"Level": 2, "Level_name": "Mage", "Experience_needed": 1000,
                         "Attack_name": "Firestorm", "Max_HP": MAGE_HP_INCREMENT(BASE_MAGE_HP()), "Base_damage_min": 20,
                         "Base_damage_max": 25, "Accuracy_rate": 40},
        3: {"Level": 3, "Level_name": "Arch Mage", "Attack_name": "Hellfire",
                         "Max_HP": MAGE_HP_INCREMENT(BASE_MAGE_HP()), "Base_damage_min": 25, "Base_damage_max": 30,
                         "Accuracy_rate": 50}
        }
def THIEF():
    return {
        1: {"Level": 1, "Level_name": "Apprentice Thief", "Experience_needed": 500,
                          "Attack_name": "Pickpocket", "Max_HP": BASE_THIEF_HP(), "Base_damage_min": 1,
                          "Base_damage_max": 5, "Accuracy_rate": 85},
        2: {"Level": 2, "Level_name": "Bandit", "Experience_needed": 1000,
                          "Attack_name": "Boomerang Step", "Max_HP": THIEF_HP_INCREMENT(BASE_THIEF_HP()),
                          "Base_damage_min": 5, "Base_damage_max": 10, "Accuracy_rate": 95},
        3: {"Level": 3, "Level_name": "Hermit", "Attack_name": "Assassinate",
                         "Max_HP": THIEF_HP_INCREMENT(BASE_THIEF_HP()), "Base_damage_min": 10, "Base_damage_max": 15,
                         "Accuracy_rate": 100}
        }

def RANGER():
    return {
        1: {"Level": 1, "Level_name": "Apprentice Ranger", "Experience_needed": 500,
                           "Attack_name": "Iron Arrow", "Max_HP": BASE_RANGER_HP(), "Base_damage_min": 5,
                           "Base_damage_max": 10, "Accuracy_rate": 50},
        2: {"Level": 2, "Level_name": "Sniper", "Experience_needed": 1000,
                           "Attack_name": "Mortal Blow", "Max_HP": RANGER_HP_INCREMENT(BASE_RANGER_HP()),
                           "Base_damage_min": 10, "Base_damage_max": 15, "Accuracy_rate": 60},
        3: {"Level": 3, "Level_name": "Marksman", "Attack_name": "Dragon's Breath",
                          "Max_HP": RANGER_HP_INCREMENT(BASE_RANGER_HP()), "Base_damage_min": 15, "Base_damage_max": 20,
                          "Accuracy_rate": 75}
        }
def WARRIOR():
    return {
        1: {"Level": 1, "Level_name": "Apprentice Warrior", "Experience_needed": 500,
                            "Attack_name": "Threaten", "Max_HP": BASE_WARRIOR_HP(), "Base_damage_min": 7,
                            "Base_damage_max": 12, "Accuracy_rate": 50},
        2: {"Level": 2, "Level_name": "Knight", "Experience_needed": 1000,
                            "Attack_name": "Power Crash", "Max_HP": WARRIOR_HP_INCREMENT(BASE_WARRIOR_HP()),
                            "Base_damage_min": 12, "Base_damage_max": 18, "Accuracy_rate": 50},
        3: {"Level": 3, "Level_name": "Paladin","Attack_name": "Heaven's Hammer",
                           "Max_HP": WARRIOR_HP_INCREMENT(BASE_WARRIOR_HP()), "Base_damage_min": 18,
                            "Base_damage_max": 24, "Accuracy_rate": 50}
    }

def MONSTER_DAMAGE():
    return {
        1: {"Level": 1, "Damage": MAX_MONSTER_DAMAGE()},
        2: {"Level": 2, "Damage": MONSTER_DAMAGE_INCREMENT(MAX_MONSTER_DAMAGE())},
        3: {"Level": 3, "Damage": MONSTER_DAMAGE_INCREMENT(MAX_MONSTER_DAMAGE())}
    }

def MONSTER_HP():
    return {
        1: {"Level": 1, "hp": MAX_MONSTER_HP()},
        2: {"Level": 2, "hp": MONSTER_HP_INCREMENT(MAX_MONSTER_HP())},
        3: {"Level": 3, "hp": MONSTER_HP_INCREMENT(MAX_MONSTER_HP())}
    }

def check_class_choice(user_choice):
    if user_choice == "Mage":
        return MAGE()
    elif user_choice == "Thief":
        return THIEF()
    elif user_choice == "Ranger":
        return RANGER()
    elif user_choice == "Warrior":
        return WARRIOR()


def return_class_dictionary(player):
    if player["class"] == "mage":
        return MAGE()
    elif player["class"] == "thief":
        return THIEF()
    elif player["class"] == "ranger":
        return RANGER()
    else:
        return WARRIOR()


def check_level(player):
    class_dictionary = return_class_dictionary(player)
    level = 1
    if player["experience"] >= class_dictionary[1]["Experience_needed"]:
        level += 1
    if player["experience"] >= class_dictionary[2]["Experience_needed"]:
        level += 1
    return level
# #testing function
# player_info = {"class": "warrior", "experience": 300}
# print(check_level(player_info))


def change_player_class_dictionary(player):
    current_dictionary = return_class_dictionary(player)
    current_level = check_level(player)
    player["class_dictionary"] = current_dictionary[current_level]
# testing function
# player_info = {"class": "warrior", "class_dictionary": "placeholder", "experience": 1000}
# change_player_class_dictionary(player_info)
# print(player_info)

def update_monster_hp(monster):


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
    job_dictionary = check_class_choice(player_job)
    return job_dictionary


def player():
    player_info = {"class_dictionary": player_job_generator()[0], "exp": 200}
    return player_info


# def main():
#     # print(player())
#     # print(leveling_package({"class": WARRIOR()[0], "exp": 200}))
#
#
# if __name__ == "__main__":
#     main()
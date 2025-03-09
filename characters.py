"""
This module defines the `Character` class and related functions to initialize and manage a player's character in
the game.

The module provides functionalities such as:
- Creating a new character with a name, gender, race, and weapon.
- Validating user input for various character attributes.
- Displaying text with a typewriter effect for better user experience.
- Starting the character's race and weapon using corresponding factories.

Imports:
--------
- `Sword`, `Bow`, `Axe`, `Slingshot`: Weapon classes imported from the `weapons` module.
- `Ork`, `Goblin`, `Elf`, `Human`: Race classes imported from the `races` module.
- `Backpack`: The player's backpack class imported from the `backpack` module.
"""

import time

from weapons import Sword, Bow, Axe, Slingshot
from races import Ork, Goblin, Elf, Human
from backpack import Backpack


MAPPING = {
    "gender": ["M", "F"],
    "race": ["Ork", "Goblin", "Elf", "Human"],
    "weapon": ["Sword", "Bow", "Axe", "Slingshot"],
    "option": ["Yes", "No"]
}

RACE_FACTORY = {
    "ork": Ork,
    "goblin": Goblin,
    "elf": Elf,
    "human": Human
}

WEAPON_FACTORY = {
    "sword": Sword,
    "bow": Bow,
    "axe": Axe,
    "slingshot": Slingshot
}


class Character:
    """
    A class representing the player's character.

    Attributes
    ----------
    name : str
        The name of the character.
    gender : str
        The gender of the character (M/F).
    race : object
        The race object representing the character's race (Ork, Goblin, Elf, Human).
    weapon : object
        The weapon object representing the character's weapon (Sword, Bow, Axe, Slingshot).
    backpack : object
        The Backpack object where the character stores items.
    buff_time : list
        A list containing information about the character's buffs.
    violence : int
        The character's violence score, increasing with aggressive actions.

    Methods
    -------
    __str__():
        Returns a string representation of the character's details.
    start():
        Initializes the character's race and weapon using the respective factory.
    """

    def __init__(self, name, gender, race, weapon):
        """
        Initializes the character with the provided attributes.

        Parameters
        ----------
        name : str
            The name of the character.
        gender : str
            The gender of the character (M/F).
        race : str
            The race of the character (Ork, Goblin, Elf, Human).
        weapon : str
            The weapon the character will use (Sword, Bow, Axe, Slingshot).
        """
        self.name = name
        self.gender = gender
        self.race = race
        self.weapon = weapon
        self.backpack = Backpack()
        self.buff_time = [0, ""]
        self.violence = 0

    def __str__(self) -> str:
        """
        Returns a string representation of the character's details.

        Returns
        -------
        str
            A string describing the character's name, gender, race, and weapon.
        """
        return f"Your name =  {self.name}, gender = {self.gender}, race = {self.race}, weapon = {self.weapon}"

    def start(self) -> None:
        """
        Initializes the character's race and weapon using the respective factory.

        This method is called to assign a specific instance of the race and weapon classes
        to the character based on the provided race and weapon strings.

        Returns
        -------
        None
        """
        self.race = RACE_FACTORY.get(self.race.lower())()
        self.weapon = WEAPON_FACTORY.get(self.weapon.lower())()


def input_validation(var, validator) -> str:
    """
    Validates the input by checking if it exists in the provided list of valid options.

    Parameters
    ----------
    var : str
        The user input to be validated.
    validator : list
        A list of valid options that the input is compared against.

    Returns
    -------
    str
        The validated input.
    """
    validator_str = "/".join(validator)
    while var.capitalize() not in validator:
        print(f"{var} is not a valid argument!")
        var = input(f"Please input correct option : ({validator_str}) ")
    return var


def typewriter_effect(text, delay=0.04) -> None:
    """
    Simulates a typewriter effect for displaying text, with each character appearing at a fixed interval.

    Parameters
    ----------
    text : str
        The text to be displayed with the typewriter effect.
    delay : float, optional
        The delay between each character being printed (default is 0.04 seconds).

    Returns
    -------
    None
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def choose_stats() -> dict:
    """
    Prompts the user to input their character's name, gender, race, and weapon,
    and validates the input using predefined valid options.

    Returns
    -------
    dict
        A dictionary containing the chosen character stats (name, gender, race, weapon).
    """
    typewriter_effect("Welcome to the magical world! Choose your statistics!")
    name = input("But first, what is Your name: ")
    gender = input("What's your gender? (M/F) ")
    gender = input_validation(gender, MAPPING["gender"])
    race = input("Now, what race are You? (Ork/Goblin/Elf/Human) ")
    race = input_validation(race, MAPPING["race"])
    weapon = input("Lastly, what weapon will You choose? (Sword/Bow/Axe/Slingshot) ")
    weapon = input_validation(weapon, MAPPING["weapon"])

    print(f"Name = {name}, Gender = {gender}, Race = {race}, Weapon = {weapon}.")
    option = input("Is this correct? (Yes/No) ")
    option = input_validation(option, MAPPING["option"])
    if option == "No":
        choose_stats()
    return {"name": name, "gender": gender, "race": race, "weapon": weapon}


# Start of the main character creation process
stats = choose_stats()

main_character = Character(stats["name"], stats["gender"], stats["race"], stats["weapon"])
main_character.start()

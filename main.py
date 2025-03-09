"""
This module is part of a text-based adventure game where the player controls a character through various
combat encounters with different enemies.

Imports:
- `time`: Used for delaying actions and simulating a typewriter effect.
- `main_character`: The main character controlled by the player in the game.
- `Boar`, `Bear`, `Zombie`, `Werewolf`: Various enemy types that the character will face in battle.
- `is_d_o_t_active`, `is_buff_over`, `choose_and_use`, `noises_action`, `spare_or_kill`, `worst_fight`: Functions that
handle different aspects of combat and decision-making.

The gameplay involves fighting various enemies in sequential encounters, using different combat actions,
and advancing through a series of narrative events.
"""

import time
import sys

from characters import main_character
from enemies import Boar, Bear, Zombie, Werewolf
from fight import is_d_o_t_active, is_buff_over, choose_and_use, noises_action, spare_or_kill, worst_fight


def fighting_sequence(character, enemy, weapon_ability) -> str | None:
    """
    Handles the sequence of actions for a single combat round between the character and an enemy.

    Parameters
    ----------
    character
        The character who is engaging in combat.
    enemy
        The enemy that the character is fighting.
    weapon_ability
        The weapon ability currently being used by the character.

    Returns
    -------
    str or None
        A string indicating the result of the fight ("Won" or "Lost"), or None if the fight is ongoing.

    This function manages the cooldown of weapon abilities, checks whether the enemy has a damage-over-time
    (DOT) effect active, checks if the character's buff has expired, triggers enemy actions, and performs
    the appropriate combat action.
    """

    weapon_ability.current_cooldown -= 1
    character.buff_time[0] -= 1
    if over := is_d_o_t_active(enemy):
        return over
    if is_buff_over(character):
        print("Your buff just ended!")
        time.sleep(1)
    noises_action(enemy)
    return choose_and_use(character, enemy, weapon_ability)


def every_fight(enemy) -> str | None:
    """
    Runs the entire fight sequence with a given enemy until the fight is resolved.

    Parameters
    ----------
    enemy
        The enemy to fight against.

    Returns
    -------
    None
        This function does not return any value.

    This function repeatedly calls the `fighting_sequence` function until the result of the fight is "Won"
    or "Lost", and then it handles whether the character spares or kills the enemy after the fight.
    """
    time.sleep(2)
    is_over = True
    while is_over not in ["Won", "Lost"]:
        is_over = fighting_sequence(main_character, enemy, main_character.weapon.ability)

    spare_or_kill(main_character)


def print_info(msg) -> None:
    """
    Prints the character's stats along with an additional message.

    Parameters
    ----------
    msg : str
        The message to print alongside the stats.

    Returns
    -------
    None
        This function does not return any value.

    This function is used to display the character's stats and any relevant message in the game.
    """
    print("Your stats: ...")
    print(msg)


def box(msg) -> None:
    """
    Prints a message inside a box frame.

    Parameters
    ----------
    msg : str
        The message to display inside the box.

    Returns
    -------
    None
        This function does not return any value.

    This function is used to visually frame a message inside a box for better presentation during gameplay.
    """
    print("-" * (len(msg) + 8))
    print(f"|   {msg}   |")
    print("-" * (len(msg) + 8))


def typewriter_effect(text, delay=0.04) -> None:
    """
    Simulates a typewriter effect by printing text one character at a time with a delay.

    Parameters
    ----------
    text : str
        The text to print with the typewriter effect.
    delay : float, optional
        The time delay between each character (default is 0.04 seconds).

    Returns
    -------
    None
        This function does not return any value.

    This function mimics the sound and appearance of a typewriter by printing each character one at a time
    with a small delay between each one, making it ideal for displaying in-game dialogue or narration.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


if __name__ == "__main__":
    typewriter_effect("You are on a mission, Your goal is to retrieve something that is Yours. ")
    typewriter_effect("You land in a forest, surrounded by silence.")
    typewriter_effect("You look around and suddenly hear a strange noise. YOU HAVE TO FIGHT!")
    typewriter_effect("YOUR ENEMY IS A BOAR")
    box("TUTORIAL: Few options will show on your screen, choose one.")

    main_character.backpack.add_item("Small Health Potion")
    main_character.backpack.add_item("Big Attack Potion")

    every_fight(Boar)

    typewriter_effect("When you are walking, You notice on the floor a similar bracelet to Yours,")
    typewriter_effect("'I know I'm close', You say to Yourself.")
    typewriter_effect("While walking You find a Big Health Potion!")

    main_character.backpack.add_item("Big Health Potion")

    typewriter_effect("Suddenly, You hear a loud Growl. YOU HAVE TO FIGHT")
    typewriter_effect("YOUR ENEMY IS A BEAR")

    every_fight(Bear)

    if main_character.violence == 2:
        typewriter_effect("THE SILENCE IS OVERWHELMING. I WILL NOT STOP.")
        time.sleep(2)

    typewriter_effect("You notice a smoke not far from here.")
    typewriter_effect("'He must be there'")
    typewriter_effect("You walk towards it, but in your way you see someone, who NEEDS to be hurt.")
    typewriter_effect("YOUR ENEMY IS A ZOMBIE")

    every_fight(Zombie)

    if main_character.violence == 3:
        print("YOU CUT OF HIS LIMBS. NOW ONLY HEAD REMAINS. FINISH HIM.")
        worst_fight(Zombie)

    typewriter_effect("You finally arrived to the source of the smoke.")
    typewriter_effect("It's a small house.")
    typewriter_effect("As you go inside, You see something you never wished to.")
    typewriter_effect("YOUR ENEMY IS A WEREWOLF")

    every_fight(Werewolf)

    if main_character.violence == 4:
        typewriter_effect("THE WEREWOLF LOSES HIS POWER. HE TURNS INTO A HUMAN.")
        time.sleep(4)
        typewriter_effect("FINISH HIM, AS YOU DID THE REST.")
        time.sleep(4)
        worst_fight(Werewolf)
        typewriter_effect("I HAVE KILLED THEM ALL.")
        time.sleep(2)

    typewriter_effect("You did It.")
    time.sleep(2)
    typewriter_effect("You finally managed to find Him.")
    time.sleep(3)
    typewriter_effect("As You look at Him, You know it's Your SON.")
    time.sleep(3)

    if main_character.violence == 4:
        typewriter_effect("BUT. YOU DON'T. RECOGNIZE. YOURSELF.")
        time.sleep(3)

    typewriter_effect("As You walk forward to Hug him.")
    time.sleep(3)

    if main_character.violence == 4:
        typewriter_effect("You feel a sting.")
        time.sleep(2)
        typewriter_effect("YOU. HAVE. JUST. BEEN. STABBED.", delay=0.2)
        time.sleep(2)
        typewriter_effect("BY. YOUR. OWN. SON.", delay=0.2)
        time.sleep(2)
        typewriter_effect("WAS. IT. WORTH. IT.")
        time.sleep(3)
        typewriter_effect("As You bleed out. Your Son says to you: ")
        time.sleep(2)
        typewriter_effect("I. HATE. YOU.")
        time.sleep(2)
        typewriter_effect("GAME. OVER.")
        time.sleep(2)
        typewriter_effect("BAD ENDING")
        sys.exit(0)

    typewriter_effect("He hugs you back.")
    time.sleep(1)
    typewriter_effect("You were finally reunited.")
    time.sleep(2)
    typewriter_effect("It was worth it.")
    time.sleep(4)
    typewriter_effect("GOOD ENDING")

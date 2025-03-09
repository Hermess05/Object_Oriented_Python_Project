"""
Module that contains various functions for handling combat actions in a game.
This includes attacking, defending, using abilities, handling critical hits, and managing other combat-related actions.

Imports:
--------
- `random`: Provides various functions for generating random numbers. Used to simulate randomness in the combat system,
such as determining if an attack is dodged, critical, or if the enemy suffers from damage over time (DoT).

- `time`: Provides time-related functions, such as `sleep()`, used to create delays between different combat actions to
make the experience feel more realistic and interactive.

- `Backpack` (from the `backpack` module): The `Backpack` class is used to manage the player's inventory and allows the
character to choose and use items from their backpack during combat.
"""

import random
import time
import sys
from backpack import Backpack


def enemy_attack(character, enemy) -> None:
    """
    Simulates an attack from the enemy on the character.

    This function calculates the damage based on the enemy's stats, including critical hits,
    and updates the character's health accordingly.

    Parameters
    ----------
    character
        The character that is being attacked.
    enemy
        The enemy performing the attack.

    Returns
    -------
    None
    """
    enemy_dmg = enemy.damage
    chance = list(range(enemy.critical))
    if random.randint(0, 99) in chance:
        enemy_dmg *= 1.5
        print("Your enemy hits you with a critical!")
        time.sleep(1)
    if enemy_dmg // character.race.defence < character.race.hp:
        character.race.hp -= enemy_dmg // character.race.defence
    else:
        character.race.hp = 0
    print(f"They hit you with {enemy_dmg // character.race.defence} dmg, Your hp is now {character.race.hp}.")
    if character.race.hp == 0:
        print("YOU LOST")
        time.sleep(2)
        sys.exit(0)


def basic_attack(character, enemy) -> str | None:
    """
    Performs a basic attack from the character to the enemy.

    The attack can be dodged or critically hit. The function calculates the damage based
    on the character's stats and updates the enemy's health.

    Parameters
    ----------
    character
        The character performing the attack.
    enemy
        The enemy being attacked.

    Returns
    -------
    str | None
        A string indicating the result of the attack ("Won" if the enemy is defeated),
        or None if the battle continues.
    """
    my_dmg = character.race.damage + character.weapon.attack
    my_crit = list(range(character.weapon.critical))
    dodged = list(range(enemy.dodge))
    if random.randint(0, 99) in dodged:
        print("ENEMY dodged the attack")
        time.sleep(2)
        return "Dodge"
    if random.randint(0, 99) in my_crit:
        my_dmg *= 2
        print("YOU CRITICALLY HIT THE ENEMY")
        time.sleep(2)
    enemy.hp = enemy.hp - my_dmg // enemy.defence if enemy.hp > my_dmg // enemy.defence else 0
    print(f"You hit the enemy with {my_dmg // enemy.defence} DMG, enemy hp left: {enemy.hp}")
    time.sleep(2)
    if enemy.hp == 0:
        print("YOU WON!")
        time.sleep(2)
        return "Won"
    return None


def choosing_ability(weapon_ability) -> bool:
    """
    Prompts the user to choose whether to use an ability.

    Parameters
    ----------
    weapon_ability
        The ability that is being considered for use.

    Returns
    -------
    bool
        True if the player wants to use the ability, False otherwise.
    """
    print(weapon_ability)
    time.sleep(2)
    option = input("Do you want to use this ability? (Yes/No)  ")
    while option.lower() not in ["yes", "no"]:
        option = input("Please input the correct option. (Yes/No)  ")
    return option.lower() == "yes"


def use_ability(ability, enemy) -> str | None:
    """
    Uses the selected ability against the enemy.

    This method applies the ability's damage, debuffs, and applies the cooldown to the ability.

    Parameters
    ----------
    ability
        The ability being used by the character.
    enemy
        The enemy being attacked.

    Returns
    -------
    str | None
        "Won" if the enemy is defeated, "Stunned" if the enemy is stunned, or None if the battle continues.
    """
    print(f"You chose to use {ability.name}")
    enemy.hp = enemy.hp - ability.damage // enemy.defence if enemy.hp > ability.damage // enemy.defence else 0
    enemy.d_o_t = ability.d_o_t
    enemy.d_o_t_time = ability.d_o_t_time
    enemy.stun = ability.stun
    ability.current_cooldown = ability.cooldown
    time.sleep(1)
    print(f"You hit the enemy for {ability.damage // enemy.defence} damage, their hp is now {enemy.hp}")
    time.sleep(1)
    if enemy.hp == 0:
        print("YOU WON!")
        return "Won"
    if ability.damage_reduction > 0:
        enemy.damage -= ability.damage_reduction
        print(f"Your ability reduces enemy dmg! It's now {ability.damage_reduction} less")
        time.sleep(1)
    if enemy.stun > 0:
        print("Your enemy is stunned!")
        return "Stunned"
    return None


def is_d_o_t_active(enemy) -> str | None:
    """
    Checks if the enemy is suffering from damage over time (DoT).

    If the enemy is suffering from DoT, it applies the damage and updates the enemy's health.

    Parameters
    ----------
    enemy
        The enemy to check for DoT.

    Returns
    -------
    str | None
        "Won" if the enemy is defeated, or None if the DoT is still active.
    """
    if enemy.d_o_t_time > 0:
        enemy.hp = enemy.hp - enemy.d_o_t if enemy.hp > enemy.d_o_t else 0
        print(f"Enemy is suffering, They lost {enemy.d_o_t} hp, Their hp is now {enemy.hp}")
        enemy.d_o_t_time -= 1
        if enemy.hp == 0:
            print("YOU WON!")
            return "Won"
    return None


def is_buff_over(character) -> bool | None:
    """
    Checks if a character's buff has expired and resets their stats.

    Parameters
    ----------
    character
        The character whose buffs are being checked.

    Returns
    -------
    bool
        True if the buff is over, False otherwise.
    """
    if character.buff_time[0] or not character.buff_time[1]:
        return False
    if character.buff_time[0] == 0 and character.buff_time[1]:
        if character.buff_time[1] == "Attack":
            character.race.damage = character.race.max_damage
        elif character.buff_time[1] == "Defence":
            character.race.defence = character.race.max_defence
        character.buff_time[1] = ""
        return True
    return None


def is_ability_cooldown(ability) -> bool:
    """
    Checks if an ability is on cooldown.

    Parameters
    ----------
    ability
        The ability being checked for cooldown.

    Returns
    -------
    bool
        True if the ability is on cooldown, False otherwise.
    """
    if ability.current_cooldown > 0:
        print(
            f"The {ability.name} ability is on cooldown, You need to wait {ability.current_cooldown} turns to use it"
        )
        return True
    return False


def choose_item(character, enemy, weapon_ability) -> bool:
    """
    Allows the character to choose an item from their backpack and use it.

    Parameters
    ----------
    character
        The character choosing the item.
    enemy
        The enemy that the character is fighting.
    weapon_ability
        The ability that may be used after choosing the item.

    Returns
    -------
    bool
        True if an item was used, False otherwise.
    """
    character.backpack.show_items()
    pick = input("Type your item of choice, or 'No' if you don't want to use any item (Item name/No)")
    if pick == "No":
        choose_and_use(character, enemy, weapon_ability)
    for item in character.backpack.items:
        if pick == item.name:
            Backpack.use_item(character, pick)
            Backpack.delete_item(character.backpack, pick)
            return True
    print(f"{pick} - You don't have this item!")
    return False


def ability_action(character, enemy, weapon_ability) -> str | None:
    """
    Handles the action of using an ability, checking for cooldown and user input.

    Parameters
    ----------
    character
        The character using the ability.
    enemy
        The enemy being attacked.
    weapon_ability
        The weapon's ability being used.

    Returns
    -------
    str | None
        "Won" if the enemy is defeated, or None if the battle continues.
    """
    if is_ability_cooldown(weapon_ability):
        choose_and_use(character, enemy, weapon_ability)
    elif choosing_ability(weapon_ability):
        if output := use_ability(weapon_ability, enemy):
            return output
        return enemy_attack(character, enemy)
    return None


def defend_action(character, enemy) -> None:
    """
    Handles the defend action where the character increases their defense temporarily.

    Parameters
    ----------
    character
        The character defending.
    enemy
        The enemy attacking.

    Returns
    -------
    None
    """
    print("You decided to defend Yourself against your opponents attack. Great choice!")
    character.race.defence *= 2
    time.sleep(2)
    return enemy_attack(character, enemy)


def noises_action(enemy) -> None:
    """
    Plays a random noise made by the enemy.

    Parameters
    ----------
    enemy
        The enemy making the noise.

    Returns
    -------
    None
    """
    if random.randint(0, 99) < 50:
        print(enemy.noises[random.randint(0, 2)])


def spare_or_kill(character) -> None:
    """
    Prompts the player to either spare or kill the enemy.

    Parameters
    ----------
    character
        The character deciding the fate of the enemy.

    Returns
    -------
    None
    """
    choose = input("Would you like to SPARE Their life, or KILL them for all the harm They've done? ")
    if choose.lower() == "spare":
        print("You decided to walk further, Your enemy thanks you.")
    elif choose.lower() == "kill":
        character.violence += 1
        print(f"YOUR VIOLENCE SCORE IS NOW {character.violence}")


def worst_fight(enemy) -> None:
    """
    Handles the worst fight scenario, where the enemy taunts and the character must attack.

    Parameters
    ----------
    enemy
        The enemy in the fight.

    Returns
    -------
    None
    """
    for voice in enemy.get_voices():
        input("ATTACK ")
        print("YOU ARE DOING THE RIGHT THING.")
        time.sleep(1)
        print(voice)
        time.sleep(2)
    print("AS YOU DEALT THE FINAL BLOW, YOU FEEL MORE PEACEFUL.")
    time.sleep(3)


def choose_and_use(character, enemy, weapon_ability) -> str | None:
    """
    Prompts the user to choose between different actions: Attack, Defend, Ability, or Item.

    Parameters
    ----------
    character
        The character performing the action.
    enemy
        The enemy being interacted with.
    weapon_ability
        The weapon's ability to be used.

    Returns
    -------
    str | None
        The outcome of the action ("Won" if the enemy is defeated, or None if the battle continues).
    """
    choose = input("Attack  /  Defend  /  Ability  /  Item")
    if choose.lower() == "attack":
        did_won = basic_attack(character, enemy)
        return did_won if did_won == "Won" else enemy_attack(character, enemy)
    if choose.lower() == "defend":
        defend_action(character, enemy)
        character.race.defence *= 0.5
        return None
    if choose.lower() == "ability" and (outcome := ability_action(character, enemy, weapon_ability)):
        return outcome
    if choose.lower() == "item" and choose_item(character, enemy, weapon_ability):
        return enemy_attack(character, enemy)
    print("Wrong input, please input correctly one of the options.")
    choose_and_use(character, enemy, weapon_ability)
    return None

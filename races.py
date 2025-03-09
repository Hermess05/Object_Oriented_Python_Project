"""
Module for defining different races in the game.

This module contains the base class `Race` and its subclasses representing
various races that players can choose in the game. Each race has attributes such as
maximum health, current health, maximum damage, damage, maximum defense, and defense.

Classes:
--------
- Race: A base class representing common attributes for all races.
- Ork: A subclass of `Race` representing the Ork race with specific stats.
- Goblin: A subclass of `Race` representing the Goblin race with specific stats.
- Elf: A subclass of `Race` representing the Elf race with specific stats.
- Human: A subclass of `Race` representing the Human race with specific stats.

Usage:
------
Each race class initializes with specific attributes that define the character's
stats, such as health, damage, and defense. Players can choose from these races
when creating their character.

Example:
--------
# Create an instance of Human race
human = Human()
print(human)
"""


class Race:
    """
    A class representing a character race in the game.

    Attributes
    ----------
    max_hp : int
        The maximum health points for this race.
    hp : int
        The current health points of the character.
    max_damage : int
        The maximum damage this race can deal.
    damage : int
        The current damage dealt by the character.
    max_defence : float
        The maximum defense of the character.
    defence : float
        The current defense of the character.

    Methods
    -------
    __str__() -> str
        Returns a string representation of the race attributes, including HP, damage, and defense.
    """

    def __init__(self, max_hp, hp, max_damage, damage, max_defence, defence):
        """
        Initializes a race with specific attributes.

        Parameters
        ----------
        max_hp : int
            The maximum health points of the race.
        hp : int
            The current health points of the character.
        max_damage : int
            The maximum damage this race can deal.
        damage : int
            The current damage dealt by the character.
        max_defence : float
            The maximum defense of the character.
        defence : float
            The current defense of the character.
        """
        self.max_hp = max_hp
        self.hp = hp
        self.max_damage = max_damage
        self.damage = damage
        self.max_defence = max_defence
        self.defence = defence

    def __str__(self) -> str:
        """
        Returns a string representation of the race's attributes.

        Returns
        -------
        str
            A formatted string containing the race's HP, damage, and defense.
        """
        return (f"Your {self.__class__.__name__} attributes: HP = {self.hp}, "
                f"Damage = {self.damage}, Defence = {self.defence}")


class Ork(Race):
    """
    A subclass of `Race` representing the Ork race.

    The Ork race has higher HP and damage, making them powerful in combat.

    Methods
    -------
    __init__() -> None
        Initializes the Ork race with predefined attributes.
    """

    def __init__(self):
        """
        Initializes the Ork race with predefined attributes.

        The Ork has 2200 HP, 10 damage, 1.8 defense, and the same maximum values for damage and defense.
        """
        super().__init__(
            max_hp=2200,
            hp=2200,
            max_damage=10,
            damage=10,
            max_defence=1.8,
            defence=1.8
        )


class Goblin(Race):
    """
    A subclass of `Race` representing the Goblin race.

    The Goblin race has lower HP but higher damage compared to other races.

    Methods
    -------
    __init__() -> None
        Initializes the Goblin race with predefined attributes.
    """

    def __init__(self):
        """
        Initializes the Goblin race with predefined attributes.

        The Goblin has 170 HP, 15 damage, 1.3 defense, and the same maximum values for damage and defense.
        """
        super().__init__(
            max_hp=170,
            hp=170,
            max_damage=15,
            damage=15,
            max_defence=1.3,
            defence=1.3
        )


class Elf(Race):
    """
    A subclass of `Race` representing the Elf race.

    The Elf race has moderate HP and damage but slightly higher defense.

    Methods
    -------
    __init__() -> None
        Initializes the Elf race with predefined attributes.
    """

    def __init__(self):
        """
        Initializes the Elf race with predefined attributes.

        The Elf has 190 HP, 13 damage, 1.4 defense, and the same maximum values for damage and defense.
        """
        super().__init__(
            max_hp=190,
            hp=190,
            max_damage=13,
            damage=13,
            max_defence=1.4,
            defence=1.4
        )


class Human(Race):
    """
    A subclass of `Race` representing the Human race.

    The Human race has balanced stats with moderate HP, damage, and defense.

    Methods
    -------
    __init__() -> None
        Initializes the Human race with predefined attributes.
    """

    def __init__(self):
        """
        Initializes the Human race with predefined attributes.

        The Human has 200 HP, 11 damage, 1.5 defense, and the same maximum values for damage and defense.
        """
        super().__init__(
            max_hp=200,
            hp=200,
            max_damage=11,
            damage=11,
            max_defence=1.5,
            defence=1.5
        )

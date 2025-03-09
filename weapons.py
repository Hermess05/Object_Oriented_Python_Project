"""
This module defines various weapon classes used in the game. Each weapon has specific attributes such as attack power,
critical hit chance,
and a special ability that can be used during combat. The weapons available in this module include:
- Sword
- Bow
- Axe
- Slingshot

Each weapon has a unique attack value, critical chance, and a corresponding ability which is defined in the `abilities`
module.

Imports:
--------
- `TripleCut`, `BurningArrow`, `Axerang`, `MeatShot`: Special abilities for each weapon imported from the
`abilities` module.
"""

from abilities import TripleCut, BurningArrow, Axerang, MeatShot


class Weapons:
    """
    A base class representing a weapon with basic attributes like attack, critical chance, and a special ability.

    Attributes
    ----------
    attack : int
        The base attack power of the weapon.
    critical : int
        The chance for the weapon to land a critical hit.
    ability : object
        The special ability associated with the weapon.
    """

    def __init__(self, attack, critical, ability):
        """
        Initializes a weapon with attack, critical chance, and a special ability.

        Parameters
        ----------
        attack : int
            The base attack power of the weapon.
        critical : int
            The critical hit chance of the weapon.
        ability : object
            The special ability of the weapon.
        """
        self.attack = attack
        self.critical = critical
        self.ability = ability


class Sword(Weapons):
    """
    A class representing a Sword weapon.

    Inherits from the `Weapons` class and sets specific attributes for the Sword weapon: attack power, critical chance,
    and ability.

    Attributes
    ----------
    attack : int
        The base attack power of the sword (15).
    critical : int
        The critical hit chance of the sword (30%).
    ability : object
        The special ability of the sword (`TripleCut`).
    """

    def __init__(self):
        """
        Initializes the Sword with predefined attack, critical chance, and special ability (`TripleCut`).
        """
        super().__init__(
            attack=15,
            critical=30,
            ability=TripleCut()
        )


class Bow(Weapons):
    """
    A class representing a Bow weapon.


    Inherits from the `Weapons` class and sets specific attributes for the Bow weapon: attack power, critical chance,
    and ability.

    Attributes
    ----------
    attack : int
        The base attack power of the bow (13).
    critical : int
        The critical hit chance of the bow (40%).
    ability : object
        The special ability of the bow (`BurningArrow`).
    """

    def __init__(self):
        """
        Initializes the Bow with predefined attack, critical chance, and special ability (`BurningArrow`).
        """
        super().__init__(
            attack=13,
            critical=40,
            ability=BurningArrow()
        )


class Axe(Weapons):
    """
    A class representing an Axe weapon.


    Inherits from the `Weapons` class and sets specific attributes for the Axe weapon: attack power, critical chance,
    and ability.

    Attributes
    ----------
    attack : int
        The base attack power of the axe (20).
    critical : int
        The critical hit chance of the axe (15%).
    ability : object
        The special ability of the axe (`Axerang`).
    """

    def __init__(self):
        """
        Initializes the Axe with predefined attack, critical chance, and special ability (`Axerang`).
        """
        super().__init__(
            attack=20,
            critical=15,
            ability=Axerang()
        )


class Slingshot(Weapons):
    """
    A class representing a Slingshot weapon.

    Inherits from the `Weapons` class and sets specific attributes for the Slingshot weapon: attack power,
    critical chance, and ability.

    Attributes
    ----------
    attack : int
        The base attack power of the slingshot (11).
    critical : int
        The critical hit chance of the slingshot (50%).
    ability : object
        The special ability of the slingshot (`MeatShot`).
    """

    def __init__(self):
        """
        Initializes the Slingshot with predefined attack, critical chance, and special ability (`MeatShot`).
        """
        super().__init__(
            attack=11,
            critical=50,
            ability=MeatShot()
        )

"""
Module for defining enemy types and their attributes.

This module contains the `Enemies` base class and several subclasses that represent
different types of enemies in the game. Each enemy has specific attributes such as
health points (HP), damage, defense, critical chance, dodge chance, damage over time,
and special noises they make during combat.

Classes:
--------
- Enemies: A base class for representing common attributes and methods for enemies.
- Enemy1: A subclass representing the first type of enemy with specific attributes.
- Enemy2: A subclass representing the second type of enemy with specific attributes.
- Enemy3: A subclass representing the third type of enemy with specific attributes.
- Enemy4: A subclass representing the fourth type of enemy with specific attributes.

Usage:
------
Each enemy class initializes with predefined attributes that describe their combat behavior.
Instances of these enemies can be used in the game to challenge the player.

Example:
--------
# Create an instance of Enemy3 (Zombie)
zombie = Zombie()
print(zombie.hp)  # Output: 110
"""


class Enemies:
    """
    A base class representing an enemy with common attributes and behavior.

    Attributes
    ----------
    hp : int
        The health points of the enemy.
    damage : int
        The base damage the enemy deals.
    defence : float
        The defense value that reduces damage taken.
    critical : int
        The chance of a critical hit in percentage.
    dodge : int
        The chance of dodging an incoming attack in percentage.
    d_o_t : int
        The amount of damage dealt over time (damage over time).
    d_o_t_time : int
        The duration for which damage over time is applied.
    noises : list
        A list of strings representing noises the enemy makes.

    Methods
    -------
    __init__(self, hp, damage, defence, critical, dodge, d_o_t, d_o_t_time, noises)
        Initializes the enemy with specified attributes.
    """
    def __init__(self, hp, damage, defence, critical, dodge, d_o_t, d_o_t_time, noises):
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.critical = critical
        self.dodge = dodge
        self.d_o_t = d_o_t
        self.d_o_t_time = d_o_t_time
        self.noises = noises


class Enemy1(Enemies):
    """
    A subclass representing Enemy1, with specific attributes for this enemy type.

    Inherits from Enemies and initializes with predefined values for health, damage,
    defense, critical chance, dodge, and noises.

    Methods
    -------
    __init__(self)
        Initializes Enemy1 with predefined attributes.
    """
    def __init__(self):
        super().__init__(
            hp=100,
            damage=25,
            defence=1.1,
            critical=20,
            dodge=15,
            d_o_t=0,
            d_o_t_time=0,
            noises=["*growls at you*", "*loud squealing*", "*grunts*"]
        )


class Enemy2(Enemies):
    """
    A subclass representing Enemy2, with specific attributes for this enemy type.

    Inherits from Enemies and initializes with predefined values for health, damage,
    defense, critical chance, dodge, and noises.

    Methods
    -------
    __init__(self)
        Initializes Enemy2 with predefined attributes.
    """
    def __init__(self):
        super().__init__(
            hp=150,
            damage=22,
            defence=1.2,
            critical=25,
            dodge=5,
            d_o_t=0,
            d_o_t_time=0,
            noises=["*huffs at you*", "*loud growl*", "*roars*"]
        )


class Enemy3(Enemies):
    """
    A subclass representing Enemy3 (Zombie), with specific attributes for this enemy type.

    Inherits from Enemies and initializes with predefined values for health, damage,
    defense, critical chance, dodge, and noises. This class also provides a method for
    getting specific voices for the zombie.

    Methods
    -------
    __init__(self)
        Initializes Enemy3 (Zombie) with predefined attributes.
    get_voices()
        Returns a list of specific voices for the zombie enemy.
    """
    def __init__(self):
        super().__init__(
            hp=110,
            damage=18,
            defence=1.1,
            critical=25,
            dodge=20,
            d_o_t=0,
            d_o_t_time=0,
            noises=["*screams*", "*loudly hisses*", "*growls silently*"]
        )

    @staticmethod
    def get_voices():
        """
        Returns a list of voices specific to the zombie enemy.

        Returns
        -------
        list
            A list of strings representing the zombie's voices.
        """
        return ["'I-I--'", "'I-I-Onl-y-'", "'W-W-Wan-ted-'", "'T-T-To-'", "'P-P-Pro-te-c--'"]


class Enemy4(Enemies):
    """
    A subclass representing Enemy4 (Werewolf), with specific attributes for this enemy type.

    Inherits from Enemies and initializes with predefined values for health, damage,
    defense, critical chance, dodge, and noises. This class also provides a method for
    getting specific voices for the werewolf.

    Methods
    -------
    __init__(self)
        Initializes Enemy4 (Werewolf) with predefined attributes.
    get_voices()
        Returns a list of specific voices for the werewolf enemy.
    """
    def __init__(self):
        super().__init__(
            hp=110,
            damage=18,
            defence=1.1,
            critical=25,
            dodge=20,
            d_o_t=0,
            d_o_t_time=0,
            noises=["*howls*", "*screams loudly*", "*growls painfully*"]
        )

    @staticmethod
    def get_voices():
        """
        Returns a list of voices specific to the werewolf enemy.

        Returns
        -------
        list
            A list of strings representing the werewolf's voices.
        """
        return ["'PLEASE.'", "'DON'T DO THIS.'", "'I AM.'", "'HIS ONLY.'", "'HOPE.'"]


# Example of creating enemy instances
Boar = Enemy1()
Bear = Enemy2()
Zombie = Enemy3()
Werewolf = Enemy4()

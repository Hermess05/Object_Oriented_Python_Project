"""
Module for defining various abilities in the game.

This module contains the `Abilities` class and its subclasses, which represent
different abilities used by characters in combat. Each ability has attributes such
as damage, cooldown, damage over time, and effects like damage reduction and stun.

Imports:
--------
- `random`: Used to generate random numbers for various game mechanics like chance calculations.
- `time`: Used to introduce delays (pauses) in the game flow for better user experience.

Classes:
--------
- Abilities: A base class for representing abilities with common properties.
- TripleCut: A subclass representing a specific ability that causes damage and applies
  damage over time.
- BurningArrow: A subclass representing a ranged attack that causes burn damage over time.
- Axerang: A subclass representing an ability where an axe is thrown like a boomerang,
  causing damage and stunning the enemy.
- MeatShot: A subclass representing an ability where the player shoots meat, causing damage.

Usage:
------
Each ability class initializes with specific attributes like damage, cooldown time, damage
over time, and effects like stun or damage reduction. Instances of these abilities can be
used in the game to perform combat actions.

Example:
--------
# Create an instance of BurningArrow
burning_arrow = BurningArrow()
print(burning_arrow)
"""


class Abilities:
    """
    A class representing an ability in the game, including its properties and effects.

    Attributes
    ----------
    name : str
        The name of the ability.
    damage : int
        The base damage of the ability.
    cooldown : int
        The cooldown time in rounds before the ability can be used again.
    current_cooldown : int
        The current cooldown status, initially set to 0.
    description : str
        A description of the ability and its effects.
    d_o_t : int
        The amount of damage dealt over time (damage over time).
    d_o_t_time : int
        The duration (in rounds) for which damage over time occurs.
    damage_reduction : int
        The amount of damage reduction provided by the ability.
    stun : int
        The number of rounds the enemy will be stunned after using the ability.

    Methods
    -------
    __str__()
        Returns a string representation of the ability.
    """

    def __init__(self, name: str, damage, cooldown, description, d_o_t, d_o_t_time, damage_reduction, stun):
        """
        Initializes an ability with specified attributes.

        Parameters
        ----------
        name : str
            The name of the ability.
        damage : int
            The base damage of the ability.
        cooldown : int
            The cooldown time before the ability can be used again.
        description : str
            A brief description of the ability.
        d_o_t : int
            The amount of damage dealt over time (damage over time).
        d_o_t_time : int
            The duration (in rounds) for which damage over time is applied.
        damage_reduction : int
            The amount of damage reduction provided by the ability.
        stun : int
            The number of rounds the enemy is stunned after the ability is used.
        """
        self.name = name
        self.damage = damage
        self.cooldown = cooldown
        self.current_cooldown = 0
        self.description = description
        self.d_o_t = d_o_t
        self.d_o_t_time = d_o_t_time
        self.damage_reduction = damage_reduction
        self.stun = stun

    def __str__(self) -> str:
        """
        Returns a string representation of the ability, including its properties.

        Returns
        -------
        str
            A formatted string containing the name, damage, cooldown, damage over time,
            damage reduction, stun duration, and description of the ability.
        """
        return f"""
        Name = {self.name}
        Damage = {self.damage}
        Cooldown = {self.cooldown}
        Damage Over Time = {self.d_o_t}, for {self.d_o_t_time} rounds
        Damage reduction = {self.damage_reduction}
        Stun = {self.stun}
        Description = {self.description}
        """


class TripleCut(Abilities):
    """
    A class representing the 'Triple Cut' ability, a specialized attack that causes
    damage and applies a damage over time effect.

    Methods
    -------
    __init__()
        Initializes the 'Triple Cut' ability with its properties.
    """

    def __init__(self):
        """
        Initializes the 'Triple Cut' ability with predefined attributes.

        The 'Triple Cut' ability causes 33 damage, applies 3 damage per round for 6 rounds,
        reduces incoming damage by 3, and has a cooldown of 3 rounds.
        """
        super().__init__(
            name="Triple Cut",
            damage=33,
            cooldown=3,
            description="Cut Your opponent in three places. Make them bleed.",
            d_o_t=3,
            d_o_t_time=6,
            damage_reduction=3,
            stun=0
        )


class BurningArrow(Abilities):
    """
    A class representing the 'Burning Arrow' ability, which sets the enemy on fire.

    Methods
    -------
    __init__()
        Initializes the 'Burning Arrow' ability with its properties.
    """

    def __init__(self):
        """
        Initializes the 'Burning Arrow' ability with predefined attributes.

        The 'Burning Arrow' ability causes 25 damage and applies 5 damage per round for 3 rounds,
        with no damage reduction and no stun. The cooldown is 4 rounds.
        """
        super().__init__(
            name="Burning Arrow",
            damage=25,
            cooldown=4,
            description="Set fire to your arrow, and set Your enemy ablaze!",
            d_o_t=5,
            d_o_t_time=3,
            damage_reduction=0,
            stun=0
        )


class Axerang(Abilities):
    """
    A class representing the 'Axerang' ability, which throws an axe like a boomerang to break the enemy's bones.

    Methods
    -------
    __init__()
        Initializes the 'Axerang' ability with its properties.
    """

    def __init__(self):
        """
        Initializes the 'Axerang' ability with predefined attributes.

        The 'Axerang' ability causes 35 damage, reduces incoming damage by 5, stuns the enemy for 1 round,
        and has a cooldown of 5 rounds. This ability does not apply damage over time.
        """
        super().__init__(
            name="Axerang",
            damage=35,
            cooldown=5,
            description="Throw Your axe into the enemy like a boomerang and break their bones!",
            d_o_t=0,
            d_o_t_time=0,
            damage_reduction=5,
            stun=1
        )


class MeatShot(Abilities):
    """
    A class representing the 'Meat Shot' ability, which shoots meat at the enemy and summons dogs to help.

    Methods
    -------
    __init__()
        Initializes the 'Meat Shot' ability with its properties.
    """

    def __init__(self):
        """
        Initializes the 'Meat Shot' ability with predefined attributes.

        The 'Meat Shot' ability causes 45 damage and has a very long cooldown (999 rounds).
        It does not apply damage over time, reduce damage, or stun the enemy.
        """
        super().__init__(
            name="Meat Shot",
            damage=45,
            cooldown=999,
            description="Shoot some meat at the enemy, let the dogs take care of them!",
            d_o_t=0,
            d_o_t_time=0,
            damage_reduction=0,
            stun=0
        )

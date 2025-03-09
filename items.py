"""
Module for defining various item classes used in the game.

This module contains a set of item classes that represent different types of potions
such as health, defense, and attack potions. Each class inherits from the base class `Items`,
which defines common attributes for all items, such as name, description, group, and effects
(e.g., how much health, defense, or attack the potion grants).

Classes
--------
Items : object
    A base class that defines common properties for all items.
SmallHealthPotion : Items
    A class representing a small health potion.
BigHealthPotion : Items
    A class representing a large health potion.
SmallDefencePotion : Items
    A class representing a small defense potion.
BigDefencePotion : Items
    A class representing a large defense potion.
SmallAttackPotion : Items
    A class representing a small attack potion.
BigAttackPotion : Items
    A class representing a large attack potion.
"""


class Items:
    """
    A base class for all items.

    This class is used to define common attributes for all items, such as the name, description,
    group, and how much effect they have.

    Attributes
    ----------
    name : str
        The name of the item.
    description : str
        A brief description of the item.
    group : str
        The group that the item belongs to (e.g., Health Potions, Attack Potions).
    how_much : list
        A list that defines the effect of the item. Typically, it will include [effect, duration].
    """

    def __init__(self, name, description, group, how_much):
        """
        Constructs all the necessary attributes for the item.

        Parameters
        ----------
        name : str
            The name of the item.
        description : str
            A brief description of the item.
        group : str
            The group that the item belongs to (e.g., Health Potions, Attack Potions).
        how_much : list
            A list that defines the effect of the item. Typically, it will include [effect, duration].
        """
        self.name = name
        self.description = description
        self.group = group
        self.how_much = how_much


class SmallHealthPotion(Items):
    """
    A class representing a small health potion.

    This potion heals the player for a small amount of health.

    Inherits from the Items class.

    Attributes
    ----------
    name : str
        The name of the potion ("Small Health Potion").
    description : str
        A description of the potion's effects.
    group : str
        The group to which the potion belongs ("Health Potions").
    how_much : list
        A list specifying the healing amount and duration. Heals 30 HP with no duration effect.
    """

    def __init__(self):
        """
        Initializes the SmallHealthPotion with specific attributes.

        The Small Health Potion heals the player for 30 HP with no duration effect.
        """
        super().__init__(
            name="Small Health Potion",
            description="Heals you for 30 HP, drink it while you can!",
            group="Health Potions",
            how_much=[30, 0]
        )


class BigHealthPotion(Items):
    """
    A class representing a big health potion.

    This potion heals the player for a large amount of health.

    Inherits from the Items class.

    Attributes
    ----------
    name : str
        The name of the potion ("Big Health Potion").
    description : str
        A description of the potion's effects.
    group : str
        The group to which the potion belongs ("Health Potions").
    how_much : list
        A list specifying the healing amount and duration. Heals 50 HP with no duration effect.
    """

    def __init__(self):
        """
        Initializes the BigHealthPotion with specific attributes.

        The Big Health Potion heals the player for 50 HP with no duration effect.
        """
        super().__init__(
            name="Big Health Potion",
            description="Heals you for 50 HP, that's a lot!",
            group="Health Potions",
            how_much=[50, 0]
        )


class SmallDefencePotion(Items):
    """
    A class representing a small defense potion.

    This potion grants a small amount of defense to the player for a limited number of rounds.

    Inherits from the Items class.

    Attributes
    ----------
    name : str
        The name of the potion ("Small Defence Potion").
    description : str
        A description of the potion's effects.
    group : str
        The group to which the potion belongs ("Defence Potions").
    how_much : list
        A list specifying the defense boost amount and duration. Grants 0.3 defense for 3 rounds.
    """

    def __init__(self):
        """
        Initializes the SmallDefencePotion with specific attributes.

        The Small Defence Potion grants 0.3 additional defense for 3 rounds.
        """
        super().__init__(
            name="Small Defence Potion",
            description="Grants you a small amount of additional defence for 3 rounds, enjoy it!",
            group="Defence Potions",
            how_much=[0.3, 3]
        )


class BigDefencePotion(Items):
    """
    A class representing a big defense potion.

    This potion grants a large amount of defense to the player for a limited number of rounds.

    Inherits from the Items class.

    Attributes
    ----------
    name : str
        The name of the potion ("Big Defence Potion").
    description : str
        A description of the potion's effects.
    group : str
        The group to which the potion belongs ("Defence Potions").
    how_much : list
        A list specifying the defense boost amount and duration. Grants 0.5 defense for 3 rounds.
    """

    def __init__(self):
        """
        Initializes the BigDefencePotion with specific attributes.

        The Big Defence Potion grants 0.5 additional defense for 3 rounds.
        """
        super().__init__(
            name="Big Defence Potion",
            description="Grants you a big amount of defence for 3 rounds, this will feel good!",
            group="Defence Potions",
            how_much=[0.5, 3]
        )


class SmallAttackPotion(Items):
    """
    A class representing a small attack potion.

    This potion gives the player a small attack boost for a limited number of rounds.

    Inherits from the Items class.

    Attributes
    ----------
    name : str
        The name of the potion ("Small Attack Potion").
    description : str
        A description of the potion's effects.
    group : str
        The group to which the potion belongs ("Attack Potions").
    how_much : list
        A list specifying the attack boost amount and duration. Grants 5 attack for 3 rounds.
    """

    def __init__(self):
        """
        Initializes the SmallAttackPotion with specific attributes.

        The Small Attack Potion grants 5 additional attack for 3 rounds.
        """
        super().__init__(
            name="Small Attack Potion",
            description="Gives you a little more attack, You need this!",
            group="Attack Potions",
            how_much=[5, 3]
        )


class BigAttackPotion(Items):
    """
    A class representing a big attack potion.

    This potion gives the player a large attack boost for a limited number of rounds.

    Inherits from the Items class.

    Attributes
    ----------
    name : str
        The name of the potion ("Big Attack Potion").
    description : str
        A description of the potion's effects.
    group : str
        The group to which the potion belongs ("Attack Potions").
    how_much : list
        A list specifying the attack boost amount and duration. Grants 10 attack for 3 rounds.
    """

    def __init__(self):
        """
        Initializes the BigAttackPotion with specific attributes.

        The Big Attack Potion grants 10 additional attack for 3 rounds.
        """
        super().__init__(
            name="Big Attack Potion",
            description="Grants you a huge attack boost, You will feel stronger!",
            group="Attack Potions",
            how_much=[10, 3]
        )

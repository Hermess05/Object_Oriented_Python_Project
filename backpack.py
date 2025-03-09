"""
This module provides functionality for managing a player's backpack and items.
It allows adding, removing, and using items such as potions (Health, Defence, Attack) that can be utilized
during gameplay.

The module includes:
- A `Backpack` class to handle the backpack's functionality.
- A mapping of different item types such as `SmallHealthPotion`, `BigHealthPotion`, `SmallDefencePotion`, etc.,
which are created in the `items` module.

Imports:
--------
- `items`: The module where item classes like `SmallHealthPotion`, `BigHealthPotion`, etc., are defined.
"""


import items

MAPPING = {
    "Small Health Potion": items.SmallHealthPotion(),
    "Big Health Potion": items.BigHealthPotion(),
    "Small Defence Potion": items.SmallDefencePotion(),
    "Big Defence Potion": items.BigDefencePotion(),
    "Small Attack Potion": items.SmallAttackPotion(),
    "Big Attack Potion": items.BigAttackPotion(),
}


class Backpack:
    """
    Class representing a player's backpack.

    The backpack holds a collection of items that the player can add, remove, or use.
    It has a limited capacity and supports functionalities to manage items.
    """

    def __init__(self):
        """
        Initializes the Backpack with an empty item list.
        """
        self.items = []

    def add_item(self, item_name) -> bool:
        """
        Adds an item to the backpack.

        Parameters
        ----------
        item_name : str
            The name of the item to be added to the backpack.

        Returns
        -------
        bool
            True if the item was successfully added, False if the backpack is full.
        """
        if len(self.items) >= 5:
            print("Backpack is full!")
            return False
        if item := MAPPING.get(item_name):
            self.items.append(item)
            print(f"Item {item_name} successfully added to your backpack!")
        return True

    def delete_item(self, item_name) -> None:
        """
        Deletes an item from the backpack.

        Parameters
        ----------
        item_name : str
            The name of the item to be removed from the backpack.
        """
        self.items.remove(MAPPING.get(item_name))

    def show_items(self) -> None:
        """
        Displays all the items currently in the backpack.

        If the backpack contains items, it lists each item's name and description.
        Otherwise, it informs the user that the backpack is empty.
        """
        if self.items:
            print("Backpack contains: ")
            for item in self.items:
                print(f"  - {item.name} : {item.description}")
        else:
            print("Backpack is empty!")

    @staticmethod
    def use_item(character, item_name) -> None:
        """
        Uses an item from the backpack on the character.

        The effect of the item depends on its type (health, attack, or defense).
        Health potions restore HP, while attack and defense potions modify the character's stats.

        Parameters
        ----------
        character
            The character who will use the item.
        item_name : str
            The name of the item to be used.
        """
        item = MAPPING.get(item_name)
        if item.group == "Health Potions":
            character.race.hp += item.how_much[0]
            print(f"You just used {item.name}, you restored {item.how_much[0]} hp!")
        else:
            character.buff_time[0] = item.how_much[1]
            match item.group:
                case "Attack Potions":
                    character.buff_time[1] = "Attack"
                    character.race.damage += item.how_much[0]
                case "Defence Potions":
                    character.buff_time[1] = "Defence"
                    character.race.defence += item.how_much[0]
            print(
                f"You just used {item.name}, your {character.buff_time[1]} is now enlarged by {character.buff_time[0]}"
            )

from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character"""
    first_name: str
    is_alive: bool

    def __init__(self, first_name, is_alive: bool = True):
        """
        Inits the class' fields with first_name and is_alive.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to override."""
        pass

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return self.__str__()


class Stark(Character):
    """Inherited from Character child class."""
    def die(self):
        """Sets the character's alive status to False."""
        self.is_alive = False

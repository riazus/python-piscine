from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """
    family_name = "Baratheon"
    eyes: str
    hairs: str

    def __init__(self, first_name, is_alive: bool = True,
                 eyes: str = "brown", hairs: str = "dark"):
        """
        Inits the class' fields with first_name, is_alive, eyes, hairs
        """
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Sets the character's alive status to False."""
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.
    """
    family_name = "Lannister"
    eyes: str
    hairs: str

    def __init__(self, first_name, is_alive: bool = True,
                 eyes: str = "blue", hairs: str = "light"):
        """
        Inits the class' fields with first_name, is_alive, eyes, hairs
        """
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Sets the character's alive status to False."""
        self.is_alive = False

    @classmethod
    def create_lannister(self, first_name, is_alive,
                         eyes: str = "blue", hairs: str = "light"):
        """
        Create a Lannister character instance with custom is_alive status.
        """
        instance = self(first_name)
        instance.is_alive = is_alive
        instance.eyes = eyes
        instance.hairs = hairs
        return instance

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King class"""
    def __init__(self, first_name, is_alive: bool = True,
                 eyes: str = "brown", hairs: str = "dark"):
        """
        Inits the class' fields with first_name, is_alive, eyes, hairs
        """
        super().__init__(first_name, is_alive, eyes, hairs)

    def set_eyes(self, eyes):
        """Set new eyes' color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set new hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """Gets current eyes"""
        return self.eyes

    def get_hairs(self):
        """Gets current hairs"""
        return self.hairs

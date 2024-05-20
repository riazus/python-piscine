class calculator:
    """Simple calculator"""
    vector: list

    def __init__(self, vector: list) -> None:
        """Inits the class' vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Overloaded addition operator"""
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] + object
        print(self.vector)

    def __mul__(self, object) -> None:
        """Overloaded multiplication operator"""
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] * object
        print(self.vector)

    def __sub__(self, object) -> None:
        """Overloaded subtraction operator"""
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] - object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Overloaded division operator"""
        for i in range(len(self.vector)):
            if object == 0:
                raise ZeroDivisionError("Zero division is not allowed")
            self.vector[i] = self.vector[i] / object
        print(self.vector)

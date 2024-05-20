class calculator:
    """Calculator for two vectors"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiplies values of each vector by index"""
        dot_product = 0.0
        i = 0
        while i < len(V1):
            dot_product += V1[i] * V2[i]
            i += 1
        print(f"Dot product is: {int(dot_product)}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds values of each vector by index"""
        res = []
        i = 0
        while i < len(V1):
            res.append((float)(V1[i] + V2[i]))
            i += 1
        print(f"Add Vector is : {res}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts values of each vector by index"""
        res = []
        i = 0
        while i < len(V1):
            res.append((float)(V1[i] - V2[i]))
            i += 1
        print(f"Sous Vector is: {res}")

from numpy.random import default_rng

class Generator:
    """
    Class containing multiple ways of generating lists with some element of randomness.
    """

    # Créer une liste de nombres comprise entre lower et upper
    def createIntegerValuesListRange(self, lower : int, upper : int):
        valuesList : list = []
        for i in range(lower, upper + 1):
            valuesList.append(i)
        return valuesList

    # Créer une liste de nombres comprise entre lower et upper inversé
    def createIntegerValuesReversedListRange(self, lower : int, upper : int):
        valuesList : list = []
        for i in reversed(range(lower, upper + 1)):
            valuesList.append(i)
        return valuesList

    # Créer une liste de nombres compris entre lower et upper mélangé
    def createIntegerValuesShuffledListRange(self, lower : int, upper : int, seed : int = None) -> list :
        """
        Generates a shuffled list of integers going from one number to the other.
        The length of the list will be (upper-lower)+1.
        If no seed is specified, it defaults to None, meaning it uses a seed given by the OS.

        Args:
            lower (int): Lower bound of the interval.
            upper (int): Upper bound of the interval.
            seed (int, optional): Seed used in the PRNG. Defaults to None.

        Returns:
            list: Shuffled list of integers.
        """
        rng = default_rng(seed=seed)
        valuesList : list = []
        for i in range(lower, upper + 1):
            valuesList.append(i)
        rng.shuffle(valuesList)
        return valuesList
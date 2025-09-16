from model.observer.AbstractListenableModel import AbstractListenableModel

class IntCompare(int, AbstractListenableModel):
    """
        Class representing a integer point number with additional functionality for counting comparisons.
        Inherits from the int class and the AbstractListenableModel class.
    """
    def __new__(cls, value):
        """
            Creates a new IntCompare object with a given int value.

            param :
                value (int) : The int value to initialize.
            return :
                A new IntCompare object.
        """
        cls.__compare_count = 0
        return super().__new__(cls, value)

    def __init__(self, value):
        """
            Creates a new IntCompare object with a given int value.

            param :
                value (int) : The int value to initialize.
        """
        AbstractListenableModel.__init__(self)
        int.__init__(value)
        self.__value = value

    def __eq__(self, other):
        """
            Compares this IntCompare object to another IntCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (IntCompare) : The IntCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__eq__(other)

    def __lt__(self, other):
        """
            Compares this IntCompare object to another IntCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (IntCompare) : The IntCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__lt__(other)

    def __le__(self, other):
        """
            Compares this IntCompare object to another IntCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (IntCompare) : The IntCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__le__(other)

    def __gt__(self, other):
        """
            Compares this IntCompare object to another IntCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (IntCompare) : The IntCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__gt__(other)

    def __ge__(self, other):
        """
            Compares this IntCompare object to another IntCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (IntCompare) : The IntCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__ge__(other)

    def __ne__(self, other):
        """
            Compares this IntCompare object to another IntCompare object.
            Increments the compare counter and triggers the compare event.

            param :
                other (IntCompare) : The IntCompare object to compare.

            return: 
                True if the two objects are equal, False otherwise.
        """
        self.__compare_count += 1
        AbstractListenableModel._fireComparisons(self)
        return super().__ne__(other)
    
    def getCompareCount(self):
        """
            Returns the number of times a comparison has been made with this IntCompare object.
            return 
                (int) : The number of comparisons performed.
        """
        return self.__compare_count
    
    def resetCompareCount(self):
        """
            Resets the comparison counter for this IntCompare object.
        """
        self.__compare_count -= 1

    def getValue(self):
        """
            Returns the int value stored in this IntCompare object.

            return:
                (int) : The stored int value.
        """
        return self.__value
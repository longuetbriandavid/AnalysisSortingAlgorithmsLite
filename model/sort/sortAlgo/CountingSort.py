
import time

from model.sort.SortingStrategy import SortingStrategy

from model.observer.AbstractListenableModel import AbstractListenableModel

from view.visualization.PipeDrawing import PipeDrawing

from model.sort.IntCompare import IntCompare



class CountingSort(SortingStrategy, AbstractListenableModel):
    """
        CountingSort sorting strategy implementation.
        Inherits from SortingStrategy and AbstractListenableModel classes.
        Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (a kind of hashing). Then do some arithmetic operations to calculate the position of each object in the output sequence.
        This version does not take floatants or negative numbers into account.
    """
    def __init__(self, tab : list, waitingDelay : int = 0):
        """
            Constructor for CountingSort.

            Args:
                tab (list): The list to be sorted.
        """
        super().__init__()
        self.__name = "CountingSort"
        self.__tab = tab
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0

        self.__waitingDelay = waitingDelay
        self.__nbWaitingDelay = 0
        
    def __countingSort(self, window=None):
        """
            The main algorithm for Counting sort.

            Args:
                window (Pg): A Pygame window object to display the sorting process (optional).
        """

        start_time = time.time()

        # Useful if we want to run the sorting algorithm multiple times to avoid biased results
        self.__comparisons = 0
        self.__arrayAccesses = 0
        self.__time = 0


        max_val = max(self.__tab)

        # The max increments the counters, which aberrant for this algorithm normally does no comparison
        self.__tab.clearCompareCount()


        if window != None:
            # Instantiate the PipeDrawing class to display pipes on the screen
            pipeD = PipeDrawing(window, self, self.__tab, self.__waitingDelay)
            self.__tab.clearCounts()

            # will be incremented when a FloatCompare is modified by another IntCompare object
            startIndex = 1



        count_tab = [0] * (max_val + 1)

        n = len(self.__tab)

        for i in range(n):
            count_tab[self.__tab[i]] += 1

        index = 0

        n = len(count_tab)


        for i in range(n):
            for j in range(count_tab[i]):
                
                if window != None:
                    # be careful, do not forget to remove the old earpiece that has become useless
                    pipeD.removeListeners()

                self.__tab[index] = IntCompare(i)
                index += 1

        
                if window != None:
                    self.__nbWaitingDelay = pipeD.getNbWaitingDelay()
                    pipeD = PipeDrawing(window, self, self.__tab, self.__waitingDelay, self.__nbWaitingDelay, True)
                    self.__tab.clearArrayAccesses()
                    # we subtract from 1 the variable compareCount of each FloatCompare starting from the index startIndex -> 1, 2, ... until the size of the tab - 1
                    self.__tab.clearCompareCount(startIndex)
                    startIndex += 1

        end_time = time.time()

        self.__time = end_time - start_time

        self.__comparisons = self.__tab.getCompareCount()
        self.__arrayAccesses = self.__tab.getArrayAccesses()

        super()._fireTime()


    def sort(self):
        """
            Sort function without displaying the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__countingSort()
        return self.__tab


    def sortDrawing(self, window):
        """
            Sort function displaying the sorting process on a Pygame window.

            Args:
                window (Pg): The Pygame window object to display the sorting process.

            Returns:
                list: The sorted list.
        """
        self.__countingSort(window)
        return self.__tab


    def getTab(self) -> list:
        """
            Getter for the sorted list.

            Returns:
            list: The sorted list.
        """
        return self.__tab

    def getName(self):
        """
            Getter for the name of the sorting algorithm.

            Returns:
                str: The name of the sorting algorithm.
        """
        return self.__name

    def getComparisons(self):
        """
            Getter for the number of comparison from the sorting algorithm.

            Returns:
                int: The number of comparison from the sorting algorithm.
        """
        return self.__comparisons
        
    def getArrayAccesses(self):
        """
            Getter for the number of array accesses from the sorting algorithm.

            Returns:
                int: The number of array accesses from the sorting algorithm.
        """
        return self.__arrayAccesses

    def getTime(self):
        """
            Getter for the time it took for the sorting algorithm to complete.

            Returns:
                float: The time it took for the sorting algorithm to complete.
        """
        return self.__time
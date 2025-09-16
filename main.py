from model.importLib.importAll import *

if __name__ == '__main__':
    
    g = Generator()

    # Création de la liste de nombres 
    ########################################################################################################

    # on peut afficher 600 pipes si l'interval = 0

    # on peut afficher 299 pipes si l'interval = 1 ((largeur de l'écran / 2) -1 ( le -1 c l'espace avant le premier élément))

    # La première barre n'est plus affichée car nous avons 
    # dépassé la résolution verticale d'1 pixel, 
    # donc l'afficheur va essayer de représenter la valeur 1 mais n'arrivera pas car on ne peut pas afficher 0.5 pixel.

    
    #gList = g.createIntegerValuesListRange(1, 10)
    #gList = g.createIntegerValuesReversedListRange(1, 10)
    gList = g.createIntegerValuesShuffledListRange(1,20)
    
    for i in range(len(gList)):
        gList[i] = IntCompare(gList[i])
        
    gList = MonitoredList(gList)


    ########################################################################################################

    # délai entre chaque animations
    DELAY = 25

    # Instanciation des différents algos de tri
    ####################
    #SS = BogoSort(gList, DELAY)
    #SS = BubbleSort(gList, DELAY)
    #SS = CombSort(gList, DELAY)
    #SS = CountingSort(gList, DELAY)
    #SS = GnomeSort(gList, DELAY)
    SS = HeapSort(gList, DELAY)
    #SS = InsertionSort(gList, DELAY)
    #SS = MergeSort(gList, DELAY)
    #SS = PancakeSort(gList, DELAY)
    #SS = QuickSort(gList, DELAY)
    #SS = SelectionSort(gList, DELAY)
    #SS = ShellSort(gList, DELAY)


    # Instanciation de cette classe qui va permettre de lancer le tri
    sort = Sort(SS)


    # Visualisation de l'algo

    # configuration de la fenêtre 
    WIDTH = 600
    HEIGHT = 400
    TITLE = SS.getName()

    window = Window(WIDTH,HEIGHT, TITLE)

    print("Liste de départ : ", gList)
    print("Stratégie " + SS.getName() + " : ", sort.executeStrategyDrawing(window))
    
    window.run()

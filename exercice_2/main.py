import numpy
import random
from matplotlib import pyplot

N_STEPS = 2000

# Lance 100 pièces et retourne le nombre de côtés face observés 
def lance100Piece():
    nbCoteFace = 0
    for i in range(100):
        if random.random() > 0.5 :
            nbCoteFace = nbCoteFace + 1     

    return nbCoteFace

# Calcule la moyenne empirique de n expériences du lancer de 100 pièces
def calculerMoyenneEmpirique(n):
    resultatsExperiences = []
    # calcule des n experiences
    for i in range(n):
        resultatsExperiences.append([i, lance100Piece()])

    y_list = [y for [x, y] in resultatsExperiences]

    return resultatsExperiences, numpy.mean(y_list)

def tracerGraph(n):
    resultatsExperiences, moyenne = calculerMoyenneEmpirique(n)
    
    x_list = [x for [x, y] in resultatsExperiences]
    y_list = [y for [x, y] in resultatsExperiences]

    pyplot.axhline(y=50, color='b', linestyle='-', linewidth=2)
    pyplot.plot(x_list, y_list, '')
    pyplot.axhline(y=moyenne, color='g', linestyle='-', linewidth=2)

    pyplot.legend(("Espérance de X", "Résultats des "+str(n)+" lancés de 100 pièces", "Moyenne empirique"))
    print(resultatsExperiences)
    print(moyenne)


pyplot.figure()
tracerGraph(N_STEPS)
pyplot.show()


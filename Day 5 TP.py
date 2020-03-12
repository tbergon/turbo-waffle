from random import randint

"""Give a name and make comments"""


def initCache(nbColors=6,nbPawns=4):    #Initialisation, 6 couleurs et 4 pions

    return [randint(1,nbColors) for i in range(nbPawns)]    #Return une couleur aléatoire entre 1 et le nombre de couleurs pour chaque pions

 

"""Give a name and make comments"""

def choose(nbColors=6,nbPawns=4):   #Choix ?

    nocorrect = True    #Incorrect 

    while nocorrect:    #Tant que incorrect = True

        nocorrect = False   #Changement en False (wtf?)

        selected = input('Input your proposal: '   )    #Demande d'une proposition

        if len(selected) == nbPawns:    #Si la longueur de ? est égale au nombre de pions

            selected = [int(x) for x in list(selected)] #On change la valeur de selected en une liste comprenant la valeur int de "x" pour chaque "x" dans la liste "selected" ?

            for x in selected:  #Pour chaque "x" dans la liste "selected"

                if (x<1) or (x>nbColors):   #Si x est inférieur à 1 ou si x est supérieur au nombre de couleurs...

                    nocorrect = True    #... ??? Probablement False au lieu de True

        else:

            nocorrect = True    #Pas correct

    return selected     #return ce qu'on avait entré (l18)

 

"""Give a name and make comments"""

def evaluation(selected,cache):     #

    WellPut = 0     #Bien placé : aucun

    Misplaced = 0   #Mal placé : aucun

    copySelected,copyCache = list(selected),list(cache)     #????

    for i in range(len(cache)):     #pour chaque ? dans "cache"

        if copySelected[i] == copyCache[i]:     #Si les deux valeurs sont égales

            WellPut += 1    #C'est bien placé

            copySelected[i],copyCache[i] = -1,-1    #Changement de valeur 

    for i in range(len(cache)):     #Pour chaque ? dans "cache"

        for j in range(len(cache)):     #Pour chaque ? dans "cache"

            if (copySelected[i] == copyCache[j]) and (copySelected[i] != -1):   #Si les deux valeurs sont égales ET la valeur d'index i est différente de -1 (changé plus haut ?)

                Misplaced += 1      #c'est mal placé

                copySelected[i],copyCache[j] = -1,-1    #Changement des valeurs d'index i et j dans copySel et copyCac

    return WellPut,Misplaced    #Return combien son bien et mal placés ?

 

"""Give a name and make comments"""

def display(well,bad):  #Fonction pour afficher ce qui est bien placé avec en arguments les nombres

    print(well,"well spot and",bad,"bad ",'\n')     #Affichage :: "nombre" bien placés et "nombre" mal placés

 

"""Give a name and make comments"""

def displayCache(cache):    # ??????

    for x in cache:     #Pour tout dans "cache"

        print(x,end='')     #Affichage espacé de chaque "x"

 

"""Give a name and make comments"""

def gameParameters():   #Définition des règles

    nbC = int(input('Input the number of colors: '))    #Nombre de couleurs

    nbP = int(input(' Enter the length of the sequence to guess: '))    #Nombre de pions ?"

    nbTry = int(input(' Enter the number of trials: '))     #Nombre d'essais autorisés

    return nbC,nbP,nbTry    #Return des trois valeurs

 

"""Give a name and make comments"""

def master():   #Fonction principale du jeu ??

    nbC,nbP,nbTry = gameParameters()    #Les règles

    cache = initCache(nbC,nbP)  #wth ?

    notFound = True #Variable notée vraie

    tries = 1   #Nombre d'essais au début (donc 1)

    print()     #???

    while notFound and (tries<=nbTry):      #Tant que le "nombre ?" n'a pas été trouvé et que le nombre d'essais autorisé n'est pas dépassé

        print('try',tries)      #On affiche le nombre d'essais en cours

        well,bad = evaluation(choose(nbC,nbP),cache)    #????

        display(well,bad)   #On affiche ce qui a été trouvé et ce qui ne l'a pas été

        if well == nbP:     #Si le nombre de pions trouvés correspond au nombre de pions total...

            notFound = False    #...notFound changé en False car on a tout trouvé

        else:   #Sinon...

            tries += 1      #...on rajoute u essai au compteur

    if tries==(nbTry+1):    #Si le nombre d'essais est égal au nombre total autorisé + 1 (donc on a dépassé)...

        print("lost, we had to find:",end=' ')      #...on a perdu

        displayCache(cache)     #wtf is "cache"

    else:   #Sinon ...

        print("Congratulations, you have found well:", end=' ')     #"Bravo vous avez trouvé wow"

        displayCache(cache)     # (ง ͠° ͟ل͜ ͡°)ง

 

"""Give a name and make comments"""

def chooseGame(S,possibles,results,tries):      #Choix du jeu ?

    if tries==1:    #SI le nombre d'essais est égal à 1...

        return [1,1,2,2]    #...on renvoie les valeur par défault de la liste : 1,1,2,2

    elif len(S)==1:     #Sinon si la longueur de "S ?" est égale à 1...

        return S.pop()      #On enlève S de la liste en l'affichant ?

    else:   #Sinon...

        return max(possibles, key=lambda x: min(sum(1 for p in S if evaluation(p,x) != res) for res in results))    #... return plein de trucs

 

"""Give a name and make comments"""

def chooseGameBis(S,possibles,results,tries):   #Again ?

    if tries == 1:      #Same

        return [1,1,2,2]    #Same

    elif len(S)==1:     #Same

        return S.pop()  #Same

    else:   #Same

        Max = 0     #Le max est définit à 0

        for x in possibles:     #Pour chaque "possible"...

            Min = 1297      #...le min est définit à 1297

            for res in results:     #Pour chaque "résultat ?"

                nb = 0  #? Compteur maybe ?

                for p in S:     #pour "p" dans "S"   *_*

                    if evaluation(p,x)!=res:    #Si "appel de la fonction évaluation où p=selected et x=cache" est différent du "résultat ?""

                        nb+=1   #? Compteur maybe ?

                if nb<Min:      #Si "le compteur ?" est inférieur au minimum...

                    Min=nb  #...le minimum prend le nombre au "compteur ?"

            if Max<Min:     #Si le max est inférieur au min ...

                Max = Min   #...Le max prend la valeur du min

                xx = x  #Et "xx" prend la valeur de "x"

        return xx   #??

                

"""Give a name and make comments"""

def game():     #Fonction représentant le jeu ?

    nbC,nbP = 6,4   #Nombre de couleurs et de pions assignés à 6 et 4 (valeurs par défault)

    cache = initCache(nbC,nbP)  #  *_*

    notFound = True     #Pas trouvé est vrai

    tries = 1   #Le nombre d'essai est set à 1

    S = set((x,y,z,t) for x in range(1,7) for y in range(1,7) for z in range (1,7) for t in range(1,7))     #???

    possible = frozenset(S)     #??

    results = frozenset((well,bad) for well in range(5) for bad in range(5-well) if not (well==3 and bad==1))   #Résultats ?

    while notFound and (tries<=10):     #Tant qu'on a pas trouvé et que le nombre d'essais est inférieur ou égal à 10

        print('try',tries)      #Affichage du nombre d'essais

        selected = chooseGameBis(S,possible, results, tries)    #kys

        print('computer proposal: ',end='')     #Affichage de "computer proposal:" 

        displayCache(selected)      #Affichage d'un truc ?

        print()     #Affichage de rien

        well,bad = evaluation(selected,cache)   #??

        display(well,bad)   #Affichage du bien et mal placés

        if well == nbP:     #Si bien placé correspond au nombre de pions...

            notFound = False    #...on a trouvé

        else:   #Sinon...

            tries +=1   #...on rajoute un essai
            S.difference_update(set(coup for coup in S if (well,bad) != evaluation(coup,selected)))     #Cmon man

    if tries == 11:     #Si le nombre d'essais est 11...

        print("lost, we had to find:",end=' ')  #...on a perdu et on nous le dit

        displayCache(cache)     #affichage d'un truc

    else:   #Sinon...

        print("He is strong, he found", end=' ')    #weird flex, but ok

        displayCache(cache)     #Affichage d'un truc

               

"""Give a name and make comments"""

game()      #lol
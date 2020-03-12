def main():
    word = "eclaire"
    adWord = "*******"
    inp = ""
    lost = 11
    while not checkWords(adWord,word):
        print(adWord)
        print(lost," tries left before being hanged")
        inp = input("choose a letter : ")
        if findLetter(inp,word):
            index = findIndexs(inp,word)
            s = list(adWord)
            for i in index:
                s[i] = inp
            adWord = "".join(s)
        else:
            lost -= 1
        if lost <= 0:
            print("HANGED")
            break
    print("the world was: ", word)

def findLetter(letter,word):
    for l in word:
        if l == letter:
            return True
    return False

def findIndexs(letter,word):
    tab = [] #Initialisation du tableau 'tab' contenant le/les indexs de la lettre 'letter' dans le mot word
    i = 0 #Initialisation du compteur
    for l in word: #Pour chaque lettre 'l' dans mon mot 'word'
        if l == letter: #Si la lettre 'l' est égale à la lettre 'letter'
            tab.append(i)#Ajouter la valeur du compteur 'i' au tableau d'index
        i += 1#Incrementation du compteur 'i'
    return tab #Retourner tableau 'tab contenant les indexs

def checkWords(wordA,wordB):
    return wordA == wordB


main()
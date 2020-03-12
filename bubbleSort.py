tab=[]
def parcours(tab):
    i=0
    for element in tab:
        if i==len(tab)-1:
            return True
        if element>tab[i+1]:
            return False
        i+=1

def bubbleSort(tab):
    print(tab)
    while not parcours(tab):
        j=0
        for element in tab:
            if j==len(tab)-1:
                break
            if element>tab[j+1]:
                tmp=tab[j]
                tab[j]=tab[j+1]
                tab[j+1]=tmp
            j+=1
    print(tab)


bubbleSort(tab)
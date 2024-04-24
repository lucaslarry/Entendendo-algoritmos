import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        indice_pivo = random.randint(0, len(array) - 1)
        pivo = array[indice_pivo]
        menores = [i for i in array if i < pivo] 
        maiores = [i for i in array if i > pivo]
        iguais = [i for i in array if i == pivo] 
        return quicksort(menores) + iguais + quicksort(maiores)

array = [3, 2, 75, 12, 22, 35, 1, 57, 1,75,100]
print(quicksort(array))
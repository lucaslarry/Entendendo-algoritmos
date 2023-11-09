def buscaMenor(arr):
    menor = arr[0] 
    menor_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(arr): 
    novo_arr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) 
        novo_arr.append(arr.pop(menor))
    return novo_arr

print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
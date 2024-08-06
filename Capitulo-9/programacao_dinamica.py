def mochila(capacidade, pesos, valores, n):
    tabela = [[0 for x in range(capacidade + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                tabela[i][w] = 0
            elif pesos[i-1] <= w:
                tabela[i][w] = max(valores[i-1] + tabela[i-1][w-pesos[i-1]], tabela[i-1][w])
            else:
                tabela[i][w] = tabela[i-1][w]

    return tabela[n][capacidade]

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidade = 50
n = len(valores)
valor_maximo = mochila(capacidade, pesos, valores, n)
print("Valor máximo que pode ser obtido:", valor_maximo)
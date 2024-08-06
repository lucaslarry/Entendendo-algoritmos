estacoes_universo = set(['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'])
estacoes = {
    'kone': set(['um', 'cinco', 'seis']),
    'ktwo': set(['dois', 'tres', 'quatro']),
    'kthree': set(['cinco', 'sete', 'oito']),
    'kfour': set(['quatro', 'cinco', 'seis', 'sete']),
    'kfive': set(['sete', 'oito', 'nove', 'dez'])
}

def cobertura_gulosa(estacoes_universo, estacoes):
    cobertura_final = set()
    while estacoes_universo:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados in estacoes.items():
            cobertos = estacoes_universo & estados
            if len(cobertos) > len(estados_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos
        estacoes_universo -= estados_cobertos
        cobertura_final.add(melhor_estacao)
    return cobertura_final

cobertura = cobertura_gulosa(estacoes_universo, estacoes)
print("Cobertura de conjunto:", cobertura)
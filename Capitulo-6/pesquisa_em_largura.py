from collections import deque

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa_em_largura(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    print("Não tem ninguém que venda manga!")
    return False

    
    
grafo = {}
grafo["Voce"] = ["Alice", "Bob", "Claire"]
grafo["Bob"] = ["Anuj", "Peggy"]
grafo["Alice"] = ["Peggy"]
grafo["Claire"] = ["Thom", "Jonny"] 
grafo["Anuj"] = []
grafo["Peggy"] = []
grafo["Thom"] = []
grafo["Jonny"] = []
  
pesquisa_em_largura("Voce")





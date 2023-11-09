def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome) #Pilha de chamada
    print("preparando para dizer tchau...")
    tchau() # pilha de chamada

def sauda2(nome):
    print("Como vai " + nome + "?")
def tchau():
    print("ok, tchau!")


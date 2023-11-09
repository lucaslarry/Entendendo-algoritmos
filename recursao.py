def regressiva(i):
    print(i)
    if i <= 1: 
        return #Caso Base
    else: 
        regressiva(i-1) #Caso Recursivo

regressiva(10)

def fat(x):
    if x == 1:
        return 1 #Caso Base
    else:
        return x * fat(x-1) #Caso Recursivo
print(fat(4))

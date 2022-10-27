#Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], 
# regla de Sarrus de forma recursiva y de forma iterativa

matriz=[]

def matri(n):
    for i in range(n):
        matriz.append([])
        for j in range (n):
            matriz[i].append(0)
    return matriz       
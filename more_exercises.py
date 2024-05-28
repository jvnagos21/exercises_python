import numpy as np
def data_input():
    coeficient = quantity = eval(input('exercicio 01: digite o valor do coeficiente: '))
    return coeficient

def calc_delta(a, b, c):
    delta = b*b-4*a*c
    return delta

def calculate_raizes(a, b, c, delta):
    if(delta< 0):
        resolution = 'exercicio 01: a equação não possui raízes nos numeros reais'
    elif(delta == 0):
        x = -b/(2*a)
        resolution = f'exercicio 01: a equação possui apenas a raiz: {x}'
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resolution = f'exercicio 01: a equação possui as raizes:{x1}, {x2}'
    return resolution


a = data_input()
b = data_input()
c = data_input()

delta=calc_delta(a,b,c)

resolution=calculate_raizes(a,b,c, delta)

print(resolution)



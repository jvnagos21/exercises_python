# exercicio 1
try:
    x = int(input("exercicio 1: digite seu numero: "))
except ValueError:
    print('exercicio 1: entre com um numero valido')

#exercicio 2

while True:
    try:
        x = int(input("exercicio 2: digite seu numero: "))
        break
    except ValueError:
        print('exercicio: entre com um numero valido')

#exercicio 3

x = int(input('exercicio 3: digite seu numero: '))
y = int(input('exercicio 3: digite seu numero: '))

def division(x, y):
    try:
        result = x / y
        print("exercicio 3: A resposta é: ", result)
    except ZeroDivisionError:
        print("exercicio 3: erro: divisão por zero")


division(x, y)
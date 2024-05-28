#exercise 00

def find_minimum(list):
    minimum = list[0]
    for elem in list:
        if (elem < minimum):  #verifico se o valor minimum é menor que elem senão for retorno o menor valor
            minimum = elem
        return minimum

test_list = [5, 10, 3, 40]
minus = find_minimum(test_list)
print("exercicio teste: o menor numero dessa lista é: [{}]".format(minus))

#exercise 01

def is_pair(num):
    resolution = (num%2 == 0)
    return resolution

def sum_pair(list):
    sum = 0
    for num in list:
        if (is_pair(num)):
            sum = sum+num
    return sum

list = [21, 322, 34, 55, 9,46]

sum = sum_pair(list)

print(f'exercicio 01: o somatório dos elementos pares da lista é: {sum}')

#exercise 03

#solution 01

def fatorial_interactive(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    return factorial

num = eval(input('exercicio 03: digite o numero que você quer fatorar: '))

print(f'exercicio 03 solução 01: o fatorial de {num} é : {fatorial_interactive(num)}')

#solution 02

def fatorial_recursive(num):
    if((num == 0) or (num == 1)):
        return 1
    return num * fatorial_recursive(num - 1)

print(f'exercicio 03 solução 02: o fatorial de {num} é : {fatorial_interactive(num)}')

#exercicio 04

def is_prime(num):
    if(num < 2):
        return False
    i = num // 2
    while (i > 1):
        if (num % i == 0):
            return False
        i = i - 1
    return True


def print_result(num, result):
    message=f'exercicio 04: o número {num} NÃO é primo'
    if(result):
        message=f'exercicio 04: o número {num} é primo'

    return message

num = eval(input('exercicio 04: digite o numero pra verificar se é primo: '))
result = is_prime(num)
message = print_result(num, result)
print(message)


#example 01

a = 7
b = 8

#solution 01
if (a > b):
    maior = a
else:
    maior = b

print(f'solução 01: O maior número é: {maior}')

#solution 02
maior = a

if (b > maior):
    maior = b

print(f'solução 02: O maior número é: {maior}')

#exercise 01

if(a%2==0):
    situacao='exercicio 1: o numero é par'
else:
    situacao='exercicio 1: o numero é impar'
print(situacao)

# exercise 02

nota_do_estudante= eval(input('exercicio 02: digite sua nota: '))

if(nota_do_estudante > 7):
    resultado='exercicio 2: aluno foi aprovado!!'
elif(nota_do_estudante >= 5.0):
    resultado='exercicio 2: o aluno está em recuperação :>'
else:
    resultado='exercicio 2: o aluno foi reprovado :('
print(resultado)

#exercise 03

unitary_price = 10
discount_10 = 0.1
discount_20 = 0.2

quantity = eval(input('exercicio 03: digite a quantidade que você quer comprar: '))
if (quantity <= 10 ):
    final_value = unitary_price*quantity
elif (quantity <=20):
    final_value = unitary_price*quantity*(1-discount_10)
else:
    final_value = unitary_price*quantity*(1-discount_20)

print(f'exercicio 03: o valor final da compra é: {final_value}')

#exercise 04

value_List = [30, 7, 13, 16, 29, 44, 21]
sum = 0

# solution 01
n = len(value_List)

for i in range(n):
    if(value_List[i]%2 == 0):
        sum=sum+value_List[i]

print(f'o somatório dos elementos pares da lista é igual a: {sum}')

# solution 02
sum = 0
for num in value_List:
    if (num%2 == 0):
        sum = sum + num

print(f'o somatório dos elementos pares da lista é igual a: {sum}')
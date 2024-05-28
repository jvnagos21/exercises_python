# value change
idol_a = 'IU'
idol_b = 'Suzy'

print('values not changed')
print(f'{idol_a} is very famous')
print(f'{idol_b} also is famous')

# first change

temp = idol_a

idol_a = idol_b
idol_b = temp
print('first value change')
print(f'{idol_a} is very famous')
print(f'{idol_b} also is famous')

# second value change

idol_a, idol_b = idol_b, idol_a
print('second value change')
print(f'{idol_a} is very famous')
print(f'{idol_b} also is famous')


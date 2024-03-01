'''Peça ao usuário que digite um número. Se o número for maior que 10,
imprima "O número é maior que 10". Caso contrário, imprima "O numero 
é menor ou igual a 10".
'''

numero = int(input('Digite um número: '))

if numero > 10:
    print('O número é maior que 10')
else: 
    print('O numero é menor ou igual a 10')
'''
Crie uma função lambda que aceite um número e retorne "Par" se o for par 
e "ímpar" se o número for ímpar.
'''

poui = lambda num: 'Par' if num % 2 == 0 else 'Impar'

numero = int(input('Digite um número: '))
print (f'O número {numero} é {poui(numero)}')
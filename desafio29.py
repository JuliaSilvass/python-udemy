'''
Crie uma função lambda que aceite um número e retorne o cubo desse número.
'''

cubo = lambda num: num ** 3

numero = int(input('Digite um núemro: '))
print (f'O cubo de {numero} é {cubo(numero)}')
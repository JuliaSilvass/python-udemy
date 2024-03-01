'''Crie uma função que aceita um número como entrada e retorna 
o quadrado desse número
'''
def quadrado (num): 
    return num ** 2

numero = int(input('Digite um número: '))
print(f'O quadrado de {numero} é igual a {quadrado(numero)}')
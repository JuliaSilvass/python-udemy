'''
Crie uma função que aceite dois números com entrada e retorne a soma desses 
números.
'''
def somar(num1, num2):
    soma = num1 + num2
    return soma

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print (f'A soma de {numero1} e {numero2} é {somar(numero1, numero2)}')
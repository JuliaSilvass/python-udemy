'''
Crie uma função lambda que aceite dois números e retorn a multiplicação desse números
'''

multi = lambda num1, num2: num1 * num2

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

print(f'A multiplicação de {numero_1} e {numero_2} é {multi(numero_1, numero_2)}')
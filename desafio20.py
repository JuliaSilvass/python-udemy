'''
Crie uma lista de números de 1 a 10. Use um 'for loop' para iterar 
sobre a lista. Se o número atual da interação for par, imprima "O número
[número] é par". Se o número for ímpar, imprima "O número [número] é ímpar".
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 == 0:
        print('O número ' + str(numero) + ' é par')
    else:
        print('O número ' + str(numero) + ' é ímpar')
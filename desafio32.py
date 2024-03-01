'''
Crie uma função lambda que eleve o número ao quadrado. Em seguida, use essa 
função par calcular o quadrado de todos os números em uma lista usando um 
loop for. 
'''
quadrado = lambda num : num ** 2

numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = []

for numero in numeros:
    resultado.append(quadrado(numero))

print(resultado)

'''
Crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim
que chegar a 5 usando os comandos "break". Em seguida, crie um segundo loop
que imprima os números de 1 a 10, mas pule a impressão do número 5 usando 
o comando "continue".
'''

for num in range (1,11):   
    if num > 5:
        break
    print(num)

print(' ')


for num in range (1,11):
    if num == 5:
        continue
    print(num)
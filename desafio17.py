'''
 Peça ao usuário para digitar a sua idade. Se a idade for menor que 13, 
 imprima "Você é uma criança". Se a idade estiver entre 13 e 19, imprima 
 "Você é um adolescente". Se a idade for 20 ou mais, imprima "Você é um adulto".
'''

idade = int(input('Qual a sua idade? '))

if idade < 13: 
    print('Você é uma criança')
elif idade in range (13, 20):
    print('Você é um adolescente')
else:
    print('Você é um adulto')
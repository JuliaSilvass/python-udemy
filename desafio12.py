'''Crie uma lista de frutas e outras de vegetais. Use um "for lopp"
aninhado (Nested for loop) para imprimir todas as combinações possíveis
de frutas e vegetais, com a fruta primeiro e o vegeral em segundo.
'''

frutas = ['abacaxi', 'maça', 'pera', 'goiaba']
vegetais = ['batata', 'cenoura', 'abobora', 'abobrinha']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)
    print (' ')
'''
Crie uma lista com 5 nomes de países e as capitais desses países. Peça ao 
usuário para digitar o nome de um país. Se o país estiver na lista, imprima
"A capital de [país] é [capital]". Se o país não estiver na lista, imprima
"Desculpe, não temos informações sobre a capital desse pais".
'''

paises ={
    'Brasil': 'Brasília',
    'Bolivia': 'La paz e Sucre',
    'Argentina': 'Buenos Aires',
    'México':'Cidade do méxico',
    'Alemanha':'Berlim'
}

pais = input('Digite o nome do país: ')

if pais in paises:
    print(f'a capital de {pais} é {paises[pais]}')
else: 
    print('Desculpe, não temos informações sobre a capital desse pais')
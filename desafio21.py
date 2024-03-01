'''
Crie uma lista com os nomes de três cidades. Peça ao usuário para digitar
o nome de uma cidade. Se a cidade estiver na lista, imprima "A cidade está
na lista de cidades". Se a cidade não estiver na tupla, imprima "A cidade 
não esta na lista de cidades".

Obs.: não pode usar list[]
'''

cidade_tuple = ('São Paulo', 'Porto Alegre', 'Crato')
cidade = input('Digite o nume de uma cidade: ')

if cidade in cidade_tuple:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não esta na lista de cidades')
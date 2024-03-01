'''
Imagine que você tem uma loja de carros. Crie uma lista com os carros 
que você tem em estoque: BMW X6, BMW i5, BMW i8. Peça ao usuário para que
ele insira o nome do carro que deseja comprar. Se o carro não estiver em 
estoque, imprima "Desculpa, este carro não esta disponível".
'''

carros = ['BMW X6', 'BMW i5', 'BMW i8']

estoque = input('Digite o carro que deseja: ')

# for carro in carros: 
#     if estoque == carro:
#         print('Este carro está disponível')
#         break
#     else:
#         print('Desculpa, este carro não está disponível') 
# nesse aqui o else exibe três vezes

if estoque in carros:
    print('Este carro está disponível')
else:
    print('Desculpa, este carro não está disponível')
        
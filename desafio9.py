'''
Comece com uma lista 'fruta' do desafio anterior, remova a "manga" da lista usando o método remove().
Depois remova o último item da lista usando o comando del. Por fim imprima a lista modificada na tela.
'''

fruta = ['maça', 'morango', 'manga', 'uva', 'abacaxi']

fruta.remove('manga')
del fruta[-1]

print(fruta)
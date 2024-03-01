'''
Comece com uma lista 'frutas', e altere o segundo elemento da lista de "banana" para "morango".
Depois adicione a fruta "abacaxi" ao final da lista. Por fim imprima a lista modificada na tela.
'''

fruta = ['maça', 'banana', 'manga', 'uva']

fruta[1] = 'morango'    #ou fruta.insert(1, 'morango')
fruta.append('abacaxi')

print(fruta)
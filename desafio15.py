'''Crie uma lista de frutas que inclui "maça" três vezes e outras frutas
de sua escolha. Use um loop for para contar quantas vezes "maça" aparece
na lista e imprima o restultado.'''

frutas = ['maça', 'banana', 'goiaba', 'pera', 'maça', 'melão', 'maça']

contador = 0
for fruta in frutas:
    if fruta == 'maça':
        contador += 1

print(contador)
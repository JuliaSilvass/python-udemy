'''
Crie dois conjuntos, cada um contendo 5 nomes de seus amigos. Alguns nomes 
devem estar presentes em ambos os conjuntos. Use um método para encontrar
quais nome aparecem em ambos os conjuntos e imprima o resultado.
'''

amigosSP = {'leonardo', 'breno', 'alexandre', 'gustavo', 'flavia'}
amigosRS = {'flavia', 'alexandre', 'gabriel', 'bruno', 'heitor'}

ambos = amigosRS.intersection(amigosSP)

print(ambos)
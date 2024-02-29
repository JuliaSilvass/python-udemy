# Desafio com If, Elif, Else

'''
Criar um programa que depende da temperatura (em celsius) do steak ele retorna o ponto de cozimento em português.
O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada) 
'''

temp = int(input('Qual a temperatura da carne? '))

if temp < 48: 
    print("Cozinhe mais!")
elif temp in range(48, 54):                                #Uma forma de fazer sem usar o < e >. 
    print("A carne esta selada!")
elif temp in range(54, 60):                                #O último valor do range não é contabilizado
    print("A carne esta ao ponto para mal passada!")
elif temp in range(60, 65):
    print("A carne esta ao ponto!")
elif temp in range(65, 71):
    print("A carne esta ao ponto para bem passada!")
else:
    print("A carne esta bem passada!")
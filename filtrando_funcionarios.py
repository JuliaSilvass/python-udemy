#Desafio com 'sets'

'''
Criar um programa que gere 3 listas de acordo com a necessidade logo abaixo: 

Lista 1: Funcionários que tem carro e trabalha a noite
Lista 2: Funcionários que tem carro e trabalha durante o dia
Lista 3: Funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
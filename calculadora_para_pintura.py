# Desafio com Funções

'''
Criar um programa que calcula a quatidade de tinta necessária para pintar uma parede. 
O usuário deverá fornecer as seguintes informações: Rendimento(m²), altura(m) e largura(m).
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tintas'
'''
import math

redimento = int(input('Qual o redimento em m²? '))
altura = int(input('Qual altura em m?'))
largura = int(input('Qual largura em m?'))

metroscb = altura*largura
x = math.ceil(metroscb/redimento)
sobras = (x - metroscb/redimento)*100

print(f'Você terá que comprar {x} latas de tintas, com chance de sobrar {sobras:.2f}% de uma lata')
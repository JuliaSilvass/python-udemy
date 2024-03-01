'''
Crie duas funções, a primeira deve aceitar um número e retonar o dobro 
desse número. A segunda função deve aceitar um número e retornar o quadrado
desse número. Em seguida, chame a primeira função dentro da segunda para
retornar o quadrado dobro de um número.
'''

def dobro (num):
    return num *2

def quadrado (num):
    return num ** 2           # ou poderia: dobro(num) ** 2

numero = int(input('Digite um número: '))

print(f'O quadrado do dobro do número {numero} é {quadrado(dobro(numero))}')
                                                # quadrado(numero)
'''
Crie uma função que calcule a potência de um número. A função deve aceitar 
dois argumentos: a base e o expoente. No entanto, se o expoente não for 
fornecido ao chamar a função, ele deve assumir o valor padrão de 2.
'''

def potencia (base, expoente):
    return base**expoente

base = int(input('Digite a base: '))
expoente = input('Digite o expoente: ')

if (expoente):
    print(f'A potência da base {base} no expoente {expoente} é: {potencia(base,int(expoente))}')
else:
    print(f'A potência da base {base} no expoente 2 é: {potencia(base,2)}')
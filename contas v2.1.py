import math
def head():
    print('\nPrograminha para resolver contas\n1 - Baskara   2 - Biquadrada\n3 - Pitágoras 4 - Sair')
    opcao = input("->")
    if opcao.isnumeric():
        return float(opcao)

def equacao_segundo_grau():
    result = []
    a = float(input('\nDefina o valor de (a): '))
    b = float(input('Defina o valor de (b): '))
    c = float(input('Defina o valor de (c): '))
    try:
        delta = b**2-4*b*c
        x1 = (-b + delta**0.5)/2*b
        x2 = (-b - delta**0.5)/2*b
        print('\nx = [-b ± √(b)² - 4 *a *c] / 2*a', f'\nx = [-(b)) ± √(b)² - 4 *b *c] / 2*b')
        print('x = [-({1}) ± √{2}] / {0}'.format(b*2,b,delta), f'\nx1 = {x1:.2f}\nx2 = {x2:.2f}')
        return [x1,x2]
    except:
        return []

def biquadrada():
    raizes = equacao_segundo_grau()
    print('\ny1 = ±{0:.2f}\ny2 = ±{1:.2f}'.format(math.sqrt(raizes[0]),math.sqrt(raizes[1])))

def pitagoras():
    opcao1 = input('\nDefina onde está o (x)\nCatetos(0) Hipotenusa(1) -> ')
    try:
        opcao1 = int(opcao1)
        if opcao1 == 0:
            a = float(input('Defina o valor de a -> '))
            b = float(input('Defina o valor de b -> '))
            c = math.sqrt(a**2 - b**2)
            print(f'\n(A)² = (B)² + (C)²\n({a})² = ({b})² + ({c})²')
            print(f'C = {c}')
        elif opcao1 == 1:
            b = float(input('Defina o valor de b -> '))
            c = float(input('Defina o valor de c -> '))
            a = math.sqrt(b**2 + c**2)
            print(f'\n(A)² = (B)² + (C)²\n({a})² = ({b})² + ({c})²')
            print(f'A = {a}')
    except ValueError:
        pass

def iniciar():
    opção = 0
    while True:
        opção = head() #Inicia a Esolha e retorna a opção esolhida
        if opção == 1:
            equacao_segundo_grau()
        elif opção == 2:
            biquadrada()
        elif opção == 3:
            pitagoras()
        elif opção == 4:
            break

iniciar()
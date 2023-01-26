menu = 0
void = 1
def head():
    print("Programinha para resolver contas")
    print("1 - Baskara   2 - Biquadrada\n3 - Pitágoras 4 - Sair")
    opcao = input("Escolha uma opção: ")

def headb():
    print('\n###############################\nContinuar(1)          Voltar(2)')

def erro():
    print('Porfavor utilize apenas numeros válidos\n')

def baskarap(a,b,c,delta):
        print('\nx = [-b ± √(b)² - 4 *a *c] / 2*a') 
        print('x = [-({1}) ± √({1})² - 4 *{0} *{2}] / 2*{0}'.format(a,b,c)) 
        print('x = [-({1}) ± √{2}] / {0}'.format(a*2,b,delta))
        print('x = [-({1}) ± {2}] / {0}'.format(a*2,b,delta**0.5))
        print('x1 = {0}'.format((-b + delta**0.5)/2*a)) 
        print('x2 = {0}'.format((-b - delta**0.5)/2*a))
def baskara():
    
    a = (input('\nDefina o valor de (a): ')) 
    if '-' in a or a.isalpha() or a.isnumeric():
        b = (input('Defina o valor de (b): '))
        if '-' in b and not b.isalpha or b.isnumeric():
            c = (input('Defina o valor de (c): '))
            if '-' in c and not c.isalpha or c.isnumeric():
                a = complex(a)
                b = complex(b)
                c = complex(c)
                delta = b**2-4*a*c
                baskarap(a,b,c,delta)
            else:
                erro()
        else:
            erro()
    else:
        erro()

def Biquadrada():
    a = (input('\nDefina o valor de (a): ')) 
    if '-' in a or a.isalpha or a.isnumeric():
        b = (input('Defina o valor de (b): '))
        if '-' in b and not b.isalpha or b.isnumeric():
            c = (input('Defina o valor de (c): '))
            if '-' in c and not c.isalpha or c.isnumeric():
                a = complex(a) 
                b = complex(b)
                c = complex(c)
                delta = b**2-4*a*c
                baskarap(a,b,c,delta)
                print('voltando...')
                print('y² = x1 ou y² = x2')
                print('y² = {0} ou y² = {1}'.format((-b + delta**0.5)/2*a,(-b - delta**0.5)/2*a))
                print('y = ±{0} ou y = ±{1}'.format(((-b + delta**0.5)/2*a)**0.5,((-b - delta**0.5)/2*a)**0.5))
            else:
                erro()
        else:
            erro()
    else:
        erro()

def pitagoras():
    print('\nDefina onde  está o  (x)')
    print('catetos(0) hipotenusa(1)')
    escolhax = (input('-> '))
    if escolhax.isnumeric() == True:
        if 0 == int(escolhax):
            a = (input('\nDefina o valor de (a): '))
            if '-' in a or a.isnumeric():
                b = (input('Defina o valor de (b): '))
                if '-' in b or b.isnumeric():
                    a = complex(a)
                    b = complex(b)
                    print('\n(A)² = (B)² + (C)²')
                    print('({0})² = ({1})² + (C)²'.format(a,b))
                    print('{0} = {1} + (C)²'.format(a**2,b**2))
                    print('(C)² = {0}'.format(a**2-b**2))
                    print('C = {0:.6}'.format((a**2-b**2)**0.5))
                else:
                    erro()
            else:
                erro()
        elif 1 == int(escolhax):
            b = (input('\nDefina o valor de (b): '))
            if '-' in b or b.isnumeric():
                c = (input('Defina o valor de (c): '))
                if '-' in c or c.isnumeric():
                    b = complex(b)
                    c = complex(c)
                    print('\n(A)² = (B)² + (C)²')
                    print('(A)² = ({0})² + ({1})²'.format(b,c))
                    print('(A)² = {0} + {1}'.format(b**2,c**2))
                    print('(A)² = {0}'.format(b**2+c**2))
                    print('A = {0}'.format((b**2+c**2)**0.5))
                else:
                    erro()
            else:
                erro()
        else:
            erro()
    else:
        erro()
    
while void == 1:
    head()
    menu = (input('-> '))
    if menu.isnumeric() == True:
        menu = int(menu)
        if menu >=1 and menu <=4:
            while menu == 1:
                baskara()
                headb()
                continuar = input('-> ')
                if '1' in continuar:
                    pass
                else:
                    break
            while menu == 2:
                Biquadrada()
                headb()
                continuar = input('-> ')
                if '1' in continuar:
                    pass
                else:
                    break
            while menu == 3:
                pitagoras()
                headb()
                continuar = input('-> ')
                if '1' in continuar:
                    pass
                else:
                    break
            if menu == 4:
                void = 0
        else:
            pass
    else:
        erro()
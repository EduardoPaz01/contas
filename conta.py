print('programinha pra resolver contas') #responsável por iniciar o programa
print('###############################')
print('  BASKARA (1)      Pitágoras (3)')
print('Biquadrada(2)   Trigonometria(4)')

menu = (0)
menu = input('-> ')
print('')

while 1 == int(menu):
	a = float(input('Defina o valor de (a): '))
	b = float(input('Defina o valor de (b): '))
	c = float(input('Defina o valor de (c): '))
	print('')

	print('Fx(Delta= -4 *a *c)')
	print('Delta= ('+str(b)+')˄2'+' -4 '+'*'+str(a)+' *'+str(c))
	Dlt = b**2 - 4*a*c
	print('Delta= '+str(Dlt))
	print('')

	print('x= -b ± √Delta /a *2')
	print('x= -('+str(b)+') ± √'+str(Dlt)+'  /2 *'+str(a))
	Dl = Dlt**0.5
	x1p1 = -b + Dl
	x2p1 = -b - Dl
	xp1 = 2*a
	x1 = x1p1/xp1
	x2 = x2p1/xp1
	print('')

	print('x1= '+str(x1))
	print('x2= '+str(x2))
	pause = input('pause')
	print('')
	print('')
	print('programinha pra resolver contas')
	print('###############################')
	print('  BASKARA (1)      Pitágoras (3)')
	print('Biquadrada(2)   Trigonometria(4)')

	menu = (0)
	menu = input('-> ')
	print('')

while 2 == int(menu):
	a = float(input('Defina o valor de (a): '))
	b = float(input('Defina o valor de (b): '))
	c = float(input('Defina o valor de (c): '))
	print('')

	print('Fx(Delta= -4 *a *c)')
	print('Delta= ('+str(b)+')˄2'+' -4 '+'*'+str(a)+' *'+str(c))
	Dlt = b**2 - 4*a*c
	print('Delta= '+str(Dlt))
	print('')

	print('x= -b ± √Delta /a *2')
	Dl = Dlt**0.5
	print('x= -('+str(b)+') ± √'+str(Dl)+'  /2 *'+str(a))
	x1p1 = -b + Dl
	x2p1 = -b - Dl
	xp1 = 2*a
	x1 = x1p1/xp1
	x2 = x2p1/xp1
	print('')
	print('x1= '+str(x1))
	print('x2= '+str(x2))
	
	print('')
	print('Voltando...')
	print('x1= y')
	print(str(x1)+'= y˄2')
	print('√'+str(x1)+'= y')
	yx1 = x1**0.5
	print('±'+str(yx1)+'= y')
	print('')
	print('x2= y')
	print(str(x2)+'= y˄2')
	print('√'+str(x2)+'= y')
	yx2 = x2**0.5
	print('±'+str(yx2)+'= y')
	pause = input('pause')

	print('programinha pra resolver contas')
	print('###############################')
	print('  BASKARA (1)      Pitágoras (3)')
	print('Biquadrada(2)   Trigonometria(4)')

	menu = (0)
	menu = input('-> ')
	print('')

while 3 == int(menu):
	print('Defina onde  está o  (x)')
	print('catetos(0) hipotenusa(1)')
	ch = (input('-> '))
	if 0 == int(ch):
		print('fx: (A)˄2 = (B)˄2 + (C)˄2')
		a = float(input('Defina o valor de (a): '))
		b = float(input('Defina o valor de (b): '))
		a = a**2
		b = b**2
		x2 = a - b 
		print(str(a)+' = x˄2 + '+str(b))
		print('x˄2= '+str(x2))
		print('x = √'+str(x2))
		x = x2**0.5
		print('x = '+str(x))
		pause = input('pause')
	elif 1 == int(ch):
		print('fx: (A)˄2 = (B)˄2 + (C)˄2')
		b = float(input('Defina o valor de (b): '))
		c = float(input('Defina o valor de (c): '))
		b = b**2
		c = c**2 
		x2 = b + c
		print('x˄2 = '+str(b)+' + '+str(c))
		print('x˄2= '+str(x2))
		print('x = √'+str(x2))
		x = x2**0.5
		print('x = '+str(x))
		pause = input('pause')
	elif 2 >= int(ch):
		erro = input('erro')

while 4 == int(menu):
	a = float(input('Defina o valor  da  hipotenusa ->'))
	b = float(input('Defina o valor do cateto menor ->'))
	c = float(input('Defina o valor do cateto maior ->')) 
	sȣ = b/a
	print('sem ȣ = '+str(b)+'/'+str(a))
	print('sem ȣ ='+str(sȣ))
	print('')
	cȣ = c/a
	print('cos ȣ = '+str(c)+'/'+str(a))
	print('cos ȣ = '+str(cȣ))
	print('')
	tȣ = b/c
	print('tg ȣ = '+str(b)+'/'+str(c))
	print('tg ȣ = '+str(tȣ))
	print('')

	sβ = c/a
	print('sem β = '+str(c)+'/'+str(a))
	print('sem β ='+str(sβ))
	print('')
	cβ = b/a
	print('cos β = '+str(b)+'/'+str(a))
	print('cos β = '+str(cβ))
	print('')
	tβ = c/b
	print('tg ȣ = '+str(c)+'/'+str(b))
	print('tg ȣ = '+str(tβ))
	print('')

	print('programinha pra resolver contas')
	print('###############################')
	print('  BASKARA (1)      Pitágoras (3)')
	print('Biquadrada(2)   Trigonometria(4)')

	menu = (0)
	menu = input('-> ')
	print('')
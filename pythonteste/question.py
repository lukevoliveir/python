Criar um script em python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

nome=input('Qual é seu nome?')

 print('Olá tudo bem ' + nome) 
--------------------------------------------------------------------------------------------

Criar um script em python que leia o dia o mes e o ano de nascimento de uma pessoa e mostre uma mesagem a data formada

dia=input('Qual é o dia que você nasceu?')

mes=input('Qual é o mes que você nasceu?')

ano=input('qual ano você nasceu?')



print('Você nasceu no dia ' , dia , ' de ' , mes , ' de ', ano)
--------------------------------------------------------------------------------------------

Criar um script em python que leia dois números e tente mostrar a soma entre eles

n1 =int(input('Digite um valo: '))

n2 =int(input('Digite o segundo valor: '))

s=n1+n2

//print('a soma entre ',  n1, ' e ', n2 , ' vale ' , s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
--------------------------------------------------------------------------------------------
crie um programa que leia dois numero e mostre a soma entre ele

n1 =int(input('Digite um valo: '))

n2 =int(input('Digite o segundo valor: '))

s=n1+n2

//print('a soma entre ',  n1, ' e ', n2 , ' vale ' , s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

--------------------------------------------------------------------------------------------

faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

DESAFIO 005:
print('====== DESAFIO05 ======')
n = int(input('Digite um número para ver seu sucessor e antecessor!: '))
su = n + 1
an = n - 1
print('O sucessor desse número é {}, e o antecessor é {}.'.format(su, an))

--------------------------------------------------------------------------------------------

crie um algoritmo que leia um numero e moste o seu dobro triplo e a raiz quadrada

DESAFIO 006:
print('====== DESAFIO06 ======')
n = int(input('Digite um número para ver seu dobro, triplo e sua raiz quadrada: '))
db = n * 2
tp = n * 3
rq = n**(1/2)
print('O dobro desse número é {}, o tripo é {}, e a raiz quadrada é {}.'.format(db, tp, rq))


--------------------------------------------------------------------------------------------

desenvolva um programa que leia as duas notas de um aluno, calule e mostre sua média

DESAFIO 007:
print('====== DESAFIO07 ======')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunta nota: '))
x = (n1 + n2)/2
print('Sua media entre essas duas notas é {}.'.format(x))


--------------------------------------------------------------------------------------------

escreva um programa que leia um valor em metros e o exia convertido em centimetros e milimetros

DESAFIO 008:
print('====== DESAFIO08 ======')
m = float(input('Digite um numero em metros para ver quanto o mesmo vale em centímetros e milímetros: '))
cm = m*100
mm = cm*10
print('Esse número vale {}cm e {}mm.'.format(cm, mm))


--------------------------------------------------------------------------------------------

faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

DESAFIO 009:
print('====== DESAFIO09 ======')
n = float(input('Digite um número para ver sua respectiva tabuada: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('1|  {}'.format(n1))
print('2|  {}'.format(n2))
print('3|  {}'.format(n3))
print('4|  {}'.format(n4))
print('5|  {}'.format(n5))
print('6|  {}'.format(n6))
print('7|  {}'.format(n7))
print('8|  {}'.format(n8))
print('9|  {}'.format(n9))
print('10| {}'.format(n10))



--------------------------------------------------------------------------------------------

crie um progama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar

DESAFIO 010:
print('====== DESAFIO010 ======')
n = float(input('Digite quantos reais você tem para ver quantos dolares você pode comprar: '))
d = n/3.27
print('Você pode comprar U${:.2f} em dolar.'.format(d))

considere 
US$1.00=R$ 3.27

--------------------------------------------------------------------------------------------

faça um programa que lei a largura e a altura de uma parede em metrosm calcule a sua área e a quantidade de tinta necessario para pinta-la, sabendo que cada lintro de tinta, pinta uma área de 2m²

DESAFIO 011:
print('====== DESAFIO011 ======')
l = float(input('Digite o comprimento em metros da parede: '))
h = float(input('Digite a altura em metros da parede: '))
a = l*h
qt = a/2
print('A área da sua parede é de {}m², sendo que você precisará de {}L de tinta para pinta-la por completo.'.format (a, qt))


--------------------------------------------------------------------------------------------

faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%de desconto.

DESAFIO 012:
print('====== DESAFIO012 ======')
x = float(input('Digite o preço do produto: '))
dx = (x*5)/100
s = x - dx
print('O preço desse produto com um desconto de 5% é R${:.2f}'.format(s))


--------------------------------------------------------------------------------------------

faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

DESAFIO 013:
print('====== DESAFIO013 ======')
x = float(input('Digite o valor de seu salario: '))
y = (x*15)/100
z = y + x
print('O seu salario com 15% de aumento iria ser: R${:.2f}'.format(z))?


--------------------------------------------------------------------------------------------






















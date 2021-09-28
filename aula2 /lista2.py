#Exercicio 1
n = 11
neg = 0

for i in range (1, n) :
 num = int(input("Digite o número " + str (i) + ": "))
 if num < 0 :
   neg = neg + 1 

print("o numero de negativos é: " + str (neg))  

#exercicio 2

n = 11
soma = 0

for i in range (1, n) :
 num = int(input("Digite o número " + str (i) + ": "))
 soma = soma + num
 
media = soma / (n - 1) 
   
print("a soma dos números é: " + str (soma) + " a média é: " + str (media))

#exercicio 3

n = 11
soma = 0

for i in range (1, n) :
 num = int (input("Digite o número " + str (i) + ": "))
 if num < 40 :
  soma= soma + num
print ("A soma dos números inferiores a 40 é: " + str (soma))

#exercício 4

soma = 0
quantidade = 0

for i in range(15, 101):
  print (i)
  soma = soma + i
  quantidade = quantidade + 1

media = soma / quantidade
print ("A soma dos números é: " + str (soma) + " e a média é de: " + str (media))

#exercicio 5

n = int(input ("Digite a quantidade de números que serão calculados: "))
soma = 0

for i in range (1,n+1) :
 num = int (input("Digite o número " + str (i) + ": "))
 soma = soma + num

media = soma / n
media = round (media, 2)

print ("A média dos números é de: " + str (media))

#exercicio 6 

n = 6
maior = 0
menor = 99999999999999
 
 
for i in range (1,n) :
 num = int (input("Digite o número " + str (i) + ": "))
 if num > maior :
  maior = num
 if num < menor :
   menor = num
 
print ("O maior número é: " + str (maior))
print ("O menor número é: " + str (menor))

#exercicio 7

a = 0
b = 1

n=6

for i in range (n) :
  print (b)
  aux = b
  b = b + a
  a = aux

#exercicio 8

n = 5

for i in range (2,n) :
  n = n*i
print (n)

fatorial = 1
n= 4
for i in range (n) :
  fatorial = fatorial * n
  n = n-1

print (fatorial)

#exercicio 9

def primo (x) :
  for i in range (2,x):
    if x % i == 0 :
      return False
    return True


n = int (input("Digite o valor de n: "))
x= 1

for i in range (n) :
  while not primo(x) :
    x = x+1
    print (x)
  x = x+1

#exercicio 10

#exercicio 11 

num=int(input('Tabuada do numero '))

for n in range (11):
  print(f'{num} x {n} = {num*n}')

#exercicio 12

nome = input("Digite a nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = 0.02
elif quantidade > 5 and quantidade <= 10:
    desconto = 0.03
elif quantidade > 10:
    desconto = 0.05
     

print(f"Total antes do desconto: {total}")
print(f"Desconto de: {(total * desconto)}")
print(f"Total após do desconto: {total * (1 - desconto)}")

#exercicio 13

soma = 0
media = 0
conceito = ""

for x in range(3):
    nota = float(input(f"Digite a {(x + 1)}º nota: "))
    soma += nota
    
media = soma / 3

if media >= 9.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
elif media < 6.0:
    conceito = "D"
    
print(f"Conceito: {conceito}")

#exercicio 14

gasolina = float(input("Digite o valor do litro da gasolina: "))
alcool = float(input("Digite o valor do litro do álcool: "))

gasolina_2 = gasolina * 0.7


if alcool <= gasolina_2:
    print("alcool é mais vantajoso.")
    print(f"Preço do litro da gasolina: {gasolina}")
    print(f"Preço do litro do álcool: {alcool}")
else:
    print("gasolina é mais vantajoso.")
    print(f"Preço do litro da gasolina: {gasolina}")
    print(f"Preço do litro do álcool: {alcool}")

#exercicio 15

idade = int(input("Digite sua idade: "))
anos_t = int(input("Digite seus anos trabalhados: "))

if idade >= 65:
    print("Pode aposentar.")
elif anos_t >= 30:
    print("Pode aposentar.")
elif idade >= 60 and anos_t >= 25:
    print("Pode aposentar")
else:
    print("Não Pode aposentar")


#exercicio 1

nomes = []
 
for i in range (10):
 nome = input("Digite um nome: ")
 nomes.append(nome)
 
print ("------")
 
ultnome = input("Digite um último nome: ")
if ultnome in nomes:
 print ("Achei")
else:
 print ("Não achei")3


#exercicio 2 

notas = []
alunos = []

for i in range (5):
  aluno = input("Digite o nome do aluno: ")
  nota = int(input("Digite a nota: "))
  alunos.append(aluno)
  notas.append(nota)

for i in range (len(notas)):
  aluno = alunos[i]
  nota = notas[i]
  print("Nome do Aluno : " + aluno + ", Nota: " +str(nota))


soma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]
media = soma / 5

print(media)

#exercicio 3 


numeros = [1, 2 , 3 , 4 , 5]
maior = 0
menor = 9999999

for i in range (5):
  if numeros [i] > maior: 
    maior = numeros [i]  
  if numeros [i] < menor: 
    menor = numeros [i]  
  

print(f"Os Valores da lista são: {numeros}")
print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")

#exercicio 4

numeros= []

for i in range(1, 6):
  num = int(input(f"Digite um numero para a posição {i}: "))
  numeros.append(num)
print(f"Os valores digitados foram: {numeros}")

numeros = numeros [::-1]

print(f"Os valores digitados na ordem inversa são: {numeros}")

#exercicio 5


lista1 = [2, 4, 6, 8, 10]
lista2 = [3, 4, 7, 8, 10]

print(f"Os valores na lista1 são: {lista1}")
print(f"Os valores na lista2 são: {lista2}")

count = 0
for i in range(len(lista1)):
  if lista1[i] == lista2[i]:
    count=count+1
print(f"Existem {count} numeros iguais na mesma posição")

#exercicio 6

lista = [1, 2, 3, 4, 5]
num = lista.append(int(input(f"Digite um número qualquer: ")))

print(f"{lista}")


quant = lista.count(lista[5])

print(f"O valor {lista[5]} aparece {quant} vezes na lista")


#exercicio 7

numeros = []

for i in range (10) :
  numero = int (input ("Digite um numero: "))
  numeros.append(numero)
  numeros.sort()
print (f"A lista ordenada em ordem crescente: {numeros}")

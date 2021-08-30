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


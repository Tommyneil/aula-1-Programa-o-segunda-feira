#exercicio 1 

txt = "Thomas Toneli Rodrigues"

indice = txt.find(" ")

print(indice)

primeironome = txt[0: indice]

print(primeironome)

sobrenome = txt[indice:].strip()
print(sobrenome)


#exercicio 2 

frases = []

def addfrase():
  for i in range (3):
    frase = str(input(f"Digite a frase {i+1}: " ))
    frases.append(frase)
    print(frase)

def busca():
  txt = input("Digite o que você quer buscar: ")
  for texto in frases:
    if texto.find(txt) != -1:
      print(texto)

addfrase()
busca()


#exercicio 3

txt = input("Digite a frase: ")

palavras = txt.split(" ")

palavras.reverse()

for palavra in palavras:
  print(palavra)

#exercicio 4
import sys

while True:

  txt = input("Digite a expressão: ")

  if txt == "sair": 
    sys.exit() 

  exp = txt.split(" ")

  operacao = exp[0]
  num1 = float(exp[1])
  num2 = float(exp[2])


  if operacao == "somar": 
    print(num1 + num2)
    
  if operacao == "multiplicar": 
    print(num1 * num2)

  if operacao == "dividir": 
    print(num1 / num2)

  if operacao == "subtrair": 
    print(num1 - num2)

  #exercicio 5

  3 splits 
  cad = "nome=Robson,email=robson.luz@fae.edu;nome=Joao,email=joao@email.com" 


usuarios = cad.split(";") 
user = cad.split(",")  
nome = user[0] 
indice = nome.find("=")  


print ("Usuários cadastrados: " + str (len(usuarios))) 
print ("===============================")

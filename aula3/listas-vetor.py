numeros = [10,20,30,40,50]
nomes = ["joao", "maria", "pedro"]


soma = 0 


for numero in numeros:
  soma = soma + numero
  
  
print(soma)

#lenght

nomes = ["joao", "maria", "pedro"]


len(nomes)

print(len(nomes))

#exercicio

nomes = ["Joao", "Maria", "Pedro"]
numeros = [18, 19, 21]


for i in range(len(nomes)):
  nome = nomes[i]
  idade = numeros[i]
  print(f"Nome: {nome}, idade:{idade}")


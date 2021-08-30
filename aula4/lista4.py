apostas = []
nomes = []
import random 
num = 0



def menu():
  print("==============================")
  print("Opções:")
  print("1 - Adicionar aposta")
  print("2 - Listar apostas")
  print("3 - Sortear um número")
  print("4 - Apresentar o ganhador")
  print("5 - Sair")


def adicionarAposta():
  aposta = int(input("Digite sua aposta entre 1 e 20: "))
  apostas.append(aposta)
  print(aposta)

def adicionarNomes():
  nome = (input("Digite seu nome: "))
  nomes.append(nome)
  print(nome)

def lista():
  for i in range (len(apostas)):
    aposta = apostas[i]
    nome = nomes [i]
    print(f"Nome: {nome}, Aposta: {aposta}")

def aleatorio():
  sorteio = random.randrange(1, 3)
  print(f"Numero sorteado: {sorteio}")
  return sorteio


def ganhador():
  print(num)
  for i in range (len(apostas)):
    aposta = apostas[i]
    nome = nomes[i]
    if num == aposta: 
      print (f"O ganhador é: {nome}")
      teveganhador = 1
  if teveganhador == 0:
    print(f"ninguém ganhou, mais sorte na próxima vez")    

opcao = 0 

while opcao != 5:
  menu()
  opcao = int(input("digite a opção: "))
  if opcao == 1:
    adicionarAposta()
    adicionarNomes()
  if opcao == 2:
    lista()
  if opcao == 3:
    num =  aleatorio()
  
  if opcao == 4:
    ganhador()







print("Game over")
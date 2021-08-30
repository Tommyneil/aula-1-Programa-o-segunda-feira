def ola() :
  print("----------")
  print(" ola python ")
  print("----------")

ola()
ola()
ola()


# função com 1 parametro


def printNumero(num):
  if num > 10:
      print(f"O numero é: {num}")

x = 10
y = 20

printNumero(x)
printNumero(y)
printNumero(30)

#função com 2 paramatros

def media(num1, num2):
  soma = num1 + num2 
  return soma / 2  



x = media1 = media(10, 20)
y = media2 = media(20, 40)

print(x)
print(y)

total = x + y 
print(total)

#media com array

def media(numeros):
  total = 0
  for num in numeros:
    total = total + num
  m = total / len(numeros)
  return m


nums = [10, 20, 30, 7, 6 ,100]

m1 = media(nums)
print(m1)






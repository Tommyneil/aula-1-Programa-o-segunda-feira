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

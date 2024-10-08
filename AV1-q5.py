for i in range(1, 51):
    preco = i *1,99
print(f"{i} -> R$ {preco:.2f}")
itens = int(input("digite a quantidade de itens"))
total = itens * 1,99
print(f"Total a pagar para {itens} itens: R$ {total:.2f}")

numero = int(input("Digite um numero inteiro: "))
if numero <= 1:
    print(f"{numero} não é um numero primo.")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
if primo:
    print(f"{numero} é um numero primo.")
else:
    print(f"{numero} não é um numero primo.")
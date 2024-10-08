numero = int(input("Digite um numero de 1 a 10: "))
if 1 <= numero <=10:
    print(f"tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print (f"{numero} x {i} = {resultado}")
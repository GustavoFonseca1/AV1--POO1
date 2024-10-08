par = 0
impar = 0
for i in range(10):
 numero = int( input(f"Digite um numero {i+1}º numero: "))
 if numero % 2:
    par +=1
 else:
    impar +=1
print(f"Quantidade de numeros pares: {par}")
print(f"Quantidade de numeros impares: {impar}")
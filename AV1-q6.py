salario = 1000
ano_final = 2025
aumento = 0.015

salario += salario * aumento

for ano in range(1997, ano_final + 1):
    aumento *= 2
    salario += salario * aumento
print(f"O salário do funcionário em {ano_final} é R$ {salario:.2f}")
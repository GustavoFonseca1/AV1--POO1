Valor_Divida = float(input("Digite o valor da divida: "))
print("Tabela de preços")

for parcelas in [1, 3, 6, 9, 12]:
    if parcelas == 1:
        juros_porcento = 0
    elif parcelas == 3:
        juros_porcento = 10
    elif parcelas == 6:
        juros_porcento = 15
    elif parcelas == 9:
        juros_porcento = 20
    elif parcelas == 12:
        juros_porcento = 25

juros = Valor_Divida * (juros_porcento / 100)
valor = Valor_Divida + juros
valor_parcela = valor / parcelas
print(f"{parcelas} parcelas - Total: R$ {valor:.2f} - Juros: R$ {juros:.2f} - Valor da parcela: R$ {valor_parcela:.2f}")
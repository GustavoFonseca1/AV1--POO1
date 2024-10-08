PA = 80000
PB = 200000
taxa_crescimentoA = 0.03
taxa_crescimentoB = 0.015
anos = 0

while PA < PB:
    PA += PA * taxa_crescimentoA
    PB += PB * taxa_crescimentoB
    anos +=1
print(f'Serão necessarios {anos} anos para que a população A ultrapasse a população B')
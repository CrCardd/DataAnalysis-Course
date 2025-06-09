import random as rd

def guerrear(defensores, atacantes):

    while(defensores > 0 and atacantes > 1):
        quantidade_ataque = min(6, atacantes)
        quantidade_defesa = min(6, defensores)

        soldados_ataque = []
        soldados_defesa = []
        for _ in range(quantidade_ataque):
            soldados_ataque.append(rd.randint(1,6))
        for _ in range(quantidade_defesa):
            soldados_defesa.append(rd.randint(1,6))
        
        soldados_defesa.sort(reverse=True)
        soldados_ataque.sort(reverse=True)

        for i in range(min(quantidade_ataque, quantidade_defesa)):
            defensores -= int(soldados_ataque[i] > soldados_defesa[i])
            atacantes  -= int(soldados_defesa[i] >= soldados_ataque[i])

    return (defensores, atacantes)


vezes = 1000
vitoria_defesa = 0
vitoria_ataque = 0
for _ in range(vezes):
    defensores, atacantes = guerrear(500, 1000)
    vitoria_defesa += int(defensores > 0)
    vitoria_ataque += int(atacantes > 1)

vitoria_ataque = round(vitoria_ataque/vezes*100,2)
vitoria_defesa = round(vitoria_defesa/vezes*100,2)
print(f'porcentagem de vitorias dos atacantes :  \t{vitoria_ataque}%')
print(f'porcentagem de vitorias dos defensores :  \t{vitoria_defesa}%')

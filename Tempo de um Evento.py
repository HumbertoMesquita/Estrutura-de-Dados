anilhas = []
aux = 0
peso_total = 0
while True:
    peso = int(input())
    if peso != 0:
        anilhas.append(peso)
    else:
        peso_desejado = int(input())
        for valor in anilhas[::-1]:
            if peso_desejado != valor and peso_desejado in anilhas:
                print(f"Peso retirado: {valor}")
                anilhas.pop()
                aux += 1
                peso_total += valor
            else:
                if peso_desejado in anilhas:
                    print(f"Peso retirado: {valor}")
                    print(f"Anilhas retiradas: {aux+1}")
                    print(f"Peso total movimentado: {peso_total+peso_desejado}")
                    quit()
                else:
                    print(f"Peso retirado: {0}")
                    print(f"Anilhas retiradas: {aux}")
                    print(f"Peso total movimentado: {peso_total}")
                    quit()
        

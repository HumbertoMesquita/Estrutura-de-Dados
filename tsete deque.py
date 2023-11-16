def deslizante(valores, inicio, fim):
    temp = []
    for pos in range(fim, inicio+fim):
        if pos <= tam_lista-1:
            temp.append(valores[pos])
            if len(temp) == inicio:
                print(f'{max(temp)} ', end = ' ')
                fim += 1
                deslizante(valores, tam_janela, fim)
        elif len(valores) <= 1:
            print(valores[0])
            quit()
        
tam_lista = int(input())
lista = input().split()
tam_janela = int(input())
valores = []
if tam_janela >= 1:
    pass
else:
    print(valores[0])
    quit()

for i in lista:
    valores.append(int(i))
deslizante(valores, tam_janela, 0)
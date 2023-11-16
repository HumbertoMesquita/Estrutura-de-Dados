def escolha(lista, tam, tam_original, dinamico):
    if len(lista) == (tam_original//2):
        print(f'{sum(dinamico)}')
        quit()
    
    if lista[0] <= lista[tam-1]:
        dinamico.append(lista[tam-1])
        lista.remove(lista[tam-1])
        
    else:
        lista.remove(lista[tam-1])
        
    escolha(lista, len(lista), tam_original, dinamico)

n = int(input())
lista_num = input().split()
valores = []
for i in lista_num:
    valores.append(int(i))
lista_num = []
escolha(valores, n, n, lista_num)



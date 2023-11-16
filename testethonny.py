lista = []
num_pre = int(input())
for i in range(num_pre):
    pretendentes = input().split()
    lista.append(pretendentes)

lista = sorted(lista, key=lambda lista: lista[2], reverse=True)
for info in lista:

    if info[2] == 180:
        
        print('bom')
    

print(lista)

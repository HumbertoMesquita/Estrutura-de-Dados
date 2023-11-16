lista = []
num_pre = int(input())
for i in range(num_pre):
    pretendentes = input().split()
    if int(pretendentes[3]) >= 75:
        pretendentes[3] = int(pretendentes[3]) - 75
    else:
        pretendentes[3] =   (75 - int(pretendentes[3]))
        #print(pretendentes[3])
        
    if int(pretendentes[2]) >= 180:
        pretendentes[2] = int(pretendentes[2]) - 180
        
    else:
        pretendentes[2] = 180 - int(pretendentes[2])
    lista.append(pretendentes)

lista = sorted(lista, key=lambda lista: (lista[2] >= 0, lista[3], lista[1], lista[0]),)



    
for i in lista:
    #print(i)
    print(f'{i[1]}, {i[0]}')

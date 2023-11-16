lista_tarefas = []
cont = 0
tarefas = input().split()
for atividade in tarefas:
    if atividade.isnumeric() != True:
        posicao = tarefas.index(atividade)
        ordenacao = int(tarefas[posicao+1])
        lista = [ordenacao, atividade]
        if tarefas.count(str(ordenacao)) >= 2:
            cont += 0.1
            ordenacao += cont
            lista = [ordenacao, atividade]
            lista_tarefas.append(lista)
        else:
            lista_tarefas.append(lista)
lista_tarefas.sort()
total_tarefas = int(input())
while total_tarefas > 0:
    total_tarefas -= 1
    lista_tarefas.pop(0)
    
print(f"Tamanho da fila: {len(lista_tarefas)}")

for i in lista_tarefas:
    print(f"Atividade: {i[1]}, Prioridade: #{int(i[0])}")




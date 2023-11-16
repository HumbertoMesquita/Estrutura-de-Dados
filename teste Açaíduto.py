def menor_caminho(n, residências, origem, destino):
    import heapq
    distâncias = [float("inf") for i in range(n)]
    distâncias[origem] = 0
    heap = [(0, origem)]
    while heap:
        custo_atual, v = heapq.heappop(heap)
        if v == destino:
            return custo_atual
        for residência in residências[v]:
            id, distância = residência
            novo_custo = custo_atual + 3.14 * distância
            if novo_custo < distâncias[id]:
                distâncias[id] = novo_custo
                heapq.heappush(heap, (novo_custo, id))
    return float("inf")

n = int(input().strip())
residências = [[]]
for i in range(n):
    line = list(map(int, input().strip().split()))
    id = line[0]
    for j in range(1, len(line[1:]), 2):
        vizinho = line[j+1]
        distância = line[j]
        residências[id].append((vizinho, distância))
        
#origem, destino = map(int, input().strip().split())
print(menor_caminho(n, residências, origem, destino))

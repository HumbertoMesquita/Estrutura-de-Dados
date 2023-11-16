def grafo(arestas,  eu, mussum):
    dist = []
    for i in arestas:
        if i[0] == eu:
            dist.append(i)
            
        if i[0] == mussum:
            dist.append(i)
            
    if len(dist) < 2:
        print('Forevis alonis...')
        
    else:
        if dist[0][1] == 0:
            print('Forevis alonis...')
            quit()
        
        if dist[1][1] == 0:
            print('Forevis alonis...')
            quit()
        
        verificacao(arestas, eu, mussum, dist, cont)
            
def verificacao(arestas, eu, mussum, dist, cont):
    for d in dist:
        if type(d) == list:
            if d[0] == mussum:
                if eu in d[2:]:
                    print(cont)
                    break
        
        
        caminho = d[2:]
        cont += 1
        verificacao(arestas, eu, mussum, caminho, cont)
                

cont = 0
num_vert = int(input())
arestas = [list(map(int, input().split())) for i in range(num_vert)]
eu, mussum = list(map(int, input().split()))
grafo(arestas, eu, mussum)


def grafo(v, a, c, arestas):
    matriz = [[0 for f in range(v)] for i in range(v)]
    
    for aresta in arestas:
        x, y, p = aresta
        matriz[x-1][y-1] = p
        
        if c == 'N':
            matriz[y-1][x-1] = p
            
    for linha in matriz:
        for i in linha:
            if i < 10:
                print(f"   {i}", end= '')
            else:
                print(f"  {i}", end= '')
                
        print()

v, a, c = map(str, input().split())
v = int(v)
a = int(a)
arestas = [list(map(int, input().split())) for i in range(a)]
grafo(v, a, c, arestas)

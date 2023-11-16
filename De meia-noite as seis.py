def str(lista):
    estudo = ''
    lista.sort()
    for i in lista:
        if i not in estudo:
            estudo += i
        
    return estudo


num_testes = int(input())
lista = []
for num in range(1, num_testes+1):
    para = 0
    stop = 0
    total = 0
    etapa = []
    conteudo = []
    palavra = input()
    cont = 0
    tam = 0
    for i in palavra:
        if i not in conteudo:
            conteudo.append(i)

    historico = conteudo.copy()
        
    for i in range(3):
        dis = input()
        etapa.append(dis)
        total += len(dis)

    for parte in etapa:
        cont += 1
        dividi = []
        
        for i in parte:
            dividi.append(i)
            
            
        tam += len(dividi)

        for letra in dividi:
            
            if letra in conteudo:
                conteudo.remove(letra)
                
            nao_tem = letra not in historico    
            copia = letra in historico
            if False == copia and para == 0:
                print("You died!")
                para = 1
                break

            elif len(conteudo) == 0 and cont != 1 and para == 0:
                print("It's in the box!")
                para = 1
                cont = 0
                break

            elif len(conteudo) == 0 and stop == 0 and para == 0:
                para = 1
                print("You died!")
                stop = 1
                break
            
            elif len(conteudo) != 0 and tam == total and nao_tem == True and copia == True:
                para = 1
                print(f"Bora ralar: {str(conteudo)}")
                
            
            
            
            
        
            

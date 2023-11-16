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
    stop = 0
    etapa = []
    conteudo = []
    palavra = input()
    cont = 0
    resto = []
    for i in palavra:
        conteudo.append(i)
    
        
    for i in range(3):
        etapa.append(input())
        

    for parte in etapa:
        cont += 1
        dividi = []
        
        for i in parte:
            dividi.append(i)
            
            
        tam = len(dividi)
        for letra in dividi:
            
            if letra in conteudo:
                conteudo.remove(letra)

            else:
                resto.append(letra)
            if len(conteudo) == 0 and len(resto) == 0 and cont != 1:
                print("It's in the box!")
                cont = 0
                
            elif len(conteudo) == 0 and len(resto) != 0 and stop == 0:
                print("You died!")
                stop = 1
                break
            
     
        if cont == 3 and len(conteudo) != 0:
            print(f"Bora ralar: {str(conteudo)}")
            
            
            
        
            


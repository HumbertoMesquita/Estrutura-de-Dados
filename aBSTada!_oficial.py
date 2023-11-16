class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

class arvorereBinaria:
    def __init__(self):
        self.raiz = None

    def incrementa(self, dado):
        novo_no = No(dado)
        if not self.raiz:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if dado < atual.dado:
                    if not atual.esq:
                        atual.esq = novo_no
                        break
                    else:
                        atual = atual.esq
                else:
                    if not atual.dir:
                        atual.dir = novo_no
                        break
                    else:
                        atual = atual.dir
        
    def print_pre(self, No):
        if No:
            print(No.dado, end=" ")
            self.print_pre(No.esq)
            self.print_pre(No.dir)

    def print_pos(self, No):
        if No:
            self.print_pos(No.esq)
            self.print_pos(No.dir)
            print(No.dado, end=" ")


arvore = arvorereBinaria()
lista= []
original = []

while True:
    item = input()
    
    if item.isnumeric() == True:
        lista.append(int(item))
        
    elif item == "in":
        print(*sorted(lista))
    
    elif item == "pre":
        
        for i in lista:
            if i not in original:
                original.append(i)
                arvore.incrementa(i)
            
        arvore.print_pre(arvore.raiz)
        print("\n", end = '')

    elif item == "pos":
        for i in lista:
            if i not in original:
                original.append(i)
                if i not in lista:
                    lista.append(i)
                arvore.incrementa(i)
                
        arvore.print_pos(arvore.raiz)
        print("\n", end = '')
        
    elif item == "quack":
        break
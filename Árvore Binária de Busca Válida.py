class ArvoreBinaria():
    
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
        

def constituiArvoreBinariaDeBusca(self):
    num = self.dado
    esq = self.esq
    dir = self.dir
    
    if esq != None:
        esquerda = self.esq.dado
        if esquerda < num:
            return constituiArvoreBinariaDeBusca(esq)
            
        else:
           return False

    if dir != None:
        direita = self.dir.dado
        if direita > num:
            return constituiArvoreBinariaDeBusca(dir)
            
           
        else:
            return False

    return True



raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))
        
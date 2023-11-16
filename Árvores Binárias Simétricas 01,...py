class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
        

def verificasubarvore(self, sub_esq, sub_dir):
    if sub_esq.dir != None and sub_dir.dir != None:
        esq = sub_esq.dir.dado
        dir = sub_dir.esq.dado
        
        if esq != dir:
            return False
        
    
    if sub_esq.esq != None and sub_dir.esq != None:
        esq = sub_esq.esq.dado
        dir = sub_dir.dir.dado
        
        if esq != dir:
            return False
        
    if sub_esq.esq == None and sub_dir.esq == None:
        return True
    
    if sub_esq.esq.esq != None and sub_esq.dir.dir != None:
        verificasubarvore(self, esq, dir)
        
    if sub_esq.esq.dir != None and sub_esq.dir.esq != None:
        verificasubarvore(self, esq, dir)
        
    '''if sub_esq.esq.esq != None or sub_esq.dir.dir != None:
        return False'''
        
    return True
        
    
def verificaSimetria(self):
    dado = self.dado
    if self.esq != None and self.dir != None:
        esq = self.esq.dado
        dir = self.dir.dado

        if esq != dir:
            return False
        
        else:
            #return verificaSimetria(self.esq) and verificaSimetria(self.dir)
            return verificasubarvore(self, self.esq, self.dir)
        
    if self.esq == None and self.dir == None:
        return True
    if self.esq == None or self.dir == None:
        return False
    
    else:
        return True

raiz = ArvoreBinaria(0)
    
raiz = ArvoreBinaria(2, ArvoreBinaria(1, ArvoreBinaria(6, 9, None), ArvoreBinaria(4, None, None)), ArvoreBinaria(1, ArvoreBinaria(4, None, None), ArvoreBinaria(6, None, None)))
print(verificaSimetria(raiz))


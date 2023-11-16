class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def verificaSimetria(arvore):
    if arvore is None:
        return True
    return Simetria_Subarvore(arvore.esq, arvore.dir)

def Simetria_Subarvore(esq, dir):
    if esq is None and dir is None:
        return True
    
    elif esq is None or dir is None:
        return False
    
    elif esq.dado != dir.dado:
        return False
    
    return Simetria_Subarvore(esq.esq, dir.dir) and Simetria_Subarvore(esq.dir, dir.esq)

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))
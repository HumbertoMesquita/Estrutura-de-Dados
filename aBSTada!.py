class ArvoreBinaria():
    def __init__(self, lista, esq = None, dir = None):
        for no in lista:
            self.dado = no
            incrementa(self, no, esq, dir)
            
            
            
        

        
        
    def incrementa(self, dado, esq, dir):
        no_atual = self.dado
        
        if dado < no_atual:
            
        
        
        '''if not self.raiz:
            self.raiz = novo_no
            
        else:
            atual = self.raiz
            while True:
                if dado < atual.esq:
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

    def print_arvore(self):
        if self.raiz:
            self._print_arvore(self.raiz)
            
            
    def _print_arvore(self, atual):
        if atual:
            self._print_arvore(atual.esq)
            print(atual.dado)
            self._print_arvore(atual.dir)'''
    



            


lista= []
while True:
    item = input()
    
    if item.isnumeric() == True:
        lista.append(item)
        
    elif item == "in":
        print(*sorted(lista))
    
    elif item == "pre":
        ArvoreBinaria(lista)
        
       
       
        
    
    elif item == "pos":
        pass
    
    elif item == "quack":
        break
    
    
    
    
    
    

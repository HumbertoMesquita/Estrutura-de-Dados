class Arvore():
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        
        
        if self.chave < chave:
            pass
            
        if self.chave > chave:
            pass
        
        else:
            Arvore(i)

    '''def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)'''
    
    
    
    
while True:
    i = int(input())
    raiz = Arvore(i)
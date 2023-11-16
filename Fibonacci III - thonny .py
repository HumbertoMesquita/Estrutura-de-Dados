def fibonacci(n, lista):
    lista.append(n)
    if n<2:
        return n
    else:
        return fibonacci(n-1, lista) + fibonacci(n-2, lista)
    
def numeros(lista):
    memoria = []
    lista.sort()
    for i in lista:
        if i not in memoria:
            print(f'{lista.count(i)} chamada(s) a fibonacci({i}).')
            memoria.append(i)

num = int(input())
lista= []
elemetos = fibonacci(num, lista)
print(f'fibonacci({num}) = {elemetos}.')
numeros(lista)








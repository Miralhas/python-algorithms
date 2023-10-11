from collections import deque

def pessoa_vendedor(pessoa):
    return pessoa[-1] == "m"

    

def breadth(grafo, nome):
    count = 0
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_vendedor(pessoa):
                print(f"{pessoa.title()}!")
                print(count)
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
                count +=1   
        
    return False


if __name__ == "__main__":
    grafo = {}
    grafo["voce"] = ["alice", "bob", "claire"]
    grafo["bob"] = ["anuj", "peggy"]
    grafo["alice"] = ["peggy"]
    grafo["claire"] = ["thom", "jonny"]
    grafo["jonny"] = []
    grafo["anuj"] = []
    grafo["thom"] = []
    grafo["peggy"] = [] 
    
    breadth(grafo, "voce")
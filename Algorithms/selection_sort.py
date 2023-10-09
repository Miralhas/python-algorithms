def find_smallest(array):
    '''
    Time Complexity: O(n^2)
    '''
    menor_valor = array[0] # Armazena o menor valor.
    menor_indice = 0 # Armazena o índice do menor valor.
    for i in range(1, len(array)): # Começa o for loop já no segundo index até o último.
        if array[i] < menor_valor:
            menor_valor = array[i]
            menor_indice = i

    return menor_indice # retorna o menor índice da lista.


def selection_sort(array):
    novoArray = [] # Cria um novo array, no qual vai ser armazenado os itens do menor ao maior valor
    for i in range(len(array)):
        menor_valor = find_smallest(array) # Chama a função que irá retornar o menor valor
        novoArray.append(array.pop(menor_valor)) # Adiciona o menor valor na nova lista e remove ele do array recebido no parâmetro
    
    return novoArray


print(selection_sort([1,1,1,1,1]))
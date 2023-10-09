def binary_search(numeros_lista, item):
    """Função com o propósito de mostrar o index de certo valor em uma lista
        Time Complexity: O(log n)
    """
    # DISCLAIMER: Para o Binary Search funcionar, a lista provida no argumeto deve estar sortida.

    # Primeiro setamos o index mais baixo e o index mais alto da lista.
    #  caso uma lista possuísse 100 elementos, o baixo seria = 0 e alto  = 99.
    baixo = 0
    alto = len(numeros_lista) - 1


    while baixo <= alto:
        # Começamos definindo o meio de nossa lista.
        meio = (alto + baixo)
        # Chute é o valor que está no meio de nossa lista.
        chute = numeros_lista[meio]

        # Caso o valor do chute seja igual o item que estamos procurando
        if chute == item:
            return meio

        # Caso o chute acabe sendo maior que o item, diminuimos a pos da lista-1
        if chute > item:
            alto = meio - 1

        # Caso o chute acabe sendo menor que o item, aumentamos o menor index em 1
        else:
            baixo = meio + 1

        # A lista vai diminuindo de tamanho até encontrarmos nosso número.
    return None


lista = [1, 2, 3, 4, 5, 6, 2, 82, 3, 4, 6, 33, 24]
print(binary_search(lista, 82))

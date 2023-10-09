from random import randint, randrange
def quick_sort(array):
    ''' Quick Sort
        Time Compelxity: O(n log(n))
    '''
    if not array:
        return array
    else:
        array = array.copy()
        pivo = array[randrange(len(array))]
        array.remove(pivo)
        menores = [i for i in array if i <= pivo]
        maiores = [i for i in array if i > pivo]

        return quick_sort(menores) + [pivo] + quick_sort(maiores)


x = [randint(0,15) for _ in range(5)]
print(x)
print(quick_sort(x))


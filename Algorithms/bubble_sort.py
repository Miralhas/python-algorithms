from random import randint
def bubble_sort(array):
    '''
    Time Complexity: O(n^2)
    '''
    for passo in reversed(range(len(array))):
        for i in range(passo):
            if array[i+1] < array[i]:
                array[i+1], array[i] = array[i], array[i+1]
    return array                

random_array = [randint(1,31) for _ in range(100)]
# print(sorted(random_array))


print(bubble_sort(random_array))
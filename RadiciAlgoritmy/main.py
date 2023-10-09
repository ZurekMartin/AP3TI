import random


# Ukol 1: Radici algoritmy
# Martin Zurek

# Selection Sort
def selection_sort(array, order_type):
    array = list(array)
    for i in range(len(array)):
        minimal_index = i
        for j in range(i + 1, len(array)):
            if order_type:
                if array[minimal_index] > array[j]:
                    minimal_index = j
            else:
                if array[minimal_index] < array[j]:
                    minimal_index = j
        array[i], array[minimal_index] = array[minimal_index], array[i]
    return list(array)


# Bubble Sort
def bubble_sort(array, order_type):
    array = list(array)
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if order_type:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return list(array)


# Insertion Sort
def insertion_sort(array, order_type):
    array = list(array)
    for i in range(1, len(array)):
        index = array[i]
        j = i - 1
        while j >= 0 and ((order_type and array[j] > index) or (not order_type and array[j] < index)):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = index
    return list(array)


array = tuple([random.randint(0, 100) for _ in range(10)])

# Nesetridene pole
print("Nesetridene pole:")
print(array)
print("")

# Setridene pole pomoci Selection Sort
print("Setridene pole pomoci Selection Sort:")
# Setridene pole pomoci Selection Sort (jeden smer)
print(selection_sort(array, True))
# Setridene pole pomoci Selection Sort (druhy smer)
print(selection_sort(array, False))
print("")

# Setridene pole pomoci Bubble Sort
print("Setridene pole pomoci Bubble Sort:")
# Setridene pole pomoci Bubble Sort (jeden smer)
print(bubble_sort(array, True))
# Setridene pole pomoci Bubble Sort (druhy smer)
print(bubble_sort(array, False))
print("")

# Setridene pole pomoci Insertion Sort
print("Setridene pole pomoci Insertion Sort:")
# Setridene pole pomoci Insertion Sort (jeden smer)
print(insertion_sort(array, True))
# Setridene pole pomoci Insertion Sort (druhy smer)
print(insertion_sort(array, False))

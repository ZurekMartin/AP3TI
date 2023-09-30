import random
# Ukol 1: Radici algoritmy
# Martin Zurek

# Selection Sort
def selection_sort(pole, typ_razeni):
    pole = list(pole)
    for i in range(len(pole)):
        minimal_index = i
        for j in range(i+1, len(pole)):
            if typ_razeni:
                if pole[minimal_index] > pole[j]:
                    minimal_index = j
            else:
                if pole[minimal_index] < pole[j]:
                    minimal_index = j
        pole[i], pole[minimal_index] = pole[minimal_index], pole[i]
    return list(pole)

# Bubble Sort
def bubble_sort(pole, typ_razeni):
    pole = list(pole)
    for i in range(len(pole)):
        for j in range(0, len(pole) - i - 1):
            if typ_razeni:
                if pole[j] > pole[j + 1]:
                    pole[j], pole[j + 1] = pole[j + 1], pole[j]
            else:
                if pole[j] < pole[j + 1]:
                    pole[j], pole[j + 1] = pole[j + 1], pole[j]
    return list(pole)

# Insertion Sort
def insertion_sort(pole, typ_razeni):
    pole = list(pole)
    for i in range(1, len(pole)):
        index = pole[i]
        j = i - 1
        while j >= 0 and ((typ_razeni and pole[j] > index) or (not typ_razeni and pole[j] < index)):
            pole[j + 1] = pole[j]
            j -= 1
        pole[j + 1] = index
    return list(pole)

pole = tuple([random.randint(0, 100) for _ in range(10)])

# nesetridene pole
print("Nesetridene pole:")
print(pole)
print("")

# setridene pole pomoci Selection Sort
print("Setridene pole pomoci Selection Sort:")
# setridene pole pomoci Selection Sort (jeden smer)
print(selection_sort(pole, True))
# setridene pole pomoci Selection Sort (druhy smer)
print(selection_sort(pole, False))
print("")

# setridene pole pomoci Bubble Sort
print("Setridene pole pomoci Bubble Sort:")
# setridene pole pomoci Bubble Sort (jeden smer)
print(bubble_sort(pole, True))
# setridene pole pomoci Bubble Sort (druhy smer)
print(bubble_sort(pole, False))
print("")

# setridene pole pomoci Insertion Sort
print("Setridene pole pomoci Insertion Sort:")
# setridene pole pomoci Insertion Sort (jeden smer)
print(insertion_sort(pole, True))
# setridene pole pomoci Insertion Sort (druhy smer)
print(insertion_sort(pole, False))

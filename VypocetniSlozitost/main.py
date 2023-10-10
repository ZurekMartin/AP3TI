# Libraries import
import random
import time


# Selection Sort function
def selection_sort(array):
    array = list(array)
    array_length = len(array)
    for i in range(array_length):
        minimal_index = i
        for j in range(i + 1, array_length):
            if array[j] < array[minimal_index]:
                minimal_index = j
        array[i], array[minimal_index] = array[minimal_index], array[i]
    return list(array)


# Bubble Sort function
def bubble_sort(array):
    array = list(array)
    array_length = len(array)
    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return list(array)


# Insertion Sort function
def insertion_sort(array):
    array = list(array)
    array_length = len(array)
    for i in range(1, array_length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return list(array)


# Stopwatch function
def stopwatch(function, array):
    start = time.time()
    function(array)
    end = time.time()
    return end - start


# Array of 10
ideal_array_of_10 = list(range(1, 11))
average_array_of_10 = tuple([random.randint(0, 100) for _ in range(10)])
worst_array_of_10 = list(range(10, 0, -1))

# Array of 100
ideal_array_of_100 = list(range(1, 101))
average_array_of_100 = tuple([random.randint(0, 100) for _ in range(100)])
worst_array_of_100 = list(range(100, 0, -1))

# Array of 1000
ideal_array_of_1000 = list(range(1, 1001))
average_array_of_1000 = tuple([random.randint(0, 100) for _ in range(1000)])
worst_array_of_1000 = list(range(1000, 0, -1))

# Array of 10 000
ideal_array_of_10000 = list(range(1, 10001))
average_array_of_10000 = tuple([random.randint(0, 100) for _ in range(10000)])
worst_array_of_10000 = list(range(10000, 0, -1))

# Array of 100 000
ideal_array_of_100000 = list(range(1, 100001))
average_array_of_100000 = tuple([random.randint(0, 100) for _ in range(100000)])
worst_array_of_100000 = list(range(100000, 0, -1))


# Function for printing measured time (array of 10)
def array_of_10():
    # Ideal array of 10
    print("Ideal array of 10:", ideal_array_of_10[:10])
    print("Selection sort:", stopwatch(selection_sort, ideal_array_of_10), "s")
    print("Bubble sort:", stopwatch(bubble_sort, ideal_array_of_10), "s")
    print("Insertion sort:", stopwatch(insertion_sort, ideal_array_of_10), "s")
    print()
    # Average array of 10
    print("Average array of 10:", average_array_of_10[:10])
    print("Selection sort:", stopwatch(selection_sort, average_array_of_10), "s")
    print("Bubble sort:", stopwatch(bubble_sort, average_array_of_10), "s")
    print("Insertion sort:", stopwatch(insertion_sort, average_array_of_10), "s")
    print()
    # Worst array of 10
    print("Worst array of 10:", worst_array_of_10[:10])
    print("Selection sort:", stopwatch(selection_sort, worst_array_of_10), "s")
    print("Bubble sort:", stopwatch(bubble_sort, worst_array_of_10), "s")
    print("Insertion sort:", stopwatch(insertion_sort, worst_array_of_10), "s")


# Function for printing measured time (array of 100)
def array_of_100():
    # Ideal array of 100
    print("Ideal array of 100:", ideal_array_of_100[:10])
    print("Selection sort:", stopwatch(selection_sort, ideal_array_of_100), "s")
    print("Bubble sort:", stopwatch(bubble_sort, ideal_array_of_100), "s")
    print("Insertion sort:", stopwatch(insertion_sort, ideal_array_of_100), "s")
    print()
    # Average array of 100
    print("Average array of 100:", average_array_of_100[:10])
    print("Selection sort:", stopwatch(selection_sort, average_array_of_100), "s")
    print("Bubble sort:", stopwatch(bubble_sort, average_array_of_100), "s")
    print("Insertion sort:", stopwatch(insertion_sort, average_array_of_100), "s")
    print()
    # Worst array of 100
    print("Worst array of 100:", worst_array_of_100[:10])
    print("Selection sort:", stopwatch(selection_sort, worst_array_of_100), "s")
    print("Bubble sort:", stopwatch(bubble_sort, worst_array_of_100), "s")
    print("Insertion sort:", stopwatch(insertion_sort, worst_array_of_100), "s")


# Function for printing measured time (array of 1 000)
def array_of_1000():
    # Ideal array of 1 000
    print("Ideal array of 1 000:", ideal_array_of_1000[:10])
    print("Selection sort:", stopwatch(selection_sort, ideal_array_of_1000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, ideal_array_of_1000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, ideal_array_of_1000), "s")
    print()
    # Average array of 1 000
    print("Average array of 1 000:", average_array_of_1000[:10])
    print("Selection sort:", stopwatch(selection_sort, average_array_of_1000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, average_array_of_1000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, average_array_of_1000), "s")
    print()
    # Worst array of 1 000
    print("Worst array of 1 000:", worst_array_of_1000[:10])
    print("Selection sort:", stopwatch(selection_sort, worst_array_of_1000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, worst_array_of_1000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, worst_array_of_1000), "s")


# Function for printing measured time (array of 10000)
def array_of_10000():
    # Ideal array of 10 000
    print("Ideal array of 10 000:", ideal_array_of_10000[:10])
    print("Selection sort:", stopwatch(selection_sort, ideal_array_of_10000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, ideal_array_of_10000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, ideal_array_of_10000), "s")
    print()
    # Average array of 10 000
    print("Average array of 10 000:", average_array_of_10000[:10])
    print("Selection sort:", stopwatch(selection_sort, average_array_of_10000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, average_array_of_10000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, average_array_of_10000), "s")
    print()
    # Worst array of 10 000
    print("Worst array of 10 000:", worst_array_of_10000[:10])
    print("Selection sort:", stopwatch(selection_sort, worst_array_of_10000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, worst_array_of_10000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, worst_array_of_10000), "s")


# Function for printing measured time (array of 100 000)
def array_of_100000():
    # Ideal array of 100 000
    print("Ideal array of 100 000:", ideal_array_of_100000[:10])
    print("Selection sort:", stopwatch(selection_sort, ideal_array_of_100000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, ideal_array_of_100000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, ideal_array_of_100000), "s")
    print()
    # Average array of 100 000
    print("Average array of 100 000:", average_array_of_100000[:10])
    print("Selection sort:", stopwatch(selection_sort, average_array_of_100000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, average_array_of_100000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, average_array_of_100000), "s")
    print()
    # Worst array of 100 000
    print("Worst array of 100 000:", worst_array_of_100000[:10])
    print("Selection sort:", stopwatch(selection_sort, worst_array_of_100000), "s")
    print("Bubble sort:", stopwatch(bubble_sort, worst_array_of_100000), "s")
    print("Insertion sort:", stopwatch(insertion_sort, worst_array_of_100000), "s")


# Calling functions
array_of_10()
print("\n\n\n\n")
array_of_100()
print("\n\n\n\n")
array_of_1000()
print("\n\n\n\n")
array_of_10000()
print("\n\n\n\n")
array_of_100000()

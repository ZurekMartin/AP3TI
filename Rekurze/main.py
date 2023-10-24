# Libraries import
import time
import numpy as np
import matplotlib.pyplot as plt


# Factorial recursive function
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Factorial iterative function
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Fibonacci sequence recursive function
def fibonacci_sequence_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sequence_recursive(n - 1) + fibonacci_sequence_recursive(n - 2)


# Fibonacci sequence iterative function
def fibonacci_sequence_iterative(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Binary search recursive function
def binary_search_recursive(array, low, high, x):
    if high >= low:
        middle = (high + low) // 2
        if array[middle] == x:
            return middle
        elif array[middle] > x:
            return binary_search_recursive(array, low, middle - 1, x)
        else:
            return binary_search_recursive(array, middle + 1, high, x)
    else:
        return -1


# Binary search iterative function
def binary_search_iterative(array, x):
    low = 0
    high = len(array) - 1
    middle = 0
    while low <= high:
        middle = (high + low) // 2
        if array[middle] < x:
            low = middle + 1
        elif array[middle] > x:
            high = middle - 1
        else:
            return middle
    return -1


# Stopwatch function
def stopwatch(function, inputs):
    times = []
    for i in inputs:
        start = time.time()
        function(i)
        end = time.time()
        times.append(end - start)
    return times


# Defining variables
inputs = np.arange(1, 513)
inputs_fibonacci_sequence = np.arange(1, 33)
array = list(range(512))
value = 256

# Calling stopwatch function
times_recursive_factorial = stopwatch(factorial_recursive, inputs)
times_iterative_factorial = stopwatch(factorial_iterative, inputs)
times_recursive_fibonacci = stopwatch(fibonacci_sequence_recursive, inputs_fibonacci_sequence)
times_iterative_fibonacci = stopwatch(fibonacci_sequence_iterative, inputs_fibonacci_sequence)
times_recursive_binary_search = stopwatch(binary_search_recursive, inputs)
times_iterative_binary_search = stopwatch(binary_search_iterative, inputs)

# Plotting graph for factorial
plt.plot(inputs, times_recursive_factorial, label='Recursive')
plt.plot(inputs, times_iterative_factorial, label='Iterative')
plt.title('Factorial')
plt.xlabel('Počet prvků')
plt.ylabel('Průměrný čas (s)')
plt.legend()
plt.show()

# Plotting graph for fibonacci sequence
plt.plot(inputs_fibonacci_sequence, times_recursive_fibonacci, label='Recursive')
plt.plot(inputs_fibonacci_sequence, times_iterative_fibonacci, label='Iterative')
plt.title('Fibonacci sequence')
plt.xlabel('Počet prvků')
plt.ylabel('Průměrný čas (s)')
plt.legend()
plt.show()

# Plotting graph for binary search
plt.plot(inputs, times_recursive_binary_search, label='Recursive')
plt.plot(inputs, times_iterative_binary_search, label='Iterative')
plt.title('Binary search')
plt.xlabel('Počet prvků')
plt.ylabel('Průměrný čas (s)')
plt.legend()
plt.show()

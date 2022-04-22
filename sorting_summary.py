import random
from typing import Match

def less(x, y):
    return x < y

def eq(x, y):
    return x == y

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def move(array, i, j):
    array[i] = array[j]

def isSorted(array):
    for i in range(len(array) - 1):
        if less(array[i + 1], array[i]):
            return False
    return True

# bubble sort
def bubbleSort(array):
    for i in range(len(array)):
        j = len(array) - 1
        while j > i:
            if less(array[j], array[j - 1]):
                swap(array, j, j - 1)
            j -= 1

# insertion sort
def insertionSort(array):
    i = len(array) - 1
    while i > 0:
        if less(array[i], array[i - 1]):
            swap(array, i, i - 1)
        i -= 1

    i = 1
    while i < len(array):
        val = array[i]
        j = i
        while less(val, array[j - 1]):
            move(array, j, j - 1)
            j -= 1
        array[j] = val
        i += 1

# selection sort
def selectionSort(array):
    for i in range(len(array)):
        min = i
        j = i + 1
        while j < len(array):
            if less(array[j], array[min]):
                min = j
            j += 1        
        swap(array, i, min)

# merge sort
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        # Sort the two halves
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    
# quick sort
def quickSort(array, lo, hi):
    if lo < hi:
        i = partition(array, lo, hi)
        quickSort(array, lo, i - 1)
        quickSort(array, i + 1, hi)

def partition(array, lo, hi):
    pivot = array[hi]
    i = lo - 1
    for j in range(lo, hi):
        if array[j] <= pivot:
            i = i + 1
            swap(array, i, j)

    swap(array, i + 1, hi)

    return i + 1

# counting sort
def countingSort(array):
    size = len(array)
    output = [0] * size
    maximum = max(array)

    # Initialize count array
    count = [0] * (maximum + 1)

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, maximum + 1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

# shell sort
def shellSort(array, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

# heap sort
def heapSort(array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        swap(array, i, 0)

        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        swap(array, i, largest)
        heapify(array, n, largest)

# implementation
lower = input("The lower bound of random numbers: ")
upper = input("The upper bound of random numbers: ")
algo = input("The desired sorting algorithm: ")
randomlist = []
for i in range(0,31):
    n = random.randint(int(lower), int(upper))
    randomlist.append(n)
print("The original array is: ")
print(randomlist)


if algo == "quick":
    print(f"After {algo} sort: ")
    quickSort(randomlist, 0, len(randomlist) - 1)
elif algo == "shell":
    print(f"After {algo} sort: ")
    shellSort(randomlist, len(randomlist))
elif algo == "insertion":
    print(f"After {algo} sort: ")
    insertionSort(randomlist)
elif algo == "bubble":
    print(f"After {algo} sort: ")
    bubbleSort(randomlist)
elif algo == "selection":
    print(f"After {algo} sort: ")
    selectionSort(randomlist)
elif algo == "counting":
    print(f"After {algo} sort: ")
    countingSort(randomlist)
elif algo == "merge":
    print(f"After {algo} sort: ")
    mergeSort(randomlist)
elif algo == "heap":
    print(f"After {algo} sort: ")
    heapSort(randomlist)
else:
    print("Wrong algorithm name, please choose one of insertion, selection, bubble, merge, quick, heap, shell and counting algorithms")
    quit()

if isSorted(randomlist):
    print(randomlist)
else:
    print("The list is not sorted")

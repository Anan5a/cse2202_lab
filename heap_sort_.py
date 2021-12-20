def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    r = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n_ = len(arr)
print("Sorted array is")
for i_ in range(n_):
    print("%d " % arr[i_], end='')

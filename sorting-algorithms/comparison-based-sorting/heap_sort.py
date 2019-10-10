import random


# initializes the list with random numbers
def getData(n):
    data = [0] * n

    for i in range(n):
        data[i] = random.randint(1, 100)

    return data


# sort function
def sort(arr, n):
    heapify(arr, n)

    i = n
    while i > 0:
        arr[0], arr[i] = arr[i], arr[0]
        n = n - 1
        maxHeap(arr, 0, n)
        i -= 1

    return arr


# function to build a heap
def heapify(arr, n):
    i = n / 2

    while i >= 0:
        maxHeap(arr, i, n)
        i -= 1


# function to swap the largest element in heap
def maxHeap(arr, i, n):
    left = 2 * i
    right = 2 * i + 1

    max_val = i

    if left <= n and arr[left] > arr[i]:
        max_val = left
    if right <= n and arr[right] > arr[max_val]:
        max_val = right
    if max_val != i:
        arr[i], arr[max_val] = arr[max_val], arr[i]
        maxHeap(arr, max_val, n)


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)

    print("Before Sorting -> {0:}".format(data))

    print("After Sorting -> {0:}".format(sort(data, len(data) - 1)))


if __name__ == '__main__':
    main()

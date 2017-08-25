import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


def binarySearch(arr, value):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) / 2

        if arr[mid] == value:

            return True

        elif value < arr[mid]:

            last = mid - 1

        else:
            first = mid + 1

    return False


def interpolationSearch(arr, key):
    low = 0
    high = len(arr) - 1

    while arr[low] <= key <= arr[high]:

        diff = arr[high] - arr[low]

        pos = low + int((high - low) * (key - arr[low]) / diff)

        if key > arr[pos]:
            low = pos + 1
        elif key < arr[pos]:
            high = pos - 1
        else:
            return True

    return False


def linearSearch(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return True

    return False

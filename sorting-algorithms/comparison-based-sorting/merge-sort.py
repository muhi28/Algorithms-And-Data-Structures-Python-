import random


def merge(left, right):
    result = []

    i = 0
    j = 0
    while len(result) < len(left) + len(right):

        if left[i] < right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])

            break

    return result


def mergeSort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) / 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    return merge(left, right)


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)

    print("Data before sorting -> {0:}".format(data))

    output = mergeSort(data)

    print("Data after sorting with Merge Sort -> {0:}".format(output))


if __name__ == '__main__':
    main()

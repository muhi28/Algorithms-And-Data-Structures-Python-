import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


# sorts the data based on the counting sort algorithm
def countingSort(arr, max_value):
    m = max_value + 1

    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0

    for a in range(m):

        for b in range(count[a]):
            arr[i] = a
            i += 1
    return arr


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)
    print("Data before Sorting -> {0:}".format(data))

    print("Data after Sorting -> {0:}".format(countingSort(data, max(data))))


if __name__ == '__main__':
    main()

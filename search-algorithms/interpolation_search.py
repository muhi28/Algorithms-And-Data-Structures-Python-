import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


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
            return "True | Index -> {0:d}".format(pos)

    return "False | Index -> null"


def main():
    data_size = int(input("How many elements do you want to insert?\t"))
    data = getData(data_size)
    print(f"Data -> {data:}")

    # search for random number between 1 and 100
    print(f"Found value -> {interpolationSearch((data), random.randint(1, 100)):s}\n")

    # search for fixed number
    data = [2, 4, 8, 20, 30, 80, 140, 857, 900]
    print(f"Data -> {data:}")
    print(f"Found value -> {interpolationSearch(data, 30):s}")


if __name__ == '__main__':
    main()

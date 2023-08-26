def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def sort012(array, end):
    start = mid = 0
    pivot = 1

    while mid <= end:
        if array[mid] < pivot:
            swap(array, start, mid)
            start = start + 1
            mid = mid + 1
        elif array[mid] > pivot:
            swap(array, mid, end)
            end = end - 1
        else:
            mid = mid + 1


if __name__ == '__main__':
    array = [2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 2,  0, 1]
    sort012(array, len(array) - 1)
    print(array)

def binarySearch(array, left, right, key):

    if left > right:
        return -1

    mid = (left + right) // 2

    if key == array[mid]:
        return mid

    elif key < array[mid]:
        return binarySearch(array, left, mid - 1, key)

    else:
        return binarySearch(array, mid + 1, right, key)


if __name__ == '__main__':

    A = [2, 5, 6, 8, 9, 10]
    key = 5

    (left, right) = (0, len(A) - 1)
    index = binarySearch(A, left, right, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")
def mergeSort(left, right):
    newList = []

    if len(left) == 1 and len(right) == 1:
        if (left[0] < right[0]):
            newList = left + right
        else:
            newList = right + left

    else:
        while len(left) >= 1 and len(right) >= 1:
            if left[0] <= right[0]:
                newList.append(left.pop(0))
            else:
                newList.append(right.pop(0))

        newList = newList + left
        newList = newList + right

    return newList


def merge(list):
    if len(list) == 1:
        return list

    # split in 2
    left = list[0:len(list)//2]
    right = list[len(list)//2:]
    leftSorted = merge(left)
    rightSorted = merge(right)

    return mergeSort(leftSorted, rightSorted)


a = [5, 4, 33, 21, 6, 7, 8]

print("Initial: ", a)
f = merge(a)
print("Sorted: ", f)

def quickSort(list):
    pivot = list[0]
    left = []
    right = []
    for i in range(1, len(list)):
        if (list[i] > pivot):
            right.append(list[i])
            quickSort(right)

        else:
            left.append(list[i])
            quickSort(left)


a = [5, 1, 4, 2, 6, 3]
print("Initial: ", a)
quickSort(a)
print("Final: ", a)
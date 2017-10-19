def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def selectionSort(list):
    for i in range(0, len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j

        swap(list, i, min)


a = [5, 1, 6, 2, 4, 3]
print(a)
selectionSort(a)
print(a)
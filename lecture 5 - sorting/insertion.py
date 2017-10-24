
def insertionSort(list):
    for i in range(1, len(list)):
        for j in range(0, i):
            if (list[i] < list[j]):
                item = list.pop(i)
                list.insert(j, item)

a = [5, 1, 4, 2, 6, 3]
print("Initial: ", a)
insertionSort(a)
print("Final: ", a)
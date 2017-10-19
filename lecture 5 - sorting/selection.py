def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def selectionSort(list):
    counter = 0
    for i in range(0, len(list)):
        min = i
        for j in range(i + 1, len(list)):
            counter += 1
            if list[j] < list[min]:
                min = j

        swap(list, i, min)

    size = len(list)
    print("Size: ", size, " comparisons: ", counter, " theory:", size*(size-1)/ 2)

a = [5, 1, 6, 2, 4, 3]
print(a)
selectionSort(a)
print(a)

for i in range(5, 11):
    temp = []
    for x in range(0, i):
        temp.append(x)

    selectionSort(temp)

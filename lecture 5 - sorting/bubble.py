from selection import swap

def bubbleSort(list):
    for j in range(0, len(list) - 1):
        counter = 0
        for i in range(0, len(list) - 1):
            if (list[i] > list[i+1]):
                counter += 1
                swap(list, i, i+1)

            print(list)

        print("-------", counter)
        if (counter == 0):
            print("break")
            break

a = [5, 1, 4, 2, 6, 3]
print("Initial: ", a)
bubbleSort(a)
print("Final: ", a)

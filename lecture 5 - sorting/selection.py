a = [5, 1, 6, 2, 4, 3]
print(a)
for i in range(0, len(a)):
    min = i
    for j in range(i + 1, len(a) - 1):
        if a[j] > a[min]:
            min = j

    temp = a[i]
    a[j] = a[min]
    a[min] = temp

print(a)
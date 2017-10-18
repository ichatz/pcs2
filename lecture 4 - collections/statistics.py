import math

# This function computes the median of a list of numbers
def computeMEDIAN(l):
    md = 0.0
    if len(l) % 2 == 1:
        md = l[(len(l) - 1) // 2]
    else:
        right_ext = (len(l) + 1) // 2
        left_ext = (len(l) - 1) // 2
        md = (l[left_ext] + l[right_ext]) / 2
    return md

# This function computes the standard deviation
def computeSTDDEV(l, average):
    sd = 0.0
    sum2 = 0.0
    for value in l:
        x = (average - value) ** 2
        sum2 += x
    sd = math.sqrt((sum2 / (len(l) - 1)))
    return sd

# initialize variables
sum = 0.0
count = 0
sum2 = 0

# Collect input from user/keyboard
xStr = input("Give me a number (press <Enter> to quit): ")
l = []
while xStr != "":
    x = eval(xStr)
    l.append(x)
    sum += x
    count += 1
    xStr = input("Give me a number (press <Enter> to quit): ")

# Compute statistics
average = sum / count
sd = computeSTDDEV(l, average)
md = computeMEDIAN(l)

# Print statistics
print("\n`The average value is", average)
print("\nValues:", l)
print("The standard deviation is ", sd)
print("The median is: ", md)

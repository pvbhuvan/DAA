a = eval(input("enter the list: "))
n = len(a)
for i in range(len(a)):
    pos = i
    for j in range(i + 1, len(a)):
        if a[j] < a[pos]:
            pos = j
    temp = a[i]
    a[i] = a[pos]
    a[pos] = temp
print("sorted array: ",a)
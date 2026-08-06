def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    temp = a[i + 1]
    a[i + 1] = a[high]
    a[high] = temp

    return i + 1

def quick(a, low, high):
    if low < high:
        p = partition(a, low, high)

        quick(a, low, p - 1)
        quick(a, p + 1, high)

def quick_sort(a):
    quick(a, 0, len(a) - 1)
    return a

a = eval(input("Enter list: "))
print(quick_sort(a))
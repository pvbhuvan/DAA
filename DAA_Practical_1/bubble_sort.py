a=eval(input("enter the list: "))
n= len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("sorted array: ",a)
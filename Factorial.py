def iterative_way(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i 

    return fact 

def recursive_way(n) :
    
    if n == 0 or n == 1 :
        return 1
    else:
        return n * recursive_way(n-1)


n = int(input("Enter any number: "))
print("\n1, Iterative way: ")
print("2, Recursive way: ")
choice = int(input("Choose option 1 or option 2: "))

if choice == 1:
    print(iterative_way(n))
elif choice == 2:
    print(recursive_way(n))



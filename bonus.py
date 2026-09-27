integers = []

n =int(input("Enter number of elements : "))

for i in range(n):
    i = int(input("Enter element : "))
    integers.append(i)

largest : int = min(integers)
sec_largest : int = None

for num in integers:
    if num > largest:
        sec_largest = largest
        largest = num
    
print("Largest : ",largest)
print("Second largest : ",sec_largest)


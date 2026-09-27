integers = []

n =int(input("Enter number of elements : "))

for i in range(n):
    i = int(input("Enter element : "))
    integers.append(i)

print("Elements in the array : ",integers)

list = []

for i in integers:
    if i not in list:
        list.append(i)

print("Elements in the array after removing all the duplicates : ",list)
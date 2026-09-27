integers = []

n =int(input("Enter number of elements : "))

for i in range(n):
    i = int(input("Enter element : "))
    integers.append(i)

def array_sum(arr : list[int], index : int) -> int:
    if index == -1 : return 0

    return arr[index] + array_sum(arr, index-1)

result : int = array_sum(integers, len(integers)-1)

print("Sum of the elements of the array is : ",result)
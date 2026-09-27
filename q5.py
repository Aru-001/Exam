integers = []

n =int(input("Enter number of elements : "))

for i in range(n):
    i = int(input("Enter element : "))
    integers.append(i)

target : int = int(input("Enter the target value: "))

low : int = 0
high : int = len(integers)

def merge_sort(arr : list[int]):
    if len(arr) <= 1 : return arr

    mid : int = len(arr) // 2

    left_arr : list[int] = arr[:mid]
    right_arr : list[int] = arr[mid:]

    left : int = merge_sort(left_arr)
    right : int = merge_sort(right_arr)

    return merge(arr,left, right)

def merge(arr : list[int], left_arr : list[int], right_arr : list[int]):
    merged_arr = []
    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i+=1
        else:
            merged_arr.append(right_arr[j])
            j+=1

    if i < len(left_arr):
        merged_arr.extend(left_arr[i:])
    if j < len(right_arr):
            merged_arr.extend(right_arr[j:])

    return merged_arr

result = merge_sort(integers)
print("Sorted array : ",result)


def binary_search(arr : list[int], low : int, high : int, target : int) -> int:
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target: return mid
    elif arr[mid] > target : return binary_search(arr,low, mid - 1, target)
    else : return binary_search(arr,mid + 1, high, target)

index : int = binary_search(result, low, high, target)

if index != -1:
    print(f"Element found at {index + 1} position in the sorted array")
else:
    print("not found...index : -1")
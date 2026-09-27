string : str = input("Enter a string : ")
length = len(string) - 1
def reverse(string : str, i : int) -> str:
    if i < 0:
        return ""

    return string[i] + reverse(string, i-1)

result = reverse(string, length)
print(result)

if result == string:
    print("Palindrome")
else:
    print("Not Palindrome")


string = input("Enter a string : ")

frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("The frequency of the characters in the entered string is : ", frequency)

for ch in frequency:
    if frequency[ch] == 1:
        print(frequency[ch])
        break
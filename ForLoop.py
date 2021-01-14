numbers = [1, 5, 5, 6, 3, 5, 3, 2]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
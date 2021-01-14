terms = int(input("Enter the number of terms: "))

#use anonymous function10
result = list(map(lambda x: 2**x, range(terms)))

#display the result
print("The total terms is: ", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])
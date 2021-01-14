weight = int(input("Enter weight: "))
units = input("(L)bs or (K)g: ")

if units.upper() == "L":
    converted_weight = weight * 0.45
    print(f"Your weight is {converted_weight} kilos")

elif units.upper() == "K":
    converted_weight = weight / 0.45
    print(f"Your weight is {converted_weight} pounds")

else:
    print("Unexpected input!")


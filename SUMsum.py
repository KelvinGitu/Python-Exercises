for i in range(0, 23):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    def multiply_no(one, two):
        return one*two

total = [8397.9, 8367.8, 8823.6, 8346.3, 8518.3, 8741.9,
        8711.8, 12539.2, 12376, 13375.6, 13552.4, 14048, 12896,
        5889, 5238, 6675, 7699.5, 4957.5, 4737.5, 13976, 7861.5,
        15744, 14496]
sumsum = 0
for number in total:
    sumsum += number
print(sumsum)
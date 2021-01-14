num = int(input("Enter number: "))
#prime numbers are greater than 1
if num>1:
    #check for factors
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
        else:
            print(num, "is a prime number")
            break

#if input is less than or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

def recur_fibo(n):
    """Recursive function to 
    print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

num = int(input("Integer: "))
total = 0

#check if the number of terms is valid
if num <= 0:
    print("Invalid, number can't be negative")
elif type(num) == float or type(num) == str:
    print("Invalid input, number must be positive integer")
else:
    for i in range(num):
        print(recur_fibo(i), end=' ') 
        # for n in recur_fibo(i):
        #     if n %2 == 0:
        #         return total += n
                
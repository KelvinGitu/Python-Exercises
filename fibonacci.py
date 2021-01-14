def fibSum(n):
    """ the function returns sum of even numbers in a fibonacci
            sequence between 1 and an input number """

    list_sequence=[1,2]
    if num == 0:
        return 0
    elif n<=0:
        print("Invalid, number can't be negative")
    elif isinstance(num, float) or isinstance(num, str)  :
        print("Invalid input, number must be positive integer")
    elif n==1:
        return list_sequence
    a=1
    b=2

    total = 0
    for i in range(0,n-1):
        b=a+b
        a=b-a
        list_sequence.append(b)

        even_list = filter(lambda n: n%2 == 0, list_sequence)
    return sum(even_list)

num = int(input("Integer: "))
fibSum(num)

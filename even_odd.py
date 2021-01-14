def even_odd(list_of_num):
    print(numbers)

    # even_num = list(filter(lambda number: number % 2 == 0, numbers))
    # print("Number of even numbers: ", len(even_num))

    # odd_num = list(filter(lambda number: number % 2 != 0, numbers))
    # print("Number of odd numbers: ", len(odd_num))

    even_num = [
        number
        for number in numbers
            if number % 2 == 0
    ]
    odd_num = [
        number
        for number in numbers
            if number % 2 != 0
    ]

    print("Number of even numbers is: ", len(even_num))
    print("number of odd numbers is: ", len(odd_num) )
numbers = range(23, 114)
even_odd(numbers)

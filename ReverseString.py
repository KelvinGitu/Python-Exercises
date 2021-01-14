def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1
name = str(input("Enter a name: "))
print(string_reverse(name))

""" def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("Enter a name")
print(reverse(s)) """ 

#a stack based function to reverse a string
""" 
def reverse(string):
    n = len(string)

#create an empty stack
stack = createStack()

#push all characters of string to stack
for i in range(0, n, 1):
    push(stack, string[i])

#making the string emptysince all characters are savedin stack
string = " "

#pop all characters of string and put them back to string
for in range(0, n, 1):
    string+=pop(stack)

return string

string = input("Enter a string of letters")
  """
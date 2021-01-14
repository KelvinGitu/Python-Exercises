#initializes size of stack as zero
def createStack():
    stack = []
    return stack

#function to determine size of stack
def size(stack):
    return len(stack)

#stack is empty if size is zero
def isEmpty(stack):
    if size(stack) == 0:
        return True
#function top add an item to a stack, increases size by one
def push(stack, item):
    stack.append(item)
#function to remove an item to a stack, decreases size by one
def pop(stack):
    if isEmpty(stack): return
    return stack.pop
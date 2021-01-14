hon -m django --version#This is a progammatical solution tlo a logical puzzle. 
#The aim is to find which box the gold is in.
#The boxes come with statements, one of which is true and the other two which are false.

#box 1 says "The gold is not here"
#box 2 says "The gold is not here"
#box 3 says "The gold is in the second box"

#This version also shows you which box has the gold in it

box1, box2, box3 = [], [], []
def checker(b1, b2, b3):
    """checks whether a proposed solution is valid. Truth 
    values must add to 1 sice there is one true and two false statements.
    Statements b2 and b3 contradict each other, so cannot have the same
    truth values"""

    if b3 == 1:
        b1 = 1
    if (b1 + b2 + b3 == 1) and ((b2 and b3) == 0) and ((b2 or b3) == 1):
        return True
    else:
         return False
def gold_finder(b1, b2, b3):
    if checker(b1, b2, b3):
        if b1 == 0:
            box1.append("gold")
        elif b2 == 0:
            box2.append("gold")
        elif b3 == 1:
            box2.append("gold")
        elif (b1 and b2) == 1:
            box3.append("gold")
        print("Box 1:", box1, "Box 2:", box2, "Box 3:", box3)
    else:
        print("This is not a valid solution.")

gold_finder(1, 0, 0)
gold_finder(0, 1, 0)
gold_finder(0, 0, 1)

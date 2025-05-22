def testfunc(myname):
    print('Hello %s!'% myname)
    
myname = input("What is your name? ")
testfunc(myname)

def test(fname, lname):
    print('Hello %s %s!'% (fname, lname))
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
test(firstname, lastname)

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
pocket_money = float(input("How much pocket money do you have? "))
paper_route = float(input("How much paper route do you have? "))
spending = float(input("How much have you spent? "))
print(savings(pocket_money, paper_route, spending))

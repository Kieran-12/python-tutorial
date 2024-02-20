#calculator with eval
problem = input("Input a problem, or press q to quit: ")

while(problem != 'q'):
    print(f"The answer is {eval(problem)}.")
    problem = input("Input another problem, or press q to quit: ")

print("Thank you for using me, bye bye.")
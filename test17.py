def celsiustofahrenheit(celcius):
    temp = (celcius * 9 / 5) + 32
    print(float(temp))


def farenheittocelcius(farenheight):
    temp = (farenheight - 32) * 9 / 5
    print(float(temp))


print("Welcome to the temperature comverter!")
while True:
    measurement = input(
        "Are you converting from Celcius to Farenheight (type C), or converting from Farenheight to Celcius (type F)? "
    )
    temp = float(input("How many degrees? "))
    if measurement == "C" or "c":
        celsiustofahrenheit(temp)
        break
    elif measurement == "F" or "f":
        farenheittocelcius(temp)
        break
    else:
        print("Invalid response, please write 'C' or 'F'.")

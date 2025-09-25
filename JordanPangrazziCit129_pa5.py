##Jordan Pangrazzi
##9/24/25
##Portfolio Project
##Convert temperatures from Fahreinheit, Celsius, or Kelvin to the other two formats


degCon = input("Enter the degree conversion code: ")    ##input conversion code
if degCon != "F" and degCon != "C" and degCon != "K":   ##code must be either F, C, or 
    print("INVALID code")          ##invalid if anything other than F, C, or K
else:
    tempVal = 0
    if degCon == "F":
        tempVal = float(input("Enter the temperature value in degrees farenheit: "))    ##input temp in Fahrenheit
    elif degCon == "K":
        tempVal = float(input("Enter the temperature value in degrees Kelvin: "))     ##input temp in Kelvin
    elif degCon == "C":
        tempVal = float(input("Enter the temperature value in degrees Celsius: "))    ##input temp in Celsius
    if tempVal < -500 or tempVal > 500:                             
        print("INVALID value for temperature - setting temperature value to 100")    ##invalid if out of perameters, set to 100 
    if degCon == "F" and (tempVal < -500 or tempVal > 500):      ##if F and out of perameters, set it to 100 and convert
        tempVal = 100
        C = (tempVal - 32) * 5/9      ##Farenheit math conversion to celsius
        K = (tempVal + 459.67) * 5/9     ##Farenheit math conversion to kelvin
        print("Temperature in degrees Celsius: ", format(C, '.2f'), " Celsius", sep = "")   ##output temp in celsius, format to 2 decimal spaces with .2f, and sep empty string to avoid extra spacing inbetween characters 
        print("Temperature in degrees Kelvin: ", format(K, '.2f'), " Kelvin", sep = "")
    elif degCon == "K" and (tempVal < -500 or tempVal > 500):
            tempVal = 100
            C = (9/5 * tempVal - 491.67) * 5/9    ##Kelvin math conversion to Celsius
            F = 9/5 * tempVal - 459.67            ##Kelvin math conversion to Farenheit
            print("Temperature in degrees Celsius: ", format (C, '.2f'), " Celsius", sep = "")
            print("Temperature in degrees Kelvin: ", format(F, '.2f'), " Fahrenheit", sep = "")
    elif degCon == "C" and (tempVal < - 500 or tempVal > 500):
            tempVal = 100
            F = tempVal * 9/5 + 32                ##Celsius math conversion to Fahrenheit
            K = (9/5 * tempVal + 491.67) * 5/9    ##Celcius math conversion to Kelvin
            print("Temperature in degrees Farenheit: ", format(F, '.2f'), "Fahrenheit", sep = "")
            print("Temperature in degrees Kelvin: ", format(K, '.2f'), " Kelvin", sep = "")
    else:
        if degCon == "F":         #if value entered is within parameters, perform this now
            C = (tempVal - 32) * 5/9
            K = (tempVal + 459.67) * 5/9
            print("Temperature in degrees Celsius: ", format(C, '.2f'), " Celsius", sep = "")
            print("Temperature in degrees Kelvin: ", format(K, '.2f'), " Kelvin", sep = "")
        elif degCon == "C":
            F = tempVal * 9/5 + 32
            K = (9/5 * tempVal + 491.67) * 5/9
            print("Temperature in degrees Farenheit: ", format(F, '.2f'), " Fahrenheit", sep = "")
            print("Temperature in degrees Kelvin: ", format(K, '.2f'), " Kelvin", sep = "")
        elif degCon == "K":
            F = 9/5 * tempVal - 459.67
            C = (9/5 * tempVal - 491.67) * 5/9
            print("Temperature in degrees Celsius: ", format (C, '.2f'), " Celsius", sep = "")  ##remember to include the name of the conversion at the end, but before sep
            print("Temperature in degrees Farenheit: ", format(F, '.2f'), " Fahrenheit", sep = "")

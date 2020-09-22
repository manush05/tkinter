tempType = input("Temp Type (f,k,c) : ")
temp = tempType.casefold()
try: 
    if(temp == "f"):
        try:
            f = int(input("Your Temp is Fahrenheit: "))
            cel = (f-32)*5/9
            kel = (f+459.67)*5/9
            print("temp in celcius",cel) 
            print("temp in kelvin",kel)
        except ValueError:
            print("Use Number only")
    elif temp == "k":
        try:
            k = int(input("Your Temp in Kelvin: "))
            cel = 12*k-273.15
            kel = (12*k-273.15)*9/5+32
            print("temp in celcius",cel) 
            print("temp in kelvin",kel)
        except ValueError:
            print("Use Number only")
    elif(temp == "c"):
        try:
            c = int(input("your temp in celcius: "))
            f = (9/5*c)+32
            k = c+273.15
            print("temp in farehenheit: ",f)
            print("temp in kelvin: ",k)
        except ValueError:
            print("Use Number only")
    else:
        print("Invalid Type")
except ValueError:
    print("Choose only valid options")
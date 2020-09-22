distType = input("Dist Unit (km,miles,m) : ")
unit = distType.casefold()
try: 
    if(unit == "km"):
        try:
            km = int(input("Your Distance in KM: "))
            mph = km/1.609
            m = km*1000
            print("distance in meters",m) 
            print("Distance in Miles per hr",mph)
        except ValueError:
            print("Use Number only")
    elif(unit == "miles"):
        try:
            miles = int(input("Your Distance in KM: "))
            Km = miles*1.609
            # m = km*1000
            # print("distance in meters",m) 
            print("Distance in Miles per hr",mph)
        except ValueError:
            print("Use Number only")
    # elif(temp == "c"):
    #     try:
    #         c = int(input("your temp in celcius: "))
    #         f = (9/5*c)+32
    #         k = c+273.15
    #         print("temp in farehenheit: ",f)
    #         print("temp in kelvin: ",k)
    #     except ValueError:
    #         print("Use Number only")
    # else:
    #     print("Invalid Type")
except ValueError:
    print("Choose only valid options")
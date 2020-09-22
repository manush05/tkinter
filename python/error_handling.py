print("Hello World")
# a = "string"

try:
    print(a)
except NameError:
    print("varaiable a not Found")
except:
    print("Error")

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
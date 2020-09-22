# READ FILE
readfile = open("test.txt","r")
print(readfile.read())
print(readfile.read(7))

readline = open("test.txt", "r")
print(readline.readline())
print(readline.readline())

for i in readline:
    print(i)
readline.close()

# CREATE FILE
createfile_x = open("demo.txt","x")
# if file exist give error

createfile_w = open("new.txt",'w')
createfile_a = open("text.txt",'a')

# append in a existing file
appendfile = open("test.txt",'a')
appendfile.write("add another Content")
appendfile.close()

# overwrite text 
overwrite = open("text.txt",'w')
overwrite.write("This is overwrite content")

# Delete Files
import os
# os.remove("demo.txt")


# CHECK IF EXIST
import os
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
else:
  print("The file does not exist")

# REMOVE DIRECTORY
os.rmdir("delete")


# with : automatic closing the file 
with open('test.txt','r') as auto_close:
     print(auto_close.read())

# OOPS
# INHERITANCE
# DATABASE CONNECTION

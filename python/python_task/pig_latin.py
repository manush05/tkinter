words = input("Enter some text:")
print("You Entered:",words)

words = words.split(" ")

for i in words:
    if len(i)>=3:
        i = i + "%say" %(i[0])
        i = i[1:]
        print(i)
    else:
        pass
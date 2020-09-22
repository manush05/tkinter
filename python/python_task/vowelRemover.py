text = "this is me"
vowel = ['a','i','e','o','u']
queryword = text.split(" ")

for word in queryword:
    if word not in vowel:
        print(word)

# resultword = [word for word in queryword if word.lower() not in vowel]
# result = ' '.join(resultword)

# print(result)
# # 

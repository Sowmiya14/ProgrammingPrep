string = "apple!mango+orange/grapes&banana"
list = []
word = ""
for i in string:
    if i.isalpha():
        word = word + i
    else:
        list.append(word)
        word = ""
if word!= "":
    list.append(word)
print(list)
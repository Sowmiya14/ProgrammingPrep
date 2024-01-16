def fruit_list(f):
    sp_chars = "!+//&"
    for char in sp_chars:
        f = f.replace(char, " ")
    return f.split()

input = "apple!mango+orange/grapes&banana"
output = fruit_list(input)
print(output)
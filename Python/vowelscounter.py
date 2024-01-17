get_string = input("Give me a String, I count a Vowel for U! :")
vowels = "aeiouAEIOU"
count = sum(get_string.count(vowel) for vowel in vowels)
print(count)
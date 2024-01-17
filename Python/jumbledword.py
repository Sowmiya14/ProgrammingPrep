def jumble_words(word, jumbled_word=""):
    if len(word) == 0:
        print(jumbled_word)
    else:
        for i in range(len(word)):
            jumble_words(word[:i] + word[i+1:], jumbled_word + word[i])

word2jumble = input("Type a Word U want to Jumble! :")
jumble_words(word2jumble)

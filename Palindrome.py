word = input("enter a word")
reversed_word = word[::1]
if word == reversed_word:
    print("YES ITS AN PALINDROMA")
else:
    print("NO ITS NOT AN PALINDROMA")
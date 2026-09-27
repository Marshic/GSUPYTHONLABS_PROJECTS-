# Donte' Brown   
# September 22nd 2026
# This program determines whether a given character is a vowel, consonant, digit, or punctuation.

# Lists
vowels = ['a','e','i','o','u']
digits = ['0','1','2','3','4','5','6','7','8','9']
punctuation = [',',';','.','?','!']

# Prompt the user
chara = input("Please enter a character: ")
chara = chara.lower()
# Conditions
if chara in vowels:
    print(f"The character '{chara}' is a vowel")
elif chara in digits:
    print(f"The character '{chara}' is a digit")
elif chara in punctuation:
    print(f"The character '{chara}' is a punctuation")
else:
    print(f"The character '{chara}' is a consonant")
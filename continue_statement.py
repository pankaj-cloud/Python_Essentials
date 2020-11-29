"""
Scenario
Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater! Write a program that uses:
•	a for loop;
•	the concept of conditional execution (if-elif-else)
•	the continue statement.

"""
# Prompt the user to enter a word
wordWithoutVovels = ""
userWord = input("Enter a word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVovels += letter

print(wordWithoutVovels)
# Complete the body of the for loop.


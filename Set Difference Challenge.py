# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

someString = "Water is my favorite beverage"

stringToSet = set(someString)
vowels = set("aeiou")

stringWithoutVowels = stringToSet.difference(vowels)
stringWithoutVowels = sorted(stringWithoutVowels)
print(stringWithoutVowels)

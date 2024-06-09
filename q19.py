import string

text = input("Enter a string: ")
clean_text = text.translate(str.maketrans('', '', string.punctuation))
print("The string without punctuation is:", clean_text)
text = input("Enter some text: ")
with open("output.txt", "w") as file:
    file.write(text)
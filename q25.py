with open('output.txt', 'r') as source_file:
    contents = source_file.read()

with open('destination.txt', 'w') as destination_file:
    destination_file.write(contents)

print("Contents copied from source.txt to destination.txt successfully.")

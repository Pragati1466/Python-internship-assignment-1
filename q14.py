lines = []

while True:
    line = input("Enter a line (leave empty to finish): ")
    if line == "":
        break  
    lines.append(line)  

print("You entered:")
for line in lines:
    print(line)

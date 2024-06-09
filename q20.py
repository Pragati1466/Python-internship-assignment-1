numbers = input("Enter a list of numbers separated by spaces: ").split()

total_sum = sum(int(num) for num in numbers)

print("The sum of the numbers is:", total_sum)

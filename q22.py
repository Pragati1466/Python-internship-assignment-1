numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]
minimum = min(numbers)
maximum = max(numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)

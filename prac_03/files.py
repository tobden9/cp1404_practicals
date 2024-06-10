FILENAME = "name_file.txt"
out_file = open(FILENAME, "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

out_file = open(FILENAME, "r")
name = out_file.read().strip()
print(f"Hi {name}!")
out_file.close()




# Open numbers.txt and read the first two numbers, then print their sum
FILENAME = "numbers.txt"
file_out = open(FILENAME, 'r')
number1 = int(file_out.readline())
number2 = int(file_out.readline())
result = number1 + number2
print(result)

# Print the total of all numbers in numbers.txt
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())
    print(total)

# 1
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# 3
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number_of_line = int(line)
    total += number_of_line
in_file.close()
print(total)

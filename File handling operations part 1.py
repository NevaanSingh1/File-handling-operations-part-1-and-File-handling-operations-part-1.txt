file = open("File handling Operations part 1.txt", "w")
file.write("Coding is basically the computer language used to develop apps, websites, and software.\n")
file.write("Without it, we’d have none of the most popular technology we’ve come to rely on such as Facebook, our smartphones, the browser.\n")
file.write("It all runs on code.\n")
file.write("To put it very simply, the code is what tells your computer what to do.\n")
file.write("To go a bit deeper, computers don’t understand words.\n")
file.write("They only understand the concepts of on and off.\n")
file.write("Binary code represents these on and off signals as the digits 1 and 0.\n")
file.write("In order to make binary code manageable, computer programming languages were formed.\n")
file.close()


file = open("File handling Operations part 1.txt", "r")
print("File is in read mode")
print(file.read())
file.close()

file = open("File handling Operations part 1.txt", "r")
first_line = file.readline()
print("First line:")
print(first_line.strip())
file.close()


file = open("File handling Operations part 1.txt", "r")
print("First 4 lines:")
for i in range(4):
    line = file.readline()
    if line:
        print(line.strip())
file.close()


file = open("File handling Operations part 1.txt", "r")
print("All lines one by one:")
for line in file:
    print(line.strip())
file.close()



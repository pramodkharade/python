# Ask user for Name
name = input("Whatr is your name?: ")
print(name)
#Ask user for age
age = input("How old are you ?: ")
print(int(age))

# Ask user for city
city = input("What city do you live in?: ")
#Ask user what they enjoy

love  = input("What do you love doing?: ")
# create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,love)
#print output to screen

print(output)

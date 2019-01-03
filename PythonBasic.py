name = input("what is your name: ")
age = int(input("How old are you: "))
year = str((2018 - age)+100)
print(name + " will be 100 years old in the year " + year)

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")

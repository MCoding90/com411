<<<<<<< HEAD
# Read in user data
=======
>>>>>>> 900d1a0e07d334b00faa5ec615243146d54c7fe4
print("What is your name?")
name = input()

print("What is your age?")
age = int(input())

print("What is your weight?")
weight = float(input())

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(f"{name} your bmi is {bmi}")
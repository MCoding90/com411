<<<<<<< HEAD
# Ask user for the type of adventure
print("What type of adventure should I have?")
adventure_type = input()

# Determine what message to display
if (adventure_type == "scary") or (adventure_type == "short"):
    print("Entering the dark forest!")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
=======
# Ask user for type of adventure
print("What type of adventure should I have?")

answer = input()

if (answer == "short") or (answer == "scary"):
    print("Entering dark forest!")

if (answer == "safe") or (answer == "long"):
    print("Taking the safe route!")

else:
    print("Not sure which route to take!")

>>>>>>> 900d1a0e07d334b00faa5ec615243146d54c7fe4

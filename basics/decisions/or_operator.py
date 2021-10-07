# Ask user for type of adventure
print("What type of adventure should I have?")

answer = input()

if (answer == "short") or (answer == "scary"):
    print("Entering dark forest!")

if (answer == "safe") or (answer == "long"):
    print("Taking the safe route!")

else:
    print("Not sure which route to take!")


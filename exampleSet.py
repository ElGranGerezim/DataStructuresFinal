collection = set()

# Add
def buy(rock):
    if not own(rock): # As long as it's not already there...
        collection.add(rock) # Buy it and add it to our collection.
        print(rock + " was purchased!") # And let the user know
    else: # If we do already own it...
        print("That type is already in our collection!") # Inform the user of error

# Remove
def sell(rock):
    if own(rock): # Only if it's there...
        collection.remove(rock) # Sell it, removing it from our collection
        print(rock + " was sold!") # Inform the user
    else: # If we don't have one...
        # Inform the user that fraud is illegal
        print(rock + " isn't in our collection! We can't sell what we don't own!")
        print("Directly to jail!") # Arrest them.

def display():
    print("Here is our collection:")
    for rock in collection:
        print("    * " + rock)
    input("Press enter to continue...")

# Helper function to remove duplicate code.
# Returns a boolean of if the desired value is
# in our set.
def own(rock):
    return rock in collection

# Output function to let us know the user if a specific
# rock is owned.
def checkFor(rock):
    if own(rock):
        print("Yes, we own a specimen of " + rock)
    else:
        print("No, we do not own a specimen of " + rock)

# Single input function to make it easier to validate input.
def prompt():
    while(True):
        choice = input("What type of rock?: ")
        if choice.isalpha():
            return choice
        else:
            print("Rock types can only contain letters!")

def main():
    choice = ""
    while choice != "1":
        print("    1. Exit program")
        print("    2. Purchase specimen.")
        print("    3. Sell Specimen.")
        print("    4. Check for specific specimen.")
        print("    5. View entire collection.")
        choice = input("What would you like to do?: ")
        
        if not choice.isnumeric():
            print("Please use only numbers")
        elif choice == "5":
            display()
        elif choice == "4":
            checkFor(prompt())
        elif choice == "3":
            sell(prompt())
        elif choice == "2":
            buy(prompt())
        elif choice == "1":
            print("Goodbye")
        else:
            print("Please select a valid choice.")

main()

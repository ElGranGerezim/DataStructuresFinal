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

# Show us your rocks!
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
def prompt(question):
    while(True):
        choice = input(question)
        if choice.isalpha():
            return choice
        else:
            print("Rock types can only contain letters!")

# Function to facilitate trade.
def trade(give, receive):
    # Write your code here!
    pass

def tradeAutoTests():
    # Store our current collection while we run tests. We'll put it back after
    oldCollect = collection

    # Give Rock not owned.
    print("Test: Give Not Owned")
    collection = {"rock"}
    trade("sediment", "igneous")
    print("Above should say we didn't execute the trade because we didn't have the rock to give")
    display()
    print("Above should just say rock")
    
    # Take Rock already Owned.
    print("Test: Take Already Owned")
    collection = {"pebble"}
    trade("sediment", "pebble")
    print("Above should say we didn't execute the trade because we already have the receive rock")
    display()
    print("Above should say just pebble")

    # Successful trade
    print("Test: TSuccessful trade")
    collection = {"rock"}
    trade("rock", "igneous")
    print("Above should say we didn't execute the trade because we already have the receive rock")
    display()
    print("Above should say just igneous")

    # Put it back.
    collection = oldCollect
    print("All Tests Done!")

def main():
    choice = ""
    while choice != "1":
        print("    1. Exit program")
        print("    2. Purchase specimen.")
        print("    3. Sell Specimen.")
        print("    4. Check for specific specimen.")
        print("    5. Trade rocks!")
        print("    6. View entire collection.")
        print("    7. Run Trade Tests.")
        choice = input("What would you like to do?: ")
        
        if not choice.isnumeric():
            print("Please use only numbers")
        elif choice == "7":
            tradeAutoTests()
        elif choice == "6":
            display()
        elif choice == "5":
            give = prompt("What rock are you willing to trade away?: ")
            receive = prompt("What rock do you want to receive?: ")
            trade(give, receive)
        elif choice == "4":
            checkFor(prompt("What rock do you want to check for?: "))
        elif choice == "3":
            sell(prompt("What rock do you want to sell?: "))
        elif choice == "2":
            buy(prompt("What rock do you want to buy?: "))
        elif choice == "1":
            print("Goodbye")
        else:
            print("Please select a valid choice.")

main()

choice = "Nothing at all"
queue = []
while(choice != "4"):
    print("Select an option:")
    print(" 1. Get name of next customer.")
    print(" 2. Add name of new customer.")
    print(" 3. View entire queue.")
    print(" 4. Exit Program.")
    choice = input(">: ")
    if (choice not in ["1", "2", "3"]):
        print("Invalid choice, try again.")
    elif(choice == "1"):
        if(len(queue) == 0):
           print("Queue is empty")
        else:
            print(queue.pop(0), "is the next in line.")
    elif(choice == "2"):
        print("Put the name of the customer to add.")
        name = input(">: ")
        queue.append(name)
    elif(choice == "3"):
        print("Here is the current queue:")
        print(queue)
print("Thank you for using our program!")
print("Goodbye.")
# Here's our queue.
GradOrder = ["Greg Greg", "Mr. Bob", "Janet J Jewels", "A Literal Tree", "Mrs Fluffypaws the Cat", "Mark Down", "P. Y. Thon", "Mr Pun", "Gregg Greg", "Another Name", "If you're seeing this it's too late", "Boneless Chicken", "Why are we still here?", "Just to suffer?"]

# Gets the next count number of items in our queue
def getNext(count):
    # Write your code here!
    pass

def tests():
    #Test 1
    print(getNext(2)) # Greg Greg, Mr. Bob

    #Test 2
    print(getNext(3)) # Janet J Jewels, A Literal Tree, Mrs Fluffypaws

    #Test 3
    print(getNext(4)) # Mark Down, P.Y.Thon, Mr Pun, Gregg Greg

#Start our tests.
tests()
class BST:
    class Node:
        def __init__(self, data): # On creation of new Node Object
            self.data = data
            self.left = None
            self.right = None

    def __init__(self): # On creation of new BST object
        # Set our root to None
        self.root = None

    def insert(self, data): # When trying to add data to our tree
        if self.root is None: # If we have no root...
            self.root = BST.Node(data) # Make a new node with the data and set it as our root.
        else: # Otherwise...
            # Start at the root and look for where to put it.
            self._insert(data, self.root)

    def _insert(self, data, node): # When trying to add new data to a not empty tree...
        if data < node.data: # If the data is smaller than ours...
            # The data belongs on the left side.
            if node.left is None: # If there's nothing to our left...
                # We found an empty spot
                node.left = BST.Node(data) # Make a new Node with our data and put it on our left.
            else: # Otherwise...
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data: # If the data is bigger than ours...
            # The data belongs on the right side.
            if node.right is None: # If there's nothing to our right...
                # We found an empty spot
                # Make a new node with the data and put it on our right.
                node.right = BST.Node(data)
            else: # Otherwise... 
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
        else:
            # If the data isn't greater or less than our data, it's the same
            # and we should just return to avoid duplicates.
            return

    def __contains__(self, data): # When trying to see if something is in our tree
        return self._contains(data, self.root)  # Start at the root and recursively look.

    def _contains(self, data, node): # Recursive function for searching the tree.
        if data == node.data: # If the data matches ours...
            return True # We found it, it's here.
        else: # Otherwise...
            if node.left is not None and self._contains(data, node.left):
                # If there's something to our left, search down that branch,
                # And if they find it anywhere down there, we'll pass along
                # back up that it's been found.
                return True
            elif node.right is not None and self._contains(data, node.right):
                # Same for the right.
                return True
            else: # Otherwise...
                # It's not on our left or right, so pass back up to keep searching.
                # If we get here on the root, it's not in our tree, so pass back
                # false.
                return False

    def __iter__(self): # To get each element from the tree one at a time, 
        # Like in a foreach loop.
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node): # To iterate through lowest to biggest.
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self): # Get each element from the tree largest to smallest.
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node): # Recursive function to get each element one
        # At a time largest to smallest.
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self): # Figure out how tall we are, useful for balancing.
        if self.root is None: # If we have no root, we're nonexistant. 0.
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node): # Recursive function to figure out how tall we are.
        # Base case. The height of a tree with only the root is 1.
        if node.left is None and node.right is None:
            return 1
        else:
            # Assume at the beginning both sides are nonexistnat, even though we know
            # at least one is because we got this far, we dont know which.
            left = 0
            right = 0

            # Validation to make sure we don't try to get the height of a none object
            if node.left is not None:
                left = self._get_height(node.left)
            if node.right is not None:
                right = self._get_height(node.right)

            # Kickback result.
            return 1 + max(left, right)
    
    def display(self):
        for item in self:
            print("    " + item)
    
    def has(self, item):
        return item in self

def prompt(question):
    return input(question)

def promptChoice():
    choice = "a"
    while(True):
        choice = input("What will you choose?")
        if choice.isnumeric():
            if int(choice) < 1 or int(choice) > 4:
                print("Invalid choice, out of range.")
            else:
                return choice
        else:
            print("invalid choice, not a number")

def main():
    tree = BST()
    choice = 0
    while(int(choice) != 4):
        print("Employee Registry Program")
        print("Main Menu:")
        print("    1. Add name to registry.")
        print("    2. Search registry for specific name.")
        print("    3. List Entire Registry.")
        print("    4. Exit")
        choice = int(promptChoice())
        if choice == 1:
            tree.insert(prompt("What name would you like to add?: "))
        if choice == 2:
            if tree.has(prompt("What are we searching for?")):
                print("Yes, that employee is on the registry.")
            else:
                prompt("No, they are not in the registry.")
        if choice == 3:
            print("Listing employees:")
            tree.display()
        if choice == 4:
            print("Goodbye.")
    
main()
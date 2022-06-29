# Queues
## Table of Contents
* Introduction
* Enqueue
* Dequeue
* Example
* Practice

## Introduction
The normal definition of a queue is ```a line or sequence of people or vehicles awaiting their turn to be attended to or to proceed.```

The data structure definition is almost exactly the same, except we replace *people or vehicles* with whatever type our data is! 

Our queue can be represented visually like this
<Insert a picture of a queue>

In order to be a queue a data structure must follow 2 rules:
1. Items can only be added to the back, an action called **Enqueue**
2. Items can only be removed from the front, an action called **Dequeue**

Python does not have a traditional queue that strictly follows these 2 rules, but we can use a list in python (Created using `<variable name> = []`) since lists have member functions that perform these 2 operations.
## Enqueue
Can you imagine standing in line at your favorite restaurant and you suddenly realize everyone coming in after you has been getting added to the front of the line instead of the back? That's no good!

In order for a queue to function properly, items can **only be added to the back**, called an `enqueue`-ing an item. Lets assume we have a queue with 2 items:
```python
# Remember in python we need to use lists as queues
myQueue = [2, 3]
```

If we wanted to add an item to it, we could use a lists `append()` function.
```python
myQueue = [2, 3]
myQueue.append(4)
print(myQueue) # 2, 3, 4
```
This adds the new number, 4, to the end of the queue, without changing the order of any of the other members! This makes this operation very efficient in python, O(1) to be exact. 
## Dequeue
But lets say we wanted to remove an item from our queue. Imagine the restaurant scenario from before. If you were at the front of the line, you'd probably be mad if you noticed that people at the end were getting their orders taken before you.

This is why items can only be removed from the **front** of the queue, called `Dequeue`-ing an item.
Using our queue from before, we can remove an item using python's `pop()` function, specifying `pop(0)` to make sure it comes from the front.
```python
myQueue = [2, 3, 4]
first = myQueue.pop(0)
print(first) # 2
print(myQueue) # 3, 4
```
It is important to note that when we dequeue, **we remove the item from the queue**. This moves every item behind it up one, getting them closer to the front and their turn to be dequeue'd. Because of this, dequeue-ing is a slightly inefficient operation, O(n) where n is the number of items in the queue. This is only true for our list-queues in python however. In other languages with specifically built queues, this operation could be O(1).
## Example
For our example, we're going to write a simple queue manager to help our restaurant staff keep track of who's turn it is to order next. Here's what we need it to do:
* Employees need to be able to add people's names to the back of the queue as they come in.
* Employees need to be able to get the name of the next person in line as they're able to take new orders.
* For testing purposes, we'll want to have a way to see the entire queue as-is without moving anything.
* Our computer we run this on also does our end of day profit calculations, so we need to be able to close the program once we close so we can use the computer.

```python
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
```
Remember to use `pop(0)` instead of just `pop()`, as the default pulls items from the end of the list, not the front, which isn't very queue-like!
## Practice Problem
We have an embarrassing situation on our hands! It's graduation, and we're about ready to start calling graduates up to get their diplomas. But we forgot to print them! The president is stalling, but we've gotta move fast!

Luckily we already had a big PDF with all of their diplomas in order, but since it's all one file we're relying on one printer. It's pretty fast though, and depending on various factors can print 2, 3, or 4 diplomas at a time.

Using this starting code [here](./practiceQueues.py), can you finish writing the code that will pull the next "x" names from the queue of diplomas and print them on the ~~screen~~ teleprompter so we can tell the president whose names to call next?

Here's a few examples of the first few names so you can be sure your code works:

The first 2 names | The next 3 names | The next 4 names
-------- | -------- | --------
Greg Greg | Janet J. Jewels | Mark Down
Mr. Bob | A literal Tree (we don't know how but he's on the list) | P. Y. Thon
/ | Mrs. Fluffypaws the cat (she attended every lecture) | Mr Pun
/ | / | Gregg Greg (no relation to the first.)

You can compare your code to the [solution](./solutionQueues.py) when you're done.
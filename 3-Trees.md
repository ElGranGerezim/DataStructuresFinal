# Trees
* Introduction
* Binary Search Tree
* Tree Balance
* Example
* Problem to Solve

## Introduction
All other data structures we've discussed have had some form of linear progression, each item links only to two other items in the list, the one before and the one after. But what if we changed that, instead of only going forward and backward, we added a third direction? In order to not create circles, which could get us stuck in infinite loops, we'd need to have only one way to go back, so we'll add a second way to go forward. Now every item, called a `node`, has one parent node and can have up to two children nodes, which could look like this:
![Anatomy of Binary Tree](./images/Anatomy%20of%20Tree.png)

We assume that up is always the parent and left/right are always down in addition to their other directions, and thus children. A node with no parent is called the **root**, and there's only one in every tree. Any node without children is called a **leaf**, and they constitute the end of that particular branch of the tree. Now, what is our rule for *which* node to store our data in?

## Binary Search Tree
Moving from one node to the next is called `Traversing the tree`. Traversing is a `Recursive`  operation, meaning we do the same small task over and over in order to complete some larger task. In this case, search the tree by going down it. In this case, we can start at the root, compare its value to what we're searching for, and go either left or right depending on the rules we know the tree follows.
 A `Binary Search Tree (BST)`, a tree designed for quick searching, has 2 simple rules. Everything on the left of a node is **smaller** than the item in the parent nodes, and everything on the right is **greater** than the data in the parent node. For example, let's have a tree that has one node, the root, with the number 7:
![Tree but only one element](./Images/Very%20Small%20Tree.png)

And now we want to add the number 5. Since it's smaller than 7, it goes to the left:
![Tree but only 2 element](./Images/Small%20Tree.png)

Insert the number 8, which goes on the right, and we have a nice looking, even tree. But what if we wanted to add the number 6? It's smaller than 7, but larger than 5, so our tree now looks like this:
![Tree but 4 element](./images/Less%20Small%20Tree.png)

Inserting into a tree is a recursive operation, since we need to keep making comparisons until we find an open spot, somewhere where the node we're on doesn't have any children in the direction we're going. 

If we wanted to *find* the number 5 in a normal list, we'd need to go over every item and see if it's there, an O(n) operation. But since we cut down on half the possible options (greater or less than) with every node we pass, searching in a tree is an O(log n) operation.

This, however, is only true if the tree is `Balanced`,

## Balance
A BST is **Balanced** if, and only if, there is no noticeable difference in distance between the root and any of the leaves. For example, imagine a tree that looks like this:
![Unbalanced tree, 1 element to left but 5 on the right](./Images/Unbalanced%20Tree.png)

Finding anything in this tree would be insane. We could balance it like this:
![Balanced tree, equal number on every side](./Images/Balanced%20Tree.png)

Now it is much easier to search this BST. There are several different algorithms to balance a tree, and they are all very complicated. Some examples include Red/Black trees and AVL (Adelson-Velskii and Landis) trees. There really is no simple way to balance a tree, so using established and proven methods/algorithms is the best option when working with them.

## Example
There is no built in tree type for Python, though there are several libraries that have them. We built a simple one for this example. Here are the public functions it has:
Function | Use
------ | ------
`<variable> = BST()` | Creates a new BST
`insert(item)`   | Adds items to the BST
`has(item)` | Boolean expression, returns if item is in tree or not.
`display()` | Lists every item in the tree in ascending order. 

Our friend Wanda in HR needs some help. She has sign up sheet for a company party that she's had everyone who plans on coming sign, but they're out of order and it's hard for her to figure out if specific people are going or not. We built her [this](./exampleTree.py) Binary Search Tree program to help her organize and search through the names. You can add as many names as you want, in any order that you want, but they'll display alphabetically and is instantly searchable.

## Practice Problem
Using a more advanced version of our BST and Node classes you can find [here](./PracticeTree.py),
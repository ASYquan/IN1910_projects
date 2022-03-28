### IN1910 – Programming with Scientific Applications 
In this repo, i have imported all my previous submissions or assignments / projects for the course: IN1910 (with a pass of course).
Each of the branches represents one project, where one projects tests our knowledge of different concepts from the curriculum.
Ranging from application of Python / Numpy in pendulum-simulation to implementation of Linked lists (singly and doubly) and arrays with c++. 

# H21_project2_asquan
-   repo url: https://github.uio.no/IN1910/H21_project2_asquan

# Author
Project 2 for asquan (asquan@mail.uio.no)
# Practical information
Compile-commands:
- c++ array_list.cpp -o array_list -std=c++11 -g      
- c++ Circular_linked_list.cpp -o circular_linked_list -std=c++11 -g      
- c++ linked_list.cpp -o linked_list -std=c++11 -g 

Run-commands:
- ./array_list
- ./circular_linked_list
- ./linked_list

All exercises were able to run and compile on local machine, and ifi-machines.   

The "-g" is not required, but i like to include it in case of debugging. 

# Part 1 - ArrayList
- note: I made a public method called "cap" which returns the capacity. I know it is not apart of the project, but i used it in one of the tests and decided to keep it for easier access. 

# Part 3 - Big-oh notation a)
- "Get element i by index": 

**ArrayList:**
When getting a value by indexing in an arraylist, there is no iteration throguh a list of size N. 
The only thing happening is an if-statement which is constant. 
If the if-statement passes, the function returns data at index: i
.This is constant, therefore it is O(1).

**LinkedList:** for a LinkedList it will take longer time. How indexing for a doubly linked list works
is that the head of the linked list will iterate through the indexed list and another 
variable will count the amount of times the head has traveresed. It will stop when it has reached
the inputted index, and return the node value. Therefore, it is O(N).

- "Insert at front/ append/ insert in middle of the list":
These methods are in one category because they work very similar to each other, for each
respective class. 

**ArrayList**:
When inserting at front for or inserting in the middle of an arary list, all elements from the indexed value to 
the end of the list will be pushed to the right, such that there are two duplicates of the value of the index - 1.
Then the inputted value will be inserted where the original index - 1 is. The method will therefore, be O(N), 
in some cases smaller than N, depending on where in the list the value will be inserted.
This also is the case for inserting in the middle of the list, for an arraylist. 

Appending works a little different for an array list. It will always add 
a value to the last index the list, which would be equal to the size of the array. No iteration is needed (unless the index is larger than size, but that is apart of the resize-method)
, and therefore is O(1). 

**LinkedList**:
Pushing to the front and appending will be O(1), because it will simply replace the value of the
head and tail of the doubly linked list to the input-value. 
Inserting in the middle of a doubly linked list will also be O(1). The input will be the index
and the value. The node for the index +1 will be set to the node after index - 1, 
then the node after index - 1, will be replaced with the new node. 

-   "Remove element from front/back/middle": 
**ArrayList**: 
Worst case for these methods from the arraylist class will be O(N), because it works very similarly
to insert. The difference being that it pushes all elements to the left and reduces the size by one. 
Again, it may also be smaller than O(N), depending on what the input-index is. 

**Linked list:**
The removal of front and back will be O(1).
If removal of element from the front were being called, then the current head would be deleted, 
and replaced with a nullpointer, and the new head would be the node after . The same for removal of the back, except only for the tail.
The new tail would be the previous node, and the current tail would become a nullpointer.

When it comes to the removal of an element in the middle, it would be at worst case
also O(N), since it will iterate through the list and stop depending on the index.
Once stopped, it will delete the node it stopped at, and replace it with the next node. 

- "print:"

**ArrayList:** 
Printing requires the iteration of the entire input list, in addition printing out
the brackets and commas. As such it will be O(N).

**Linked list:** The head of the linked list will iterate and print every node through the entire input-list.
Thus, resulting also in O(N).

# Part 3 - expressions b):
**ArrayList:**

- Get-method: 0.005 * O(1)
- Insert-method: 0.001 * O(N)

**LinkedList::**

- Get-method: 0.001 * O(N)
- Insert-method: 0.1 * O(1) 

# Part 4 - pop quiz

By inserting n = 67, and k = 7 into the function i will receive position 61. 
Therefore, i would bet on position 61 to be the winning position. 








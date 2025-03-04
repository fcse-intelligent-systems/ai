# Auditory exercise 2 - Introduction to Python

## Problem 1 - Swap elements in a list of tuples

Write a function that, given a list of tuples in the form [('a', 1), ('b', 2), ('c', 3)] will swap the elements in the tuples so that the element at position 0 will be the element at position 1 and vice versa. Use list comprehension.
Example input:
[('a', 1), ('b', 2), ('c', 3)]

Example output:
[(1, 'a'), (2, 'b'), (3, 'c')]


## Problem 2 - Agent movements

Define a class for an Agent that stores its position (x and y coordinates) in space. Define a method that indicates the movement of the agent in space. Then define agents that implement a specific movement (left, right, up, down). Perform 5 movements for each of the agents and print the position of the agent at each step.

## Problem 3 - Nested list comprehension
Using list comprehension, given a matrix of numbers, change each element so that it is multiplied by 2. Each element of the matrix is ​​read from the keyboard by first reading N and M (number of rows and columns) and then in each row the elements are read, separated by a space.

Example input:
4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Output:
[[2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]


## Problem 4 - Nested list comprehension with checks
Using list comprehension, given a matrix composed of numbers, change each element so that if it belongs to the upper half (the row index is between 0 and n/2) it should be multiplied by 2 and if it belongs to the lower half it should be multiplied by 3. Each element of the matrix is ​​read from the keyboard so that first N and M (number of rows and columns) are read and then the elements separated by a space are read in each row.

Example input:
4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Output:
[[2, 4, 6, 8], [2, 4, 6, 8], [3, 6, 9, 12], [3, 6, 9, 12]]



## Additional resources:
https://www.datacamp.com/community/tutorials/python-list-comprehension
https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/

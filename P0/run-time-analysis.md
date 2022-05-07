# Run Time Analysis for the P0 Exercise: Investigating Texts and Calls

## Task0.py

Each of the open functions to open `texts.csv` and `calls.csv` have a runtime of O(1) each, as the computation required to open these files don't change. The print statements also have a runtime of O(1) for the same reasons. 

Since we know which index to retrieve the element in the list from, we don't need to scan the entire list. Hence, the time it takes to retrieve an element in an array is also O(1). Hence, retrieving an element in another element also has a runtime of O(1 * 1) = O(1).

Hence, Task0.py has a constant runtime at O(1).

## Task1.py

For the following tasks, I'll ignore the file opening functions, as these all have constant runtime.

Concatenating the two lists for texts and calls have a constant runtime because it doesn't change the runtime the longer the lists.

As for extracting the first and second elements of a list of lists, each will have a runtime of O(n) as it requires scanning through each text and call record linearly twice, i.e. O(2n) = O(n).

Adding the `records_from` and `records_to` lists has a constant runtime, as with adding `texts` and `calls`. However, calling the `set()` function, which deduplicates elements in the list -> set, has a runtime of O(n), since the set function has to scan through the list at least once.

The `len()` function has a constant runtime O(1), since it only checks for the length of the set once regardless of size.

And lastly, the print function has constant runtime.

Hence, the total runtime for this function is linear, i.e. O(n).

## Task2.py

Let's analyze the task into different tasks:

### 1. Variable declaration, assignment, and retrieval

This includes the `durations = {}` dict declaration, assigning a caller and callee in the first and second entries in a call record, assigning keys and values into the `durations` dict, and retrieving the answer for the print statement.

All of these have constant runtime as it only takes a single input and output to execute.

### 2. For loop

Since we're going through the length of the `calls` record, this has a runtime of O(n).

### 3. If else statements

For each of the if else statements, both are checking if a key exists in the dictionary, which are both constant runtime tasks.

### 4. Max function

The `max()` function goes through all the key/value pairs once. Assuming the worst case where there were no duplicate callers and callees, this has a runtime of O(n), where n is the maximum number of callers and callees. 

An average case might have a runtime of O(m), where m < n due to duplicates.

### Conclusion

All in all, the worst-case runtime for this task is O(1 + n + 1 + n) = O(2n) = O(n).

## Task3.py

Since we've previously analyzed similar functions in the past, let me outline the list of tasks for each part for easier analysis:

Part A has:
- list comprehension as a for loop -> O(n)
- variable assignments -> O(1)
- a for loop where: -> O(n)
- 1. if else with a for loop but constant length -> O(1)
- 2. Hence the for loop has a total runtime of O(n)
- conversion from set to list -> O(1)
- a sort function -> O(n log n)
- a print function with a for loop -> O(n)

Hence the total runtime of this function is O(n + n + n log n + n) = O(3n + n log n) = O(n log n), since n log n diverges to infinity faster than n.

Part B has:
- a `len()` function -> O(1)
- a for loop with an if else check -> O(n)
- an arithmetic operator and a print function with prettify for the number -> O(1)

Part B has a total runtime of O(n).

Hence, this task has a total runtime of O(n log n + n) = O(n log n).

## Task4.py

Task 4 has these tasks:
- Four tasks that have a for loop with a set -> O(4 * (n + n)) = O(8n) = O(n)
- A `|` function which denotes a set union. It goes through the set at least once to find all elements at least in one of the sets -> O(n)
- A `&` function which denotes a set intersection. It goes through the set at least once to find elements common in both sets. -> O(n)
- A `-` functionwith denotes a set difference between A and B. It goes through the sets to find elements in set A but not set B. -> O(n)
- a `sort()` function with a list conversion -> O(n log n + 1) = O(n log n)
- a for loop to print a number -> O(n)

Hence, this task has a total runtime of O(5n + n log n) = O(n log n).

# Lab3_202_Spring26# Lab 3: Lists
**CS 202 - Spring 2026**  
**Professor Duran**  
**Due: Friday, April 17, 2026**

This is a two-day lab on immutable list data structures in Python. In this course, we are practicing a functional style whenever possible. For immutable data structures, this means your functions should return new structures rather than changing existing ones.

## Day 1 - Wednesday, April 15, 2026
### `lab3_1.py`: Array List

For Day 1, you will work with an array-backed list.

Before starting your tasks, read the given functions carefully. Do they make sense? Make sure you understand how the `ArrayList` stores data, how `next` is used, and why these functions return new structures instead of modifying the original one.

Your tasks:
- implement `resize(arr, factor=2)`
- modify `insert(arr, n)` so that it automatically calls `resize` when the array is full

### What to do
The `ArrayList` keeps track of:
- `size`: total capacity
- `array`: the underlying list
- `next`: the next open position

You should implement `resize` so that it creates a larger array, copies the old values into it, and returns a new `ArrayList`.

Then, update `insert` so that when the array is full, it first resizes the list and then inserts the new value.

---

## Day 2 - Friday, April 17, 2026
### `lab3_2.py`: Linked List

For Day 2, you will work with an immutable linked list using a frozen recursive `Node`.

Before starting your task, read the given functions carefully. Do they make sense? Pay attention to how recursion is used and how each function returns a new linked list instead of modifying an old one.

Your task:
- implement `insert(node, index, value)`

### What to do
Since the linked list nodes are immutable, you cannot change an existing node. Instead, your function should use recursion to build and return a new linked list with the inserted value.

Your function should:
- insert the value at the correct index
- return a new linked list
- leave the original list unchanged
- raise `IndexError` if the index is invalid

---

## Testing
Make sure the following tests pass:
- `test_1.py`
- `test_2.py`

---

## Sign-Off
Once your tests pass:
- get signed out by the instructor or TA
- turn in your sign-off sheet at the end of lab on Friday
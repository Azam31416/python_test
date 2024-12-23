# python_test
This is a small list of questions to test your python skills.

## Challenge 1: Basic Syntax and Variables

Level: Beginner

Task: Write a Python function sum_of_evens(nums) that takes a list of integers and returns the sum of all even numbers in the list. If there are no even numbers, return 0.

Example input:

```python
sum_of_evens([1, 2, 3, 4, 5, 6])  # Output should be 12 (2 + 4 + 6)
sum_of_evens([1, 3, 5, 7])         # Output should be 0``
```

## Challenge 2: Loops and Conditional Statements

Level: Intermediate

Task: Create a function fizz_buzz(n) that returns a list of numbers from 1 to n. For multiples of 3, the list should have the string "Fizz", for multiples of 5, the string "Buzz", and for numbers that are multiples of both, the string "FizzBuzz". Otherwise, the number itself should be in the list.

Example input:

```python
fizz_buzz(15)  
# Output should be: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
```

## Challenge 3: Functions and Data Structures

Level: Intermediate

Task: Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key exists in both dictionaries, the value from dict2 should be used. If a key only exists in one of the dictionaries, it should be included in the result as is.

Example input:

```python
merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# Output should be: {'a': 1, 'b': 3, 'c': 4}
```

## Challenge 4: Recursion

Level: Advanced

Task: Write a recursive function factorial(n) that returns the factorial of a number n. The factorial of a number n is defined as n! = n * (n-1) * (n-2) * ... * 1.

Example input:

```python
factorial(5)  # Output should be 120
factorial(0)  # Output should be 1
```

## Challenge 5: Object-Oriented Programming

Level: Advanced

Task: Define a Python class Rectangle with the following attributes:

- width (width of the rectangle)
- height (height of the rectangle)

The class should have the following methods:

- area(): Returns the area of the rectangle.
- perimeter(): Returns the perimeter of the rectangle.

Example usage:

```python
rect = Rectangle(4, 5)
print(rect.area())       # Output should be 20
print(rect.perimeter())  # Output should be 18
```

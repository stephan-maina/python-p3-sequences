# Sequences in Python

This repository explores the fundamental concepts of sequences in Python, covering data types like lists, tuples, ranges, and strings. It also includes a function to print the Fibonacci sequence.

# Table of Contents

Key Concepts
Operations on Sequences
Lists
Tuples
Ranges
Strings
Fibonacci Sequence Example
Running the Code
Contributing
License

# Key Concepts

Sequence: A data structure that stores elements in a specific order.
Index: The position of an element in a sequence, starting from 0.
Iterable: A data structure that can be iterated (looped) through.
Slice: A group of neighboring elements in a sequence.
Mutable: An object that can be changed.
Immutable: An object that cannot be changed.
List: A mutable data type that can store various data types.
Tuple: An immutable data type that can store various data types.
Range: A data type storing integers in a fixed pattern.
String: An immutable data type for storing sequences of characters.

# Operations on Sequences

Sequences in Python support a variety of operations to manipulate and work with their elements. These operations include:

Checking if an element is in a sequence using x in s.
Concatenating sequences with s + s2.
Repeating a sequence with s \* n.
Accessing elements by index using s[i].
Slicing sequences with s[i:j] and s[i:j:k].
Finding the length of a sequence with len(s).
Finding minimum and maximum values using min(s) and max(s).
Finding the index of an element with s.index(x).
Counting occurrences of an element with s.count(x).

# Lists

Lists are one of the most commonly used data structures in Python. They are mutable, versatile, and can store elements of various data types. Some common list operations include sorting, adding, and removing elements.

# Tuples

Tuples are immutable sequences, meaning their elements cannot be changed after creation. They are useful for situations where you want to ensure the integrity of the data.

# Ranges

Ranges are simple sequences primarily used in for loops to iterate over integers in a specific pattern. They are memory-efficient and are especially useful for generating sequences of numbers.

# Strings

Strings are sequences of characters and are also immutable. They provide various methods for operations like changing case, formatting, and searching.

# Fibonacci Sequence Example

The provided code includes a function called print_fibonacci(length) that demonstrates the concept of sequences. It prints the Fibonacci sequence of a given length.

python
Copy code
print_fibonacci(9)

# => [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Running the Code

To execute and test the code, you can use the Python shell to run code interactively. Additionally, the code includes unit tests written with pytest. You can run the tests using the following command:

bash
Copy code
pytest -x
This will check if the code behaves as expected and ensure that the Fibonacci sequence function works correctly.

# Contributing

Contributions to this repository are welcome. If you'd like to contribute, please feel free to open issues or pull requests on the GitHub repository.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [Common Sequence Operations][common sequence operations]
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Range Docs](https://docs.python.org/3/library/stdtypes.html#ranges)
- [String Methods][string methods]

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[string methods]: https://www.w3schools.com/python/python_ref_string.asp
[fibonacci sequence]: https://www.mathsisfun.com/numbers/fibonacci-sequence.html

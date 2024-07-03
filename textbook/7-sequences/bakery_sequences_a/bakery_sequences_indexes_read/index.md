---
waltz:
  title: bakery_sequences_indexes_read
  display title: 7A1) Lists and Indexes Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Lists and Indexes
    youtube:
      Bart: 3iUPQl9XIZU
      Amy: GdJt-L55cLU
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0600 PM
  files:
    path: bakery_sequences_indexes_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Lists and Indexes

```python list-elements
values = [10, 10, 20,  1,  5]
#indexes:  0,  1,  2,  3,  4
#   also: -5, -4, -3, -2, -1

print("First is", values[0])
print("Third is", values[2])
print("Last is", values[-1])
```

So far, we have iterated through a list using the for-each syntax to get each value of the list.
We have also used indexing to access specific values in a list by their individual postiion.
In many languages, indexes are used to iterate through all the values of a list.
The index of the list are the integers, starting from 0 and counting up, that uniquely identify each element.
The code shown here demonstrates how we can access indexes using positive and negative integers.
In this chapter, we'll learn how we can use indexes to iterate through the list, modify elements of the list,
and do more complex manipulations to the list.

## Value Iteration vs. Index Iteration

```python index-value-iteration
names = ["Adam", "Betty", "Clarice"]
    
# Value style
for name in names:
    print(name)

# Index style
for i in range(len(names)):
    print(names[i])
```

The top code shown here is the usual way to process a list in Python, where we iterate through each value.
However, you can also iterate by using a combination of the range and len functions, as shown here.
Both the Value style and the Index style shown will print the same result.
The Index style is a little more complicated since we need to ues the other two helper functions, so let's take a closer look at them.

## Len Function

```python len-function
grocery_list = ['Bread', 'Ham', 'Eggs']

# len function
number_of_groceries = len(grocery_list)
print("Length of list is", number_of_groceries)
print("The length of Bread is", len(grocery_list[0]))
```

The `len` function is relatively straightforward; the function consumes an iterable like
a list and produces an integer representing the length of the list.
In other words, the number of elements in the list.
The `len` function also works on strings, producing the number of characters in the string.
In fact, the `len` function does all the work of the basic Count pattern, although
sometimes we want to extend that pattern in ways that you cannot with the `len` function.

## Range Function

```python range-function
numbers = range(3)
for number in numbers:
    print("Number: ", number)
  
# Range with Map pattern
chapters = []
for number in range(10):
    chapters.append("Chapter " + str(number))
print(chapters)
```

The `range` function consumes an integer and produces a list of integers from 0 up until that number.
One use case is to iterate an explicit number of times, as in the first example, where we iterate exactly three times.
A distinct use case for this is to create lists of numbers via the Map pattern, as shown in the second half of this code.
In that example, we iterate 10 times in order to produce a list of 10 numbers, starting from `"Chapter 0"` to `"Chapter 9"`.

## Enumerate Function

```python enumerate-function
grocery_list = ['Bread', 'Ham', 'Eggs']

for index, grocery in enumerate(grocery_list):
    print("At index", index, "there is", grocery)
```

As an alternative to combining `range` and `len`, we can also use the `enumerate` function.
The `enumerate` function allows us to access both the values and indexes at the same time.
While convenient, we do have a new, unusual feature to learn about.
Instead of one iteration variable, we now have two iteration variables to worry about.
This only works because the `enumerate` function returns a list of pairs of things.

## Modifying Elements of a List with Indexes

```python modifying-list-elements
names = ["Adam", "Betty", "Clarice"]

names[0] = "Alphonse"
names[-1] = "Carol"
print(names)

# 1) But indexing out of bounds will NOT work!
#names[3] = "David"
# 2) Nor will modifying a string's characters
#a_name = "Erin"
#a_name[0] = "B"
```

So far, we have focused on only one way to modify a list, using the `append` and `pop` methods to
add and remove elements from the end of the list.
But we can actually also update the elements of a list using assignment statements, similar to how we can
update fields of dataclasses.
As the example code illustrates, we just put the indexed element on the left hand side of the assignment statement,
and the appropriate indexes value will be changed.
Note also that the first commented-out block of code demonstrates that we cannot use this to add new elements to the list.
If you attempt to update an index outside of the size of the list, you'll get an IndexError.
Note also the last example shown in the commented out code, where we try to first character of a string.
That does not work, and will cause an error, because strings are immutable.

## Modifying Multiple Elements with Iteration

```python modifying-for-loop
words = ["Dog", "Cat", "Mouse"]

for index, word in enumerate(words):
    words[index] = word + "s"

print(words)
```

Up until now, our `for` loops have always created new lists instead of directly modifying old lists.
This is because modifying values makes it difficult to keep track of changes.
But sometimes, we will want to modify every element of our original list.
By combining the `enumerate` function and the index assignment syntax we just learned, we can do so.
This code shown here will add the letter `s` to the end of each word in the original list, and then assign
to that index in the list.

## Swapping Elements

```python swap-example
words = ["Dog", "Cat", "Mouse"]
print(word)

words[0], words[1] = [words[1], words[0]]
print(words)
```

Sometimes, you will need to swap the position of two elements in a list.
In order to do so, we need to assign directly to multiple indices at once.
This is similar to how we can assign to two iteration variables at once when we use the `enumerate` function.
Python always handles the right-hand side of the assignment statement first, so the original values are obtained and put into a new list.
Then, those values are assigned one at a time to the two entries on the left-hand side, which are the first and second indexes of the list.
By assigning to the index, we update the value stored at that location.

## Indexes vs. Values

1. Indexes allow more flexibility
2. Values require fewer operations
3. Values are less complex

So when do you use indexes and when do you use values?
Usually, you should stick to value style unless you have an explicit reason to use indexes.
Indexes allow more flexibility and are necessary for certain kinds of specialized algorithms.
However, they require more operations and are more complex to reason about.
When you manipulate indexes, you run the risks of mutable danger, which we discussed a few chapters ago.
In general, we prefer to read data and create new variables, instead of modifying existing values.
That way, we do not have to keep track of whether data has changed later in the program.

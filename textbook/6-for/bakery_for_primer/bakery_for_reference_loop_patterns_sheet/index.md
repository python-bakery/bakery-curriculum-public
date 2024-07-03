---
waltz:
  title: bakery_for_reference_loop_patterns_sheet
  display title: 6) Reference (Loop Patterns)
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    slides: https://blockpy.cis.udel.edu/blockpy/download_file?placement=assignment&directory=1266&filename=CISC108_Loop_Patterns_Cheat_Sheet.docx
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 3
    created: September 24 2022, 0159 PM
    modified: September 24 2022, 0222 PM
  files:
    path: bakery_for_reference_loop_patterns_sheet
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
This is a reference page on all the loop patterns; it will be useful as you work on the chapter material. You can also download and print it out using the button in the top-right!

## General Notes

**Before and After the Loop**

Assume the following list variable is initialized:

```python
my_list = [10, 30, 20, 40]
```

After you have used a pattern, you might print, return, or pass the result into another function.

**Iteration Variable**

Do not use `item` as your iteration variable. 

```python
for word in my_words:
for number in the_numbers:
for fruit in fruits:
```

# Loop Patterns
## Count

```python
counted = 0
for item in my_list:
    counted = counted + 1
```

The Count pattern is a specific case of the Accumulate pattern. The result is an integer representing the number of elements in the list. You can also use this for indexes of each element.

## Sum

```python
summated = 0
for item in my_list:
    summated = summated + item
```

The Sum pattern is a specific case of the Accumulate pattern. The result is an integer representing the total of all the elements in the list added together. Sometimes you modify `item`.

## Accumulate

```python
result = ___
for item in my_list:
    result = result ????? item
```

The Accumulate pattern collapses an entire list of values down into one value. You need two things:

1.	The initial value of the accumulation
2.	How to combine an item with the result

In the `___` blank, put an initial value based on what you will accumulate. Typically:

* Strings are initially the empty string `""`
* Integers and floats are initially zero `0`
* Booleans are either `True` or `False`
 
For the question marks (?????), use an operator based on what you accumulate. Typically:

* Strings are added with `+`
* Integers and floats are added (`+`), multiplied (`*`), divided (`/`), subtracted (`-`), etc.
* Booleans can be combined with the `or` operator or the `and` operator

## Map

```python
new_list = []
for item in my_list:
    new_list.append(___)
```

The map pattern produces a new list based on the old list, but modifies the value in some way. Technically speaking, the Map pattern is just a specific example of the Accumulate pattern, but for lists.

The `___` blank should be an expression that involves `item` in some way. For example, you might be doubling it (`item * 2`).

Be careful not to assign the result of calling append back to the `new_list`. That function produces `None`, so you clobber your `new_list`! 

Frequently, you will call a helper function inside of the `___` blank.

## Filter

```python
new_list = []
for item in my_list:
    if ___:
        new_list.append(item)
```

If you want to remove items from a list, you will need to have an `if` statement with a conditional.

The `new_list` has the same element type as the original list. Items are removed, not changed. 

The `___` blank should be an expression that asks something about `item` in some way. For example, you might find out if the value is greater than zero (`item > 0`).

You can use the Filter pattern to modify any accumulation, swapping out the body of the `if` statement with whatever accumulation you need.

## Take

```python
taking = True
new_list = []
for item in my_list:
    if ___:
        taking = False
    elif taking:
        new_list.append(item)
```

If you want a copy of a list without elements past a certain point, you will need to have an `if` statement and an additional boolean variable.

The `new_list` has the same element type as the original list. Items are removed, not changed. 

The `___` blank should be an expression that asks something about `item` in some way. For example, you might ask if this item is equal to a certain value (`item == 47`).

## Find

```python
found = None
for item in my_list:
    if ___:
        found = item
```

If you want to find a single value in a list, you will need to have an `if` statement and an additional boolean variable.

The `___` blank should be an expression that asks something about `item` in some way. For example, you might ask if this item is equal to a certain value (`item == 47`).

Afterwards, the `found` variable will either be `None` or the last value from the list that satisfied the conditional.

You may want to swap out the initial value of found to be some other default value.

## Min/Max

```python
minimum = my_list[0]
for item in my_list:
    if item < minimum:
        minimum = item

maximum = my_list[0]
for item in my_list:
    if maximum < item:
        maximum = item
```

The Min/Max pattern are specific examples of the Find pattern.

A major difference is that the initialization is now the first element of the list.

Another major difference is that the conditional requires checking the current value of the found value.

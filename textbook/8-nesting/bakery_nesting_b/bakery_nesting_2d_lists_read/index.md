---
waltz:
  title: bakery_nesting_2d_lists_read
  display title: 8B1) Nested Lists Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Nesting Lists
    youtube:
      Bart: 57sGMXQylNg
      Amy: Ew4uLGE93CQ
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 11
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0620 PM
  files:
    path: bakery_nesting_2d_lists_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Lists of Lists

```python list-of-lists
numbers = [
  [1, 2, 3, 5, 6],
  [7, 8, 9, 10, 11],
  [12, 13, 14, 15, 16],
  [17, 18, 19, 20, 21],
]

# Entire nested list
print(numbers)
# Third row of values
print(numbers[2])
# First row, second column's value
print(numbers[0][1])
```

A common pattern is to store data, especially numeric data, in a list of lists.
This structure is similar to the tables that we saw with nesting dataclasses in lists.
Except now, every item inside the table must be the exact same type.
Structurally, the inner lists all have the same element type, a primitive type.
The outer list has a somewhat complex element type: a list of list of primitives.
We might also think of this as a "grid" or "2-Dimension" list of numbers.
The representation is very useful for representing X and Y coordinates.

## Nested Iteration

```python nested-iteration
numbers = [
  [1, 2, 3, 5, 6],
  [7, 8, 9, 10, 11],
  [12, 13, 14, 15, 16],
  [17, 18, 19, 20, 21],
]

# Iterate through outer list
for row in numbers:
    # Iterate through inner list
    for number in row:
        # Reached actual integer
        print(number)
```

Frequently, you will want to loop over the data, just like we did with one dimensional lists.
To do so, we need to nest the `for` loops as shown.
Notice how when we iterate through the outermost list, we get a `row` for each element.
Then we can iterate through each `row` to get each `number`.
The innermost body of the nested loops represents one individual element.

## Nested Accumulate

```python nested-sum
nested = [[4, 6, 8],
          [3, 5, 3]]

total = 0
for row in nested:
    row_total = 0
    for value in row:
        row_total = row_total + value
    total = total + row_total
print(total)
```

Actually doing something with the individual elements, however, requires state outside of the loops.
Much like how our loop patterns had an additional variable outside of the loop, we require additional variables
outside of both of the loops, depending on what we are trying to do.
In the code shown here, we are adding up all the numbers in the list, first by iterating through row and summing their values, while adding together all of those nested sums.
Technically, in this case, we could have added directly to the `total` variable, but we will soon see another example where we MUST have inner accumulation variables.

## Nested Map

```python nested-map
def double_table(table: list[list[int]]) -> list[list[int]]:
  new_list = []
  for row in table:
      new_row = []
      for value in row:
          new_row.append(value * 2)
      new_list.append(new_row)
  return new_list

print(double_table([[4, 6, 8],
                    [3, 5, 3]]))
```

In this function `double_table`, we are implementing the Nested Map Pattern by iterating through the list of list of integers given.
For each row, we have to create a `new_row`. We also need to append each `new_row` to a `new_list` in each of the outermost iterations.
When we are done, we'll have perfectly recreated the original structure, but this time each of the original numbers will have been doubled.

## Nested Find

```python nested-find
nested = [[4, 6, 8],
          [3, 5, 3]]

found = None
for row in nested:
    for value in row:
        if value > 5:
            found = value
print(found)
```

In this last Nested Loop Pattern, we see a modification of the Find Pattern where we find the last value greater than 5.
We are once again iterating through each and then through each element within that row.
With the `if` statement inside of the innermost `for` loop, we ask a question about each individual element.
Because we are seeking a property about the entire table and not just within each row, we can use the same `found` variable
throughout the entire nested iteration.

## X/Y Iteration

```python x-y-iteration
grid = [
  [1, 2, 3, 5, 6],
  [7, 8, 9, 10, 11],
  [12, 13, 14, 15, 16],
  [17, 18, 19, 20, 21],
]

for y, row in enumerate(grid):
    for x, value in enumerate(row):
        print(x, y, value)
```

Combining what we have learned about iterating through indexes with what we see now about iterating through two dimensional lists,
we can iterate through the indexes of the grid of data to get access to the X and Y positions within the table.
Note how we iterate vertically through the table in the outermost loop, meaning that each index represents the `y` coordinate into the table.
The inner loop iterates within a row, so that represents the column or `x` coordinate.
Inside the loops, we have access to each individual x and y coordinate.

## X/Y Access and Update

```python x-y-update
grid = [
  [1, 2, 3, 5, 6],
  [7, 8, 9, 10, 11],
  [12, 13, 14, 15, 16],
  [17, 18, 19, 20, 21],
]

# Read third row, second column
print(grid[2][1])

# Write third row, second column
grid[2][1] = 100
print(grid[2][1])
```

Instead of iterating by position, we can also access and update specific values within the grid by chaining together the indexing notation.
This is actually similar to how we chain together attribute accesses, or method calls.
Each time we reach another layer of data, we have to unpack the information with another index.
The expression `grid[2]` gives a list, so we can unpack that with another indexing by having `grid[2][1]`.
Much like how we iterated vertically and then horizontally, it's important to remember that the indexing happens with the Y axis first, then the X axis second.

## Decomposing Grids

```python decomposition
def sum_row(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total = total + number
    return total

def map_sum(grid: list[list[int]]) -> list[int]:
    result = []
    for row in grid:
        result.append(sum_row(row))
    return result

print(map_sum([
  [1, 2, 3, 5, 6],
  [7, 8, 9, 10, 11],
  [12, 13, 14, 15, 16],
  [17, 18, 19, 20, 21],
]))
```

Decomposing complex grid-handling functions with a helper function is a smart way to make complicated code easier to read.
Instead of trying to do two different loops, we can have one of the helper functions in a separate loop.
This example shows how we can turn a list of list of integers into a single list of integers by mapping a sum function to each row.
This same idea can be applied to many other 2d list operations.
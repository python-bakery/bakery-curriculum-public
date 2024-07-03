---
waltz:
  title: bakery_for_composition_read
  display title: 6B2) Loop Composition Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Loop Composition
    slides: bakery_for_composition.pdf
    youtube:
      Bart: 7N5ch_c_3-c
      Amy: bDGw_8SYbQ8
    summary: Looping is complicated but powerful, so we want to find ways to make
      it easier to apply. One good solution is to compose loop functions to create
      more complex behavior.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0130 AM
  files:
    path: bakery_for_composition_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Directly Looping in Functions

```python direct-average
def average(nums: list[int]) -> float:
    sum = 0
    count = 0
    for num in nums:
        sum = sum + num
        count = count + 1
    return sum / count

print(average([1, 4, 5]))
```

You can calculate the mean, or average, of a list by adding together the elements and dividing by the number of elements.
Finding the average is a common operation for a list.
You could write this function by creating a loop that combines the Sum and Count patterns.
This is a valid solution, but ends up being a little complicated inside of the loop with the two statements.

## Indirectly Looping in Functions

```python
def sum(nums: list[int]) -> int:
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
def count(nums: list[int]) -> int:
    count = 0
    for num in nums:
        count = count + 1
    return count
def average(nums: list[int]) -> float:
    return sum(nums) / count(nums)
```


Alternatively, you could define functions to sum and count, and then use those functions in your Average function.
This version does not require a loop directly in the Average function, because the loop happens indirectly in a helper function.
Although this version takes more code, each function only has to do one thing, making it easier to test and debug each individual component.

## Functional Decomposition

![A diagram showing how a main function is decomposed into calls to several helper functions.](bakery_loops_decomposition_arrows.png)

Earlier, we learned to break up complex functions into multiple parts using functional decomposition.
With loops, we finally see why that becomes necessary.
The control flow for a function with a loop is complicated.
When you start nesting loops and if statements inside of functions, mistakes are likely.
Functional decomposition allows us to tame that complexity by focusing on one conceptual step at a time.

## Complex Combinations

![A person is shown thinking about the many different actions they must take.](bakery_loops_decomposition_confusing.png)

Let's say that we wanted to add up all the negative numbers in a list.
You could write a for loop that combines the Filter pattern and the Count pattern.
You might even succeed.
But what if you also needed to convert all the elements from strings to integers first?
What if you needed to also find the average?
Suddenly, combining all these patterns becomes difficult.

## Composing Loop Patterns

```python
# Helper functions
def map_strs_to_ints(numbers: list[str]) -> list[int]:
def remove_negatives(numbers: list[int]) -> list[int]:
def count(numbers: list[int]) -> int:
def sum(numbers: list[int]) -> int:
    
# Main function
def average_positives(numbers: list[str]) -> float:
    numbers = remove_negatives(map_strs_to_ints(numbers))
    average = sum(numbers) / count(numbers)
    return average
```

Instead, let's focus on defining functions to solve each part of the puzzle in turn.
We define a `map_strs_to_ints` function that maps string conversion over a list of strings.
We define a `remove_negatives` function that filters out negative integers.
We define a `count` and `sum` function that consume lists of integers to accumulate.
Then, we can compose those functions as needed into an `average_positives` function.
This may seem like a lot more work - suddenly we have to define and test 5 functions instead of 1.
But the advantage is that each function is relatively easy to define and test.
If you make a mistake, you will be able to track it down very quickly.

---
waltz:
  title: bakery_time_sorting_read
  display title: 9B2) Sorting Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Sorting and Searching
    youtube:
      Bart: AwM62lQAqJM
      Amy: _4Eheef8jYs
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 8
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0627 PM
  files:
    path: bakery_time_sorting_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Sorting and Searching

* Sorting: Putting elements in order
* Searching: Finding an element in a list

In this chapter, we will be looking at sorting and searching, two important operations on a list.
These operations have been exhaustively studied by Computer Scientists over the year, and they have some interesting characteristics.
So although we study them partially because they are useful in their own right, we also will study them because they are very educational.

## Simple Sorting

```python simple-sorting
data = [5, 4, 9, 7, 3, 6]

in_order = sorted(data)

print(in_order)
```

One of the most fundamental operations to do on a list is to sort the elements.
For a list of numbers like the one shown, this puts them into ascending order.
You can sort elements of any type, as long as they support ordering comparisons - this includes strings and floats, but does not include dataclasses by default.
Sorting is so useful, Python provides a built-in `sorted` function to make it easy to sort a given list.
Some interesting algorithms become available when we start working with sorted lists.
So before we talk about how the `sorted` function works, let's take a look at a different problem: searching.

## Iterative Search

```python iterate-search
def linear_search(target: int, data: list[int]) -> int:
    for number in data:
        print(number, target, data)
        if target == number:
            return target
    return None

print(linear_search(3, [1, 2, 9, 5, 7, 8, 3]))
```

Previously, we learned how the Find pattern would let us determine if an element was in a list.
That pattern had us use a `for` loop to walk through each number in the list, and check if it was the target.
If we find the target, we can immediately return.
But in the worst possible case, the element could be at the very end or not even in the list.
In that case, we would have to go check every single element.
If there were a million elements, we would have potentially have to do a million checks!
This is known as linear search, or sometimes iterative search, and it is easy to understand but can be unfortunately slow.
Fortunately, there is a faster way to search that we can use, IF we have a sorted list.

## Binary Search

```python binary-search
def binary_search(target: int, data: list[int]) -> int:
    midpoint = len(data)//2
    while target != data[midpoint]:
        print(midpoint, target, data)
        if target < data[midpoint]:
            data = data[:midpoint]
        else:
            data = data[midpoint+1:]
        midpoint = len(data)//2
        if not data:
            return None
    return target

print(binary_search(3, [1, 2, 5, 7, 8, 9]))
```

Shown here is the classic binary search algorithm that repeatedly divides a sorted list in half to find a target.
First, the function calculates the midpoint of the list using the `len` function.
If the `target` is equal to the value at the middle index of the list, then we stop looping and return the `target`.
However, if not, then instead we check whether the `target` is less or greater than the value at the midpoint.
If less than, we trim `data` to be only the first half of the list.
If it is greater than, we trim `data` to be the second half of the list, skipping over the midpoint element.
Then, we recalculate the new midpoint of this smaller, half-sized list.
If we run out of list, then we stop the function and return `None`. Otherwise, we loop back and check whether we have found our target.
Try experimenting with different values for `target` and `data` to see the effect on the iteration.

## Binary Search Time Complexity

* Formula: log₂(number of elements)
* 8 elements is log₂(8), only 3 checks!
* 1024 elements is log₂(1024), only 10 checks!
* 1024 elements is log₂(1024), only 10 checks!
* 1 million elements would only be about 20 checks!

This binary search algorithm, which repeatedly divides a search space in half, is one of the most remarkable algorithms in Computer Science.
You will see that its approach is much faster than a simple iterative search.
The time complexity of binary search is said to be "logarithmic on the size of the input".
Logarithmic, in this case, refers to how we repeatedly divide the input into two.
Logarithmic relationships are significantly better than linear, although they do not beat constant time.
Still, being faster than linear is a wonderful accomplishment, and we should be proud of this little algorithm.
Keep in mind, however, that this faster search is only possible because we knew the list was sorted.

## Some Sorting Algorithms

* Bubble Sort
* Selection Sort

So since sorting is so useful, we need to understand how it works.
In the rest of this section, we will quickly go over the code of two different sorting algorithms, just to give you an idea of what is possible.
This may not be sufficient to help you learn how the algorithms work, but we will provide some additional links at the end of good websites that have helpful visualizations of these sorting algorithms in more depth.

## Bubble Sort

```python bubble-sort
def bubble_sort(data: list[int]) -> list[int]:
    length = len(data)
    for i in range(length):
        for j in range(length - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

print(bubble_sort([5, 4, 9, 7, 3, 6]))
```

One of the simplest classic sorting algorithms is Bubble Sort, which operates by repeatedly swapping adjacent elements until all elements are in the right order.
Note the most-indented line of the function, which does a swap of two adjacent list elements, but only if the first element is greater than the second element.
That conditional swap is inside of a nested `for` loop.
The outer loop is guaranteed to run a linear number of times, once for each element of the list.
Every inner loop requires an additional linear number of steps; although we do one fewer step each time, we are still going to have to do a linear number in total.
Nesting a linear loop inside of a linear loop actually causes *Quadratic* growth, which is very slow indeed.
Bubble sort is fairly easy to code, but does not work very well in practice.

## Insertion Sort

```python insertion-sort
def insertion_sort(data: list[int]) -> list[int]:
    for i, current in enumerate(data):
        j = i - 1
        while j >= 0 and data[j] > current:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = current
    return data

print(insertion_sort([5, 4, 9, 7, 3, 6]))
```

An improvement to Bubble Sort is Insertion Sort, which also works by swapping adjacent elements.
However, the difference is in the inner loop, which no longer iterates through all of the elements.
Instead, the inner loop is a `while` loop that swaps the current element backwards through the list until it encounters a smaller element.
At any given point in time, the elements prior to the `current` element are in sorted order.
We are merely dragging elements from the back of the list to the front and placing them in the appropriate spot.
In the best case, the list is already sorted and we only have to walk through to confirm this.
But in the worst case, we may be dragging each element all the way from the back to our current position as we walk through the list.
This makes Insertion Sort an even more interesting sorting algorithm, because suddenly the runtime depends on more than just the size of the input: the values of the input also affects the time complexity.
Still, the fact that sometimes the sorting algorithm performs poorly means we would like to find a better one.

## Other Sorts

* HeapSort
* MergeSort
* QuickSort
* TreeSort
* HashSort
* ...
* https://visualgo.net/en/sorting

There are a huge number of other sorting algorithms out there, each with their own advantages and disadvantages.
We are have only looked at two simple ones, Bubble Sort and Insertion Sort.
If you would like to learn more sorting algorithms, we recommend you check out the website shown here for interactive visualizations.
There are many more resources on the web for learning about sorting algorithms, and you will also hear about them in future Computer Science courses.
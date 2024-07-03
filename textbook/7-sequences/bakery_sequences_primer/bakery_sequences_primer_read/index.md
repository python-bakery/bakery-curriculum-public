---
waltz:
  title: bakery_sequences_primer_read
  display title: 7) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    header: Sequences
    youtube:
      Bart: squyTXGm70g
      Amy: qjqdHfWtNbA
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0615 PM
  files:
    path: bakery_sequences_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_sequences_primer_read\grades.txt
---
## Using Indexes

```python
values = [7, 4, 6, 5, 3, 9]
print(values)

# Update value at index
values[1] = 7
print(values)
```

Lists have been a powerful addition to our toolkit, along with loops for processing them.
But back when we first started with lists, we only learned how to index specific elements.
It turns out that in addition to reading values in lists, we can also update those values.
Much like updating dataclass instances, the indexed list goes on the left-hand side of the assignment statement.
This mutates the list itself, once again similar to mutating a dataclass.

## Index Iteration

```python index-iteration
values = [7, 4, 6, 5, 3, 9]

# Iterate through indexes
for index in range(len(values)):
    print(index, values[index])

# Iterate through indexes AND values
for index, value in enumerate(values):
    print(index, value)

# Update indexes in place
for index in range(len(values)):
    values[index] = values[index] * 2
print(values)
```

Sometimes, we need to iterate through indexes instead of values.
This is useful for finding the location of an item in a list, perhaps to find an adjacent element.
Or, you might want to actually update the original list, instead of creating a new list.
Mutating a list, however, means that other parts of the program that were using that list now have to be kept in mind.
Therefore, we will typically avoid mutation in favor of creating new lists.
Still, you should become familiar with the two approaches to iterating through indexes shown here, using the `enumerate` function and the `range` and `len` functions.

## String Iteration

```python
values = "AB, CD, EF"

# Each character on its own line!
for value in values:
    print(value)
print("*******")
# ["AB", " CD", " EF"]
for value in values.split(","):
    print(value)
print("*******")
# ["AB,", "CD,", "EF"]
for value in values.split():
    print(value)

```

Strings are a primitive type, but have some interesting features.
Much like how you can index both strings and lists, you can iterate through strings too.
If you iterate through a string directly, then it gives you each character one-by-one, just like if you indexed the string.
However, you can use the `split` method to iterate through chunks of the string.
Without arguments, the string is split on whitespace.
If you provide a string as an argument, however, you can iterate based on a specific character.
One of the most common ways to iterate is by splitting on a comma, if the string has comma-separated values.

## Filesystems and Files

```python file-reading-example
grade_file = open('grades.txt')
contents = grade_file.read()
grade_file.close()

print(contents)
```

In the second half of this chapter, we will learn more about the filesystem of your computer.
Your computer is a collection of files organized into a filesystem.
Each file has a name with an extension.
Files are grouped together into folders, also known as directories.
Folders can also have other folders inside of them, leading to a hierarchy of files and folders.
Each file across an entire filesystem can be uniquely identified by its path, which is the sequence of folders holding the file from the root to the file itself.
By referencing the path of a file, Python is able to read and write data to files.
In this example, we *open* the file, *read* its data as a string, and then *close* the file.
You must always remember to close files once you are done with them, to avoid memory leaks.

## File Iteration

```python file-iteration-example
grade_file = open('grades.txt')

total = 0
count = 0
for line in grade_file:
    grade = int(line.strip())
    total += grade
    count += 1

grade_file.close()

print(total/count)
```

You might think of a file as a string or a list, since they share some characteristics.
But make no mistake, files are their own type, and they are critical for making sophisticated programs.
By letting us store data between executions and read data from other programs, we can solve a lot of new interesting problems.
In this example program, we iterate through a file line-by-line.
Since each line of the file is an integer, we can grab the text of each line, convert the line to an integer, and then combine those integers to calculate an average.
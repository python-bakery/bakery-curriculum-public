---
waltz:
  title: bakery_sequences_files_read
  display title: 7B2) Files Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Files
    youtube:
      Bart: gucQQNJZTVw
      Amy: YRQOBH846sU
    small_layout: true
    hide_files: false
    summary: In this lesson, you will learn about using Files in Python. Files are
      an important part of making programs useful, because they allow us to persist
      information between runs of a program. Commonly, we obtain many different data
      files, and write a single program that can operate across many files of the
      same type.
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: October 05 2022, 0907 AM
  files:
    path: bakery_sequences_files_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_sequences_files_read\Count-of-monte-cristo.txt
    - bakery_sequences_files_read\scores.txt
---
## Files

![A picture representing a file is shown, as a document with a filename below it. The filename reads `"Count-of-monte-cristo.txt"`. The document has some text in it that is clearly very long.](bakery_sequences_files_monte_cristo_text.png)

You can think of a File as a string of data.
If we know the path and filename of the File, we can use Python to get access to it.
Then you can process the data as if it were a string, or a list of strings, depending on how you want to use it.

## Opening

```python open-example
book_path = "Count-of-monte-cristo.txt"
book_file = open(book_path)

# Boring!
print(book_file)
```

Before you can access a file, you must explicitly open the file using the `open` function.
This function consumes the path to the file as a string and returns a file object.
Typically, we store this file object into a variable.
If you run this code, it will not seem very exciting, since we have not actually processed the data in the file.

## Reading

```python read-example
book_path = "Count-of-monte-cristo.txt"
book_file = open(book_path)

# Use the read() method to get the file as a string
book_text = book_file.read()

print(book_text)
```

The primary way to get data from a file is to use the ".read()" method.
This simply returns the contents of the file as a single string.
Check out this example, where we open the file, read the file handle, and then print the text.
Notice how this is a multi-step process: we use the path to open the file, and then we read from that open file.

## For Loops and Files

```python iterate-example
book_path = "Count-of-monte-cristo.txt"
book_file = open(book_path)

for line in book_file:
    print(line)
```

Often, we want to process a file line-by-line.
Because a File is actually a sequence of strings (each separated by a new line), we can process it using a For loop quite easily.
The example shown will process the file line-by-line, which would be perfect if we wanted to manipulate each line of the file, perhaps to adjust capitalization or convert it to a number.
Notice that with the `for` loop, we no longer need to use the `read` method.
If we had combined the `read` and `for` loop, we would have done string iteration, going through the file character by character.

## Closing Files

```python close-example
book_path = "Count-of-monte-cristo.txt"
book_file = open(book_path)

print(book_file.read())

# This is critical!!!
book_file.close()
```

When you are done with a file, you should always remember to close it using the `close` method.
It's like leaving a house: if you open a door, you need to close the door.
Forgetting to close a file can leak memory resources on older devices, and possibly lose data.

## FileNotFoundError

1. Do you have the right filename?
2. Do you have the right path?
3. Is the file where you think it is?
4. Is your program where you think it is?
5. Ask for help!

Filesystems are tricky, because everyone has a different setup.
Often, we misplace files.
When we try to open a file that does not exist, Python raises an FileNotFoundError and will suggest the file does not exist.
Typically, you should check that you know the exact filename, that you are using the path, and that you know where your Python source file is relative to the file you are opening.

## Example File Processing

```python file-processing
score_sum = 0
data_file = open('scores.txt')

for line in data_file:
    score_sum = score_sum + int(line.strip())

data_file.close()
print(score_sum)
```

Processing books' text is one possible application for files, but often we want to process a file full of numeric data.
Here, we see some example code that will process a list of numbers in a file, each of which represents a score.
We are also using the Sum pattern we learned about before to add each of those scores together.
Notice how we must strip off the new lines at the end of each line, and then convert that line to a number; when we read data from a file, it comes in as a string.

---
waltz:
  title: bakery_sequences_strings_read
  display title: 7A2) String Iteration Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Lists and Strings
    youtube:
      Bart: xXjrxbn7Lt8
      Amy: e631o8adhC8
    small_layout: true
    summary: In this lesson, we will learn more about lists. Specifically, the differences
      between lists and strings. Strings have some important differences from lists,
      but also some shared behavior.
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0600 PM
  files:
    path: bakery_sequences_strings_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Processing a String

```python string-iteration
word = "Hello"

for character in word:
    print(character)
```

Lists and Strings are somewhat similar, since they are both a sequence of things.
Strings are sequences of characters, but Lists can be a sequence of anything.
The key idea is that both Strings and Lists are sequences, which means that you can iterate over them with a FOR loop.
When you iterate over a list, you get each element.
When you iterate over a string, you get each character.

## Using the split() method

```python string-split
text = "A multi-word string!"
words = text.split()
print(words)

text = "ONE"
words = text.split()
print(words)

text = ""
words = text.split()
print(words)
```

Often, instead of processing a list character-by-character, we want to process it word-by-word, or by some other chunking of characters.
To make this easy, strings have a method named split.
Split is an awesome method because it is easy to use.
When you call the method without arguments, a list of strings is returned from the string.

## For loop and Split

```python for-loop-split
authors = "Alice Bob Carol"

for author in authors.split():
    print("By", author)
```

As you can see below, after we have split a string, it is easy to loop over each word.
In this example, we separate each author to print them individually.

## Splitting on Characters

```python split-on-characters
desserts = "Apple Pie,Yellow Cake,Plum Tart"
print(desserts.split(","))

email = "snakerybakery@example.com"
email_pieces = email.split("@")
print(email_pieces)

word = "Banana"
print(word.split("nan"))
```

If you do not pass anything to split, then it splits on any kind of whitespace - spaces, tabs, new lines.
Sometimes, we want to split on other characters.
You can pass a string as an argument to split on a different character.
In this example, we split on a comma ("`,`"), at symbol ("`@`"), and the string `"nan"`.

## String Iteration in Three Ways

```python string-iteration-three-ways
a_string = "AD, BE, CF"

# By each individual character
for a_character in a_string:
    print(a_character)
print("----")

# On chunks of items by a separator
for an_item in a_string.split(","):
    print(an_item)
print("----")

# On chunks of items by any whitespace
for a_chunk in a_string.split():
    print(a_chunk)
```

Just to summarize briefly, there are three major ways to iterate over a string.
Without the split method, you iterate by character.
With a parameter in the split method, you iterate by splitting the string on the parameter.
And without a parameter in the split method, you iterate by splitting the string on whitespace.

## Input/Split/Loop

```python user-input
# Get user input
user_input = input("Type numbers separated by commas: ")

# Split into parts
user_values = user_input.split(',')

# Process each part independently
for value in user_values:
    value = int(value)
    print(value)
```

Here is a useful pattern.
You take a string separated by a specific character from the user, split the elements on that character, and process each component in turn.
Notice how we can use this to process a string of numbers separated with commas by converting them using the `int` function.
Study each statement of this pattern carefully, and make sure you understand it.

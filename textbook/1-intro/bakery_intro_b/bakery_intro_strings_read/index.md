---
waltz:
  title: bakery_intro_strings_read
  display title: 1B6) Strings Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Strings
    slides: bakery_intro_strings.pdf
    youtube:
      Bart: G2SNTDwewtc
      Amy: iph00g8cJtE
    summary: This class gives a more formal introduction to Strings. Although we covered
      Strings briefly back when we learned about types, now we're studying them in
      more depth.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1247 AM
  files:
    path: bakery_intro_strings_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Purpose

```python example-strings
name = "Ada Bart"
word = "rubber"
book = "Dante's Inferno"
website = "https://wikipedia.org"
```

Strings are how we put text data into a computer.
Any text data can be a string: names, words, books, web sites.

## Characters

* Characters: Letters, Numbers, and symbols

Strings are made up of letters, numbers, and symbols.
We call these things "characters".

## The name "String"

![A picture of a necklace of beads with characters written on the beads, spelling out "Hello World"](intro_strings_beads.png)

Think of a String like a necklace, where each bead has a character on it.
We "string together" letters.
The single or double quotes are knots at the end that tie the letters off.

## Notation

```python string-notation
message1 = "What's wrong with me?"
message2 = 'He said, "What did you do?"'

print(message1)
print(message2)
```

Strings are represented with quotes.
You can use either double quotation marks or single quotation marks.
However, if you start a String with double, you must end with double.
If you start with single, you must end with single.
The reason there are two kinds is to make it easier to create strings like the ones shown.
In the first string, we can have single quotes because we wrapped the string in double quotes.
In the second string, we can have double quotes because we wrapped the string in single quotes.

## Escape Characters

```python escape-characters
print("He said, \"What's wrong with me?\" to the girl.")

print("This will\nbe on two lines.")

print("\tThis will\thave some\tgaps.")
```

So how do you have a string with both single and double quotes in it?
You can use escape characters.
By putting a back-slash `\` before a character, you create a special character.
In the code shown here, we have a slash before the double quotes so that they are escaped safely.
There are actually many kinds of escape characters.
A slash before a lowercase "n" makes a new line in the string when it is printed, like if you pressed enter.
A slash before a lowercase "t" makes the string indented when the string is printed, like if you pressed tab.

## Numbers and Strings

```python numbers-and-strings
# Predict what will be printed when this code runs!
print(1 + 2)
print("1" + "2")
```

It's a little confusing, but you can put a number in quotes.
However, this means that you have a string and not an integer.
The difference becomes very obvious when you try to add things together.
`"1" + "2"` is `"12"`, instead of `3`.
Python is very strict about the differences between Numbers and Strings.

## Variables and Strings

```python string-vs-variable
my_string_variable = "A string value"

print(my_string_variable)
```

Some people confuse Variables and Strings, but they are very different.
Strings are values, while variables hold values.
You can update a variable with a new value, but you cannot assign to a string. That is a syntax error. Try swapping the order of the value and the variable in this code, and you will see for yourself that it cannot work!

## Triple Quoted Strings

```python triple-quoted-string
my_variable = """This is a long multi-line 
text block. Notice how it can spill onto 
multiple lines. It has been assigned to a new 
variable called my_variable. You can use 'single'
and "double" quotes inside."""

print(my_variable)
```

Rarely, you have to put a huge amount of text into your program. The best way
to do so is to use "triple quoted strings". The syntax is simple: you start and
end the chunk of text with three quote marks. It doesn't matter if they are
single or double quotes, as long as it starts and ends the same.
---
waltz:
  title: bakery_appendix_misconceptions
  display title: Appendix E) Misconceptions
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 1
    created: August 21 2022, 0133 PM
    modified: August 21 2022, 0133 PM
  files:
    path: bakery_appendix_misconceptions
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
This document is a collection of feedback for misconceptions identified during previous exams. We do recommend reading
over this entire document, and reviewing the rest of your notes from the semester (or perhaps rewatching the videos).



* * *

# Variables

Recognize the difference between variables and values. Know the term "literal value" and how it differs from a "value
associated with a variable". Be able to predict the result of assignment and how it changes the value associated with a
variable.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_values_reading" target=_blank>Lesson 7- Values</a>, <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_variables_assignment_reading" target=_blank>Lesson 11- Variables</a>, and <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_tracing_reading " target=_blank>Lesson 12- Tracing</a>.

Recognize that only a few things can change the value of a variable:

  1. Assignment will update the variable on the left-hand side of the assignment statement ([Lesson 11- Variables](https://udel.instructure.com/courses/1604660/pages/lesson-11-variables)).
  2. When you use the `def` keyword, you are creating a function; that function's name is technically a variable (that represents a function, so you should only use it to call the function) (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_defining_functions_reading" target=_blank>Lesson 20- Defining Functions</a>).
  3. The parameters of a function (not the arguments) are variables that are only available within the body of the function. Parameters automatically get values after the function is called (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_defining_functions_reading" target=_blank>Lesson 20- Defining Functions</a>).
  4. The iteration variable of a `for` loop will be a new variable that takes on each of the values from the iteration list (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_for_loops_reading" target=_blank>Lesson 32- For Loops</a>.



* * *

## Tracing Assignment

Variables do not update automatically in response to other variables changing, they only update when one of the above
happens to that variable.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_tracing_reading" target=_blank>Lesson 12- Tracing</a>



* * *

## Int and Float Operations

Whenever you do math involving a `float`, the result will be a `float`. Whenever you do division, the result will be a
`float`. No matter how complex the math is, if at some point it produces a `float` uses a `float`, then the rest of the
expression will be a `float`.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_arithmetic_reading" target=_blank>Lesson 9- Arithmetic</a>



* * *

## String Values vs. Other Values

Strings are anything surrounded by single or double quotes. Even if the thing surrounded by quotes looks like some other
kind of value, it's still a string. For example, all of the following are strings:

```python

"True"
"False"
"5"
"None"
"def"
"for"
"integer"

```

Remove the quotes, and they all become very different things.

* * *

## String Conditionals

There are several kinds of tests we can do on strings:

  * We can do membership testing to determine if a string is in another string. We must match every character in the left string precisely in the right string, including spaces, symbols, and capitalization.
  * We can test if two strings are equal or not equal. Again, every character must match precisely.
  * We can test if one string is less than/greater than another, which uses alphabetical ordering.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_strings_reading" target=_blank>Lesson 15- Strings</a> and <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_string_operations_reading" target=_blank>Lesson 16- String Operations</a>

* * *

## String Indexing and Slicing

String indexing let's you access a specific character in a string by a position, starting at zero. You can also access
elements from the back starting at `-1`. When doing string indexing, write the string on a sheet of paper, and then put
the indexes DIRECTLY BELOW each character (zero counting up from the left, and -1 counting down from the right).

String slicing let's you access a range of characters in a string by two positions, separated by a colon. If the left
position is left blank, it is assumed to start from zero. If the right position is left blank, it is assumed to end at
the end of the string. When doing string slicing, write the string on a hseet of paper, and then write the positions
BETWEEN the characters (1 between the first and second character then coutning up, and -1 between the second to last and
last character and counting back down).

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_string_operations_reading" target=_blank>Lesson 16- String Operations</a>

* * *

## Truthiness and Order vs. Equality

The rules for truthiness are actually pretty consistent. There aren't that many values that are `False` according to the
rules of Truthiness:

  * `False`
  * `0`
  * `0.0`
  * `""`
  * `[]`
  * `{}`
  * `None`

Everything else is `True`. Note that lists and dictionares are only `False` when they are empty. If you have a list of
`False` values, the list is not empty, so the overall expresion is `True`.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_truthiness_reading" target=_blank>Lesson 28- Truthiness</a>

It is always okay to ask if two things are equal or not equal, even if they are different types. But to ask if things
are in a certain order, they must be the same type (for this purpose, consider `int` and `float` to be the same type).
In other words:

```python

>>> 1 == 1
True  
>>> 1 == 5  
False
>>> 1 == "1"
False
>>> True == None
False
>>> "Dog" != "Doggo"
True

```

```python

>>> 1 < 10
True
>>> 7.5 < 5
False
>>> "Alpha" < 27
# TYPE ERROR!
>>> "Alpha" < "Beta"
True

```

* * *

## Split

There were some real misconceptions about splitting strings. The `split` method of strings let's you convert a string
into a list of strings.

```python

>>> grades = "90,94,82".split(",")
# Notice that these are still list of strings
>>> grades
["90", "94", "82"]
>>> grades[0]
"90"
# We'd have to convert them to integers before we could do math with them
>>> int(grades[0])
90
# We have a list, not a dictionary. You cannot use dictionary access.
>>> grades[","]
TypeError: list indices must be integers or slices, not str

```

You should definitely check out <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_lists_strings_reading" target=_blank>Lesson 35- Lists and Strings</a>.

* * *

## Iteration Variable

When we write a `for` loop, we are iterating through something. We create a new variable to hold each value from that
something. We refer to the new variable as the "iteration variable" (sometimes known as an "iteration target"). In the
code `for item in sequence`, the iteration variable is `item`. The type of `item` is dependent on the type of
`sequence`. In particular, the type of `item` is the subtype of `sequence`.

If `sequence` is a list of strings, then `item` will be a string. If `sequence` is a list of dictionaries, then `item`
will be a dictionary.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_for_loops_reading" target=_blank>Lesson 32- For Loops</a>

* * *

# Flow

Programs move top-to-bottom. A few things interrupt that flow:

  * Function calls jump execution to the body of the function (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_data_flow_reading" target=_blank>Lesson 26- Data Flow</a>)
  * The `return` statement jumps execution back to where the function was called from (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_data_flow_reading" target=_blank>Lesson 26- Data Flow</a>)
  * The `if`, `elif`, and `else` statements allow us to optionally pass over its body (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_if_reading" target=_blank>Lesson 27- If Statements</a>)
  * A `for` loop allows us to repeatedly go through the body, or completely pass over the body if the iteration list was empty (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_for_loops_reading" target=_blank>Lesson 32- For Loops</a>)

* * *

## Statements and Expressions

A single line (a statement) is not always read left-to-right. Depending on the statement, you might jump around a bit.
Assignment statements, for example, should be read right-hand first, then left-hand first. On the right-hand side, you
can have an expression that has a very complicated order depending on the use of operators, function calls, and
parentheses.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_statements_expressions_reading" target=_blank>Lesson 13- Statements and Expressions</a>

* * *

## Function calls and Function definitions

Make sure you know what a function _call_ requires:

  * Function name
  * Parentheses
  * Arguments (potentially)

As opposed to a function _definition_ , which requires:

  * _`def` _keyword
  * Function name
  * Parentheses ( and )
  * Parameters (potentially)
  * Colon (:)
  * Indentation (four white spaces)
  * Body (at least one statement, maybe more)

Printing is not necessary for function calls. Sometimes we may ask you to print the result of calling a function, but
that doesn't mean you have to always print.

Calling a function does NOT require a colon.

Parentheses are ALWAYS required when calling a function.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_defining_functions_reading" target=_blank>Lesson 20- Defining Functions</a> and <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_calling_reading" target=_blank>Lesson 17- Calling Functions</a>

* * *

# Data Flow

Many students struggled with questions about Data Flow, the idea of passing values through functions. If I call a
function, I pass in values through arguments. Those arguments' values get attached to parameters automatically through
Python. If you later return a value, the original function call is substituted for whatever is returned.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_data_flow_reading" target=_blank>Lesson 26- Data Flow</a>

* * *

## Clobbering Parameters' Values

One of the biggest misconceptions that I see is something like this:

```python

def add(alpha, beta):
    alpha = 5
    beta = 3
    return alpha+beta

result = add(5, 3)

```

This is _extremely_ incorrect and demonstrates that you fundamentally don't understand what parameters and arguments.
Python is already assigning the `5` to the `alpha` parameter - you should not be doing it yourself. If you do, you
destroy the possibility of someone else using your function. What if I come back later and try this?

```python

result2 = add(7, 2)

```

The broken version of `add` would always return `8` instead of `9`, because you clobbered the parameters' values.
Instead, observe this correct version:

```python

def add(alpha, beta):
    return alpha+beta

```



* * *

## Scope

There are two kinds of scopes: local and global. All programs have a global scope. There's also a local scope for each
function. Parameters are automatically in the function's local scope, as are any variables defined inside the function's
body (not _after_ , but _inside_ ). Other variables are considered to be global.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_scope_reading" target=_blank>Lesson 23- Scope</a>

* * *

## Print, Input, Return, Parameters

There are two ways to get data into a function: parameters and the `input` function. There are two ways to get data out
of a function: the `print` function and `return` statement. They each fundamentally do different things:

  * The `input` function let's the user (a human) type some text in and then returns that value wherever you called `input`. (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_console_io_reading" target=_blank>Lesson 6- Console IO</a>)
  * The `print` function takes some data and puts it on the console. It's a one-way trip to let the user know something. Nothing gets returned. (<a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_return_print_reading" target=_blank>Lesson 22- Return and Print</a>)
  * Parameters allow us to access the values of arguments passed into a function call. When you call a function, you have values (arguments) inside of the parentheses. Those arguments are assigned to parameters. This is how data usually flows _into_ a function. <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_data_flow_reading" target=_blank>Lesson 26- Data Flow</a>
  * Return statements allow us to make a function produce a value. When a function reaches a `return` statement, the function body stops and we jump back to where the function is called. Whatever value was returned is substituted in for the function call. <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_data_flow_reading" target=_blank>Lesson 26- Data Flow</a>

There's no limit to the number of parameters or the times a function can print or take input. A function can print AND
return. It can take parameters AND take user input. But it can also do any combination of those!

* * *

## Calls and Assignment

If we have the following code:

```python
alpha = input("Type something")
def action1(beta):
    return beta+"!"
def action2(delta):
    print(delta+"?")
```

Data will initially enter the program through the `input` function call and be stored in `alpha`. In order to get that
data into the functions, we will need to call them. If we want to move that data through `action1` and then into
`action2`, we need to compose the function calls in the right order.

```python
action2(action1(alpha))
```

We could also assign to a temporary variable:

```python
epsilon = action1(alpha)
action2(epsilon)
```

Don't try and force extra `print` functions into there - the `action2` function is already printing, so why should we
try to do any extra printing?

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_data_flow_reading" target=_blank>Lesson 26- Data Flow</a>

* * *

## Printing vs. Returning

I swear to Ada, I better not see anyone even suggest that the `unprint` statement is a thing. There's no such thing. If
you want to get data out of a function, you have to use a `return` statement. If you `print`, then that data is now
visible to the user, but it won't be returned from the function. Data printed to the console lives there, you can't get
data that was printed to the console. Although you can prompt the user for new data using `input`, that's not
necessarily the data that was printed - you are at the mercy of whatever the user wants to type in!

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_return_print_reading" target=_blank>Lesson 22- Return and Print</a>

* * *

## Printing a Print Call

If a function does not explicitly return a value, then it returns the special value `None`. A common mistake is to think
that a function which printed also returned a value. For example:

```python

def add5(a_number):
    increased = a_number + 5
    print(increased)

print(add5(10))

```

The `add5` function does `print` but does not `return`. Therefore, it returns the value `None`. Therefore, although the
first value printed is `15`, the code will also print the value `None` after the `add5` call finishes (since `None` is
returned).

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_return_print_reading" target=_blank>Lesson 22- Return and Print</a>

* * *

# Mutability

Lists and dictionaries are mutable. Strings, integers, floats, boolean, and None are immutable. The idea is whether you
can intrinsically change the value. You can add and remove stuff from lists and dictionaries, but immutable values are
fundamentally always the same.

If you perform `5+1`, you are not changing `5` into a new value. Instead, you create a new value `6` and forget the old
values `5` and `1` for now. They still exist - the concept of `5` is not gone. If you calculate `not True`, the new
value `False` does not replace the existence of `True`. And, in Python, if you do something like `"Hello".lower()` you
are producing a new string instead of altering the original value `"Hello"`. The specifics might be clearer if you look
at variables holding immutable values:

```python

# Strings are immutable, but we can produce new versions of a value
>>> "Hello"
"Hello"
>>> "Hello".lower()
"hello"
# Even if an immutable value is in a variable, you cannot change the value
>>> message = "Hello"
>>> message
"Hello"
>>> message.lower()
"hello"
>>> message
"Hello"
# So if you want to change the value, you must assign it back to the variable
>>> message = message.lower()
>>> message
"hello"

```

Compare that to what happens when you have a list:

```python

# Lists are mutable, so we can add new elements
>>> dogs = ["Ada", "Klaus"]
>>> dogs.append("Butters")
>>> dogs
["Ada", "Klaus", "Butters"]

```

A tricky thing with the `append` method is that it returns `None`. So it's a mistake to assign its value back to the
list.

```python

>>> dogs = dogs.append("Spike")
>>> dogs
None

```

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_mutability_reading" target=_blank>Lesson 34- Mutability</a>

* * *

# Composite Type Relationships

Composite types include Lists and Dictionaries, as opposed to primitive types (int, str, bool, float, None). The core
idea of a composite type is that they are composed of other types. Lists have a single subtype ("A list of TYPE") and
dictionaries have a subtype for their keys and their values ("A dictionary mapping TYPE to TYPE").

The subtype of lists and dictionaries can be any other type, including both primitives and composite types. You can have
lists of lists of ints. Or dictionaries that map lists to integers. Or dictionaries that map strings to lists of
dictionaries that map strings to integers. There's no limit with composite types on how nested and complex they can get.

Strings are confusing because they are sort-of composed of strings. However, it is extremely incorrect to suggest that
strings are composed of lists, integers, or any other type. You may think that something like `"1, 2, 3"` is a string
composed of a list of integers, but that is wrong. It is just a string. You _could_ convert that string into a list
using the `split` method, but that does not mean that the string is composed of an integer or a list; there are any
number of methods and functions we could use to convert values, but that is unrelated to the idea of composite types.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_nested_data_reading" target=_blank>Lesson 41- Nested Data</a>

* * *

## Length of Nested Data

If you are given a complex piece of data (such as a list of dictionaries), you might be asked "how many elements are
there" or "how many keys are there"? The answer depends on the context and you must read the question closely. Let's say
we were given the following code:

```python

dogs = [{"Name": "Ada", "Age": 1},
        {"Name": "Klaus", "Age": 18},
        {"Name": "Butters", "Age": 3},
        {"Name": "Darwin", "Age": 7}]

```

  * "How many lists are there?": 1 list
  * "How many elements are in the list?": 4 elements
  * "How many dictionaries are there?": 4 dictionaries
  * "In the first dictionary, how many keys are there?": 2 keys
  * "In the third dictionary, how many values are there?": 2 values
  * "How many keys are there total?": 8 keys

The person asking the question must be precise. Let's look at another weirder piece of code.

```python

choices = [{"Names": ['Ada', 'Klaus', 'Butters'],
            "Ages": [1, 18, 3]},
           {"Names": ['Reese', 'Pumpkin', 'Jiji'],
            "Ages": [2, 4, 8]}]

```

  * "How many lists are there?": 5 lists
  * "How many dictionaries are there?": 2 dictionaries
  * "How many elements are there in the list?": Too ambiguous, you can't know which list they are referring to. Might be 2 if they're thinking about the outer list, or 3 if they're thinking about one of the inner lists.

* * *

## List Indexing and Dictionary Access

Both lists and dictionaries have their data accessed using square brackets. This makes it really easy to make mistakes,
because lists are ALWAYS indexed with numbers but dictionaries are accessed according to their key's types.

```python

number_names = {0: "Zero", 6: "Six", 5: "Five"}
name_numbers = {"Seven": 7, "Nine": 9, "Ten": 10}
person_names = ["Ada", "Pumpkin", "Reese"]

```

These three variables all allow you to do square brackets, but some expressions are valid and some are not.

```python

# Good dictionary access
>>> number_names[0]
"Zero"
>>> number_names[5]
"Five"
# Bad dictionary access
>>> number_names["Five"]
KeyError: 'Five'
>>> number_names[3]
KeyError: 3
# Good dictionary access
>>> name_numbers["Seven"]
7
>>> name_numbers["Ten"]
10
# Bad dictionary access
>>> name_numbers["Six"]
KeyError: 'Six'
>>> name_numbers[10]
KeyError: 10
# Good list index
>>> person_names[0]
"Ada"
>>> person_names[2]
"Reese"
# Bad list index
>>> person_names["Ada"]
TypeError: list indices must be integers or slices, not str
>>> person_names[5]
IndexError: list index out of range

```

Notice that the error messages for the list are pretty strange - Python gets very confused when you try to treat a list
as a dictionary!

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_lists_indexes_reading" target=_blank>Lesson 36- Lists and Indexes</a> and <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_dictionaries_reading" target=_blank>Lesson 37- Dictionaries</a>.

* * *

## Accessing Nested Data

Dictionaries cannot be accessed by position, unlike lists.

```python

courses = [
    {'title': 'CISC108', 'credits': 3, 'teachers': ['Decker', 'Bart']},
    {'title': 'CISC181', 'credits': 3, 'teachers': ['Wassil', 'Harvey']},
    {'title': 'CISC210', 'credits': 3, 'teachers': ['Roosen', 'Silber']}
]

```

You can access arbitrary elements by position in the lists, but not the dictionary.

```python

>>> courses[0]
{'title': 'CISC108', 'credits': 3, 'teachers': ['Decker', 'Bart']}
>>> courses[0]['teachers']
['Decker', 'Bart']
>>> courses[0]['teachers'][1]
'Bart'
>>> courses[0][0]
KeyError: 0
# You also cannot access dictionaries using values
>>> courses[0]['CISC108']
KeyError: 'CISC108'

```

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_nested_data_reading" target=_blank>Lesson 41- Nested Data</a>

* * *

## Dictionary Access with Operators

A lot of people messed up a question where the dictionary access not literal values. Recall that literal values are
values stored directly in the source code like `"Name"` or `3` or `True`. Although we often access dictionaries with
literal values, it is perfectly possible to have expressions and variables as keys.

```python

>>> tricky = {2: "Alpha", 2+2: "Banana",
              '2+2': "Corgi", '2': 'Delta',
              'Name': 'Ellie', 'name': 'Fwoosh'}
# Let's look at the numbers first
>>> tricky[2]
'Alpha'
>>> tricky[4]
'Banana'
>>> tricky['2+2']
'Corgi'
>>> tricky['2']
"Delta"
>>> tricky[5-1]
'Banana'
# Let's look at strings
>>> tricky["Name"]
'Ellie'
>>> tricky['name']
'Fwoosh'
>>> name = 'Name'
>>> tricky[name]
'Ellie'
>>> tricky[name.lower()]
'Fwoosh'

```

You have to pay attention and potentially do some math. But if you follow the rules of dictionary access, it should be
straightforward.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_dictionaries_reading" target=_blank>Lesson 37- Dictionaries</a>

* * *

## Dictionary Aliasing

Dictionaries are mutable. When you create a dictionary, you end up with a new thing that can be changed. There is just
the one version of it. This has really important implications that can be difficult to follow.

```python

udel = {'name': 'UD', 'students': 437}
udel_copy = {'name': 'UD', 'students': 437}
our_school = udel

def add_students(a_school):
    stds = a_school['students']
    a_school['students'] = stds + 1
    stds = stds + 1

add_students(udel)

```

We have 3 global variables in this code, each of which are dictionaries meant to represent schools. The `add_student`
function has two local variables: `a_school` (a dictionary) and `stds` (an integer). After we call the function, what
are the new values of the `students` keys in the dictionaries?

Dictionaries are mutable, so whenever a dictionary's key's value is changed then that is remembered. Hopefully it is
clear that this code updates `udel['students']` to be `438`.

The `udel_copy` variable is a completely new, different dictionary than `udel`. Since `udel_copy` is not passed into
`add_students`, the expression `udel_copy['students']` will remain `437`.

The `our_school` variable refers to the same dictionary as `udel`. So `our_school['students']` will also be `438`.

Integers are immutable, so when we store an integer like `a_school['students']` into a variable like `stds`, it doesn't
matter that it originally came from a dictionary - any changes to `stds` will not affect the original dictionaries.
Therefore, the last line of the body (`stds = stds + 1`) actually has zero effect on the dictionaries.

See: This [PythonTutor instance](http://www.pythontutor.com/visualize.html#code=udel%20%3D%20%7B'name'%3A%20'UD',%20'students'%3A%20437%7D%0Audel_copy%20%3D%20%7B'name'%3A%20'UD',%20'students'%3A%20437%7D%0Aour_school%20%3D%20udel%0A%0Adef%20add_students%28a_school%29%3A%0A%20%20%20%20stds%20%3D%20a_school%5B'students'%5D%0A%20%20%20%20a_school%5B'students'%5D%20%3D%20stds%20%2B%201%0A%20%20%20%20stds%20%3D%20stds%20%2B%201%0A%0Aadd_students%28udel%29&cumulative=false&heapPrimitives=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) gives a beautiful visualization of the ideas described here.

* * *

## Dictionary Speed

Accessing an element in a list by position is very fast. Accessing an element in a dictionary by key is very fast.

Searching for an element by value in a list could potentially take a long time if the list is big, because we might have
to check every value. Searching for a specific value in a dictionary could potentially take a long time if the
dictionary is big, because we might have to check every value.

Summing up all the elements in a list requires us to visit every element, so it will take longer for longer lists.
Summing up all the values in a dictionary requires us to visit every value, so it will take longer for longer
dictionaries. It doesn't matter if you have a list or a dictionary - if you are summing up all the values inside, it
will take longer if there are more elements.

See: <a href="https://blockpy.cis.udel.edu/assignments/reading/sneks_lookup_find_reading" target=_blank>Lesson- Lookup and Find</a>
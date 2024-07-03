---
waltz:
  title: bakery_intro_console_read
  display title: 1A3) Console I/O Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Console Input/Output
    slides: bakery_intro_console.pdf
    youtube:
      Bart: xwVPAVx9T_0
      Amy: _FJtLkJ5xtw
    summary: In this lesson, you will learn how to write programs that use input and
      output.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1226 AM
  files:
    path: bakery_intro_console_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Phases of a Program

1. Input
2. Processing
3. Output

Every program has three main phases: 
First, input data is given to the program.
Second, the data is processed.
Third, the data is output in some way to the user.
The Inputs and Outputs are how we connect programs to the real world.

## Programming Is Like Baking

![A sequence of three pictures with arrows connecting them. From left to right, there are ingredients (labeled "inputs"), a woman baking ("processing"), and a cake ("outputs")](intro_console_baking_process.png)

Think of it like baking.
The inputs are your ingredients.
Mixing and stirring are the processing.
Then the cake is your output.

## Inputs

![Pictures of a mouse, keyboard, and some kind of USB stick with a sensor on it.](intro_console_inputs.png)

Examples of input are data typed by a keyboard, movements made by your mouse, data from the internet, and data from sensors.

## Outputs

![Pictures of a monitor, printer, and a robot.](intro_console_outputs.png)

Examples of output are pixels on your screen, paper out of your printer, or the movement of a robotic arm.

## Code

* `input`: A function to get data from the user
* `print`: A function to give data to the user

Computers take in data from users and put out results.
In order to transform the inputs into the outputs, we write instructions as code.
The instructions that we write are often stored in a program, so that they can be reused.
This is what "programs" or "code" really are.
Now let's learn how to write a very simple program by learning two basic commands.
The `input` command will let us get information from the user.
The `print` command will let us report information to the user.
Let us take a look at what these commands look like in our very first, simple programs.

## Print

```python print-example
print("This text will be shown to the user")
```

The `print` function lets you write information to users.
Printing is necessary because we cannot see "inside" the mind of the computer when a program runs.
For now, the only thing we end up seeing is the result of whatever we print.
Notice that there is some text between the parentheses: this is the text that is output to the user.
You can try running this program to see the message is "printed" on the console.
You can think of the console as like a messenger box, for sending and receiving data to and from the computer.
Every time you run this program, the exact same text will be written in the console by the computer.

## Input

```python input-example
favorite_color = input("What is your favorite color?")
print("Your favorite color is", favorite_color)
```

The `input` function lets you get information from users.
Notice that once again there is text between parentheses, asking for their favorite color.
That text will be shown as a prompt to the user in the console.
The user will be able to type their answer and press enter.
On the second line, we have used the `print` function to print out that same information.
Without that `print`, this program would only ask the user for their color, without ever reporting anything back at the end.
While not a very big program, this is a demonstration of the input-processing-output workflow that every program will have.

## But Why?

![On the left, a circle is labeled "Types of Data", with smaller circles sticking out - these smaller circles are labeled nouns like "geographical", "financial", "scientific", "statistical", and "cultural". On the right, an arrow labeled "Python" points to a person thinking.](intro_console_why.png)

The goal of any program is to transform the inputted data into the desired outputs.
For now, our programs will have simple inputs and simple outputs that work through the console.
But eventually, we will create complex code that can achieve great things.
For example, you could have the user speak into a microphone, with their instructions translated into the movement of a robot.
Or have the user input recent weather data in order to create the output of future weather predictions.

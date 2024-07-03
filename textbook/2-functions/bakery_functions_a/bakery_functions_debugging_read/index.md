---
waltz:
  title: bakery_functions_debugging_read
  display title: 2A6) Debugging Functions Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Debugging Functions
    slides: bakery_functions_debugging.pdf
    youtube:
      Bart: GOcrBbukqlw
      Amy: Cqqi7jla8U8
    summary: In this lesson, you will learn some practical techniques for fixing a
      program that has errors. These techniques are known as "debugging", and can
      be difficult to learn - you will get better with them as you practice.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1259 AM
  files:
    path: bakery_functions_debugging_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## What is Debugging?

![On the left, a picture of an actual insect (a bug) taped to a piece of paper that reads "(moth) in relay, First actual case of bug being found".  On the right, a picture of [Admiral Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper) (one of the most famous computer scientists)](functions_debugging_bugs.png)

When a program doesn't work, we say that it has a "bug" in it.
When we get rid of bugs, we call it "Debugging".
The first actual case of debugging a computer program was when Admiral Grace Hopper found a moth trapped inside of a relay of the Mark II Computer.
Nowadays, our bugs usually don't involve live insects.

## The Scientific Method

1. Observe failure
2. Hypothesize cause
3. Predict behavior
4. Experiment with code
5. Repeat 3-4 until fixed

When you're debugging code, you should approach it using the scientific method.
First, we observe a failure in our code.
Second, develop a hypothesis as to why the code failed.
Third, turn this hypothesis to make a prediction.
Fourth, test the prediction by experimenting with the code and making observations.
Fifth, repeat steps 3 and 4 until you have fixed the code.
This may be intuitive to some people, but formally following this method can really help train yourself as a programmer!

## Wolf Fencing

```python wolf-fencing
command = input("What are the dimensions")
stop = "stop" in command
#------------------------------------------
print("Works fine until here")
#------------------------------------------
area = length ** width
volume = height * area
set_size(volume)
```

"There's one wolf in Alaska, how do you find it? First build a fence down the middle of the state, wait for the wolf to howl, determine which side of the fence it is on. Repeat process on that side only, until you get to the point where you can see the wolf). In other words; put in a few "print" statements until you find the statement that is failing (then maybe work backwords from the "tracks" to find out where the wolf/bug comes from)."
This method is also known as "Print Debugging".

## Rubber Duck Debugging

![Person speaking to a rubber duck, saying: "Here it should increase the sum variable. Oh wait, it's decreasing it. My mistake. Thanks rubber duck!"](functions_debugging_duck.png)

Okay, this will sound weird. 
First, get yourself a rubber duck or a wise stuffed animal. 
Second, politely inform the duck that you will be explaining your code to it.
Third, explain what your code is supposed to do in general, and the go over each line of code to the rubber duck.
At some point, you will tell the rubber duck what you are supposed to be doing next, and you will realize that's not actually what your code does.
Fourth, thank the duck for its excellent work. 
This may sound crazy, but rubber ducks are actually the world's best coders.

## More About Rubber Ducks

[https://rubberduckdebugging.com/](https://rubberduckdebugging.com/)

[https://www.smbc-comics.com/comic/the-rubber-duck-method](https://www.smbc-comics.com/comic/the-rubber-duck-method)
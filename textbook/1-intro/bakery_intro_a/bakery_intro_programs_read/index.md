---
waltz:
  title: bakery_intro_programs_read
  display title: 1A2) Programming Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Lesson 1A2) Programming
    youtube:
      Bart: 4swXT8qhb9w
      Amy: ZDfWDWEdW44
    slides: bakery_intro_programs.pdf
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1221 AM
  files:
    path: bakery_intro_programs_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## What is a Programming Language?

![Picture of woman writing some instructions in pseudocode on a computer.](intro_programs_what_is_pl.png)

Programs are created by writing instructions in a *Programming Language*, similar to how movie scripts are written in human spoken languages like English.
Programming languages were created by Computer Scientists, to make it easy to write instructions that a computer can understand.
A computer can then run these programs, if they are written correctly.

## Python and Its Competition

![Collage of icons from many different programming languages, including Java, Ruby, C++, PHP, and JavaScript. In the center, Python's icon is circled.](intro_programs_languages.png)

In this course, you are learning a programming language named Python.
However, there are many programming languages out there.
This diagram shows the symbols of a bunch of other possible programming languages that you could learn instead.

## Why Python?

![Three headings on top of three pictures: first is popular over a ranking of different languages that has Python in the lead; second is useful ver a list of application areas that python is useful in including scientific computing, web servers, data science, game development, and scripting languages; third is friendly over a pair of smiling little snakes.](intro_programs_popular_useful_friendly.png)

You might be wondering why Python is a good language to learn, if there are so many options.
First, Python is one of the most popular languages in the world; in fact, according to some metrics, it might be THE most popular programming language in the world.
Second, it has a huge number of libraries that make it useful for a wide range of problems in scientific computing, data science, web development, and much more.
Third, it is sometimes called a "friendly" language for beginners, because many people have found it easier to learn than other languages despite being so powerful.

## Python is a Language and a Tool

1) Python is a programming language
2) Python is a tool that runs programs

Python is actually two things: First, as a programming language, Python is a set of rules for writing Python programs.
Second, Python is also a program, that can execute programs written according to the rules of the Python programming language.
Therefore, we will sometimes refer to Python as a language, and sometimes refer to Python as a tool for running programs.
Before we explain what it means to run a program, let us talk about programming languages a little more.

## A Language for Instructions

![A balancing scale with two unequal sides is shown. On the left side, the Human Languages list is shown with the words intructions, poetry, debate and ellipsis. On the right side, the Programming Languages list is shown with only the word instructions.](intro_programs_human_computer_languages.png)

Human languages, like English or Spanish, can be used to talk about many complex ideas.
However, programming languages are good for only one thing: giving instructions to a computer to solve a problem.
We don't use programming languages to talk to each other the same way we do human languages.
That's because programming languages have a small vocabulary and a limited grammar.

## A Small Language

![An adult is giving instructions to a small child, saying "Sum up all the numbers on that paper". The child looks confused and has thought balloons that make it clear they do not understand the words "sum", "paper", or "all".](intro_programs_child_instructions.png)

Imagine you were giving commands to a very small child in English.
The child only knows a few words.
If they don't know a word, you will have to explain new words to them using words they already understand.
Programming Languages are similar to this - you build new words using a small set of original words.
Most words and ideas that we take for granted as smart humans, are not useable in a programming language unless we add them ourselves based on existing words.
Basically, you can never underestimate how little a computer will understand when it comes to a programming language.

## Rules

* Syntax: grammar, spelling, punctuation
* Semantics: logic, making sense, intent

Programming languages have very strict rules.
This is similar to how we have rules in English.
There are two kinds of rules: syntax and semantics.

## Syntax

![The nonsense text "Run can . upwAys the, to healp?!?" is shown, with speech bubbles annotating various syntactic errors. In particular, the bubbles point to a bad period, bad capitalization, and bad spelling.](intro_programs_bad_syntax.png)

In English, we follow grammar rules about how we can structure our sentences.
The sentence shown here is not grammatically correct english, so we would reject it.
Similarly, in Python, we use symbols, spaces, and words in very precise ways.
Using them incorrectly will give you a "syntax error".
You will probably make many syntax errors as you learn to program.

## Semantics

![The nonsense text "Colorless green ideas sleep furiously" is shown, with speech bubbles annotating various semantic errors. In particular, it highlights that "ideas can't sleep", you can't have something that is "colorless bug green" and it is meaningless to be "sleeping furiously".](intro_programs_bad_semantics.png)

Although the sentence here follows grammar rules, it doesn't make any sense.
This is the idea of semantics, the rules concerned with meaning.
It is very easy to write perfectly valid sentences in Python that accomplish nothing at best and hurt things at worst.
You need to think critically when programming, to recognize when you've written instructions that makes no sense.

## Programs are Text

![An arrow is drawn between the text of a program and a photo of someone writing an essay by hand, relating that they are similar.](intro_programs_are_text.png)

When you write a Python program, you are really just writing some text.
That text needs to be valid Python text, following all of it syntax rules.
But that means its not that different from an essay you might write in english.

## Executing a Program

![A picture of a program's source code, with an arrow pointing downward next to it.](intro_programs_executing_lines.png)

Once a program is written according to the Python language rules, the program can be executed.
This means that the computer will read the text of the program line by line, and perform each step.
This is just like following the steps of a recipe or instructions; just like a human, the computer will do each step one at a time.

## Terminology

* Run: Perform each step of a program line-by-line
* Execute: Synonym for "run"
* Kill: To stop a program

When we want to use a program, we will say the the program is "run" or "executed". Either a program will end on its own, or we will have to stop it ourselves, which is sometimes referred to as "killing" a program.

## Programming Environments

![Screenshot of the BlockPy programming environment, with callouts annotating the output area, the run button, and the program editor.](intro_programs_blockpy.png)

Technically, you can write programs in a text editor and then run them with Python separately.
However, most programmers use a Programming Environment that makes it very easy to write programs and then press a single button to run them.
Usually, running a program causes some kind of visual output, although this is not always guaranteed.
This screenshot shows the BlockPy programming environment, which we will use to write and run basic programs so we can view their output.

---
waltz:
  title: bakery_project2_instructions
  display title: 1) Instructions
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
    version downloaded: 5
    created: August 16 2022, 1116 AM
    modified: October 13 2022, 0932 AM
  files:
    path: bakery_project2_instructions
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
You have gotten an internship at the latest, trendy startup: The **CryptoCorgiCompany**. Your new senior colleague is friendly, but also a little naive. On your first day, you are given an enthusiastic explanation about the companies new Secure Communication Protocol that you will help implement for their mobile chat application.

> "You see, we made up our own algorithm so that no one else would know how it works. As long as we keep it secret, no one can possibly crack our code!"

In the back of your mind, that doesn't sound right to you. If one person can figure out the algorithm, surely another can too, right? Still, internships can be hard to get, and it's a good chance to learn more about encryption, so you decide to give them a chance.

## The Four Functions

In this project, you are going to create a program that will encrypt, decrypt, and hash text. This will be essential for
Ada's new Crypto Corgi Company!

Your first goal is to define the `encrypt_text` function, which consumes a string representing a user's message, and
produces an encrypted version.

You will also need to define the `decrypt_text` which consumes the encrypted version and produces the user's message.

Third, you need to define the `hash_text` which consumes a message and produces a unique [_hash_](https://simple.wikipedia.org/wiki/Cryptographic_hash_function). The hash is a way to convert text to a number that is likely to be unique for each possible string. If someone has tampered with the message, the hash value will be different from what was given.

Finally, you'll put it all together into a single `main` program! This will be a user interface for people who want to use your other functions.

## Function Signatures

Over the course of this project, you will define the following four functions:

  * `encrypt_text`: Consumes a string (plaintext `message`) and an integer (`rotation_amount`), and produces a new string that is encrypted.
  * `decrypt_text`: Consumes a string (encrypted `message`) and an integer (`rotation_amount`), and produces a new string that is decrypted.
  * `hash_text`: Consumes a string (any kind of `message`) and two integers (`base` and `hash_size`), and produces an integer that attempts to uniquely represent the text.
  * `main`: Consumes nothing and produces nothing. Instead, takes user input to encrypt or decrypt a message.

## Quizzes and Tests

Prior to writing these functions, there are some readings and quizzes that will help. The answers to the quizzes will be your unit tests for the project!

## Decomposition

All three functions have a lot of operations in common. We strongly recommend you make at least three helper functions:

  * A function to convert a string to a list of integers using `ord`
  * A function to convert a list of integers to a string using `chr`
  * A function to rotate a list of integers by a given amount.

If you complete these three helper functions, then the remaining functions are all much easier.

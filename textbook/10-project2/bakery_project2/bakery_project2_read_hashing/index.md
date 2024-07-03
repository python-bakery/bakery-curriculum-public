---
waltz:
  title: bakery_project2_read_hashing
  display title: 5) Hashing Values Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 2
    created: October 12 2022, 0334 PM
    modified: October 13 2022, 1053 AM
  files:
    path: bakery_project2_read_hashing
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Hashing values is one of the most powerful ideas in computing. This technique has applications in everything from
cryptography all the way to fundamental data structures. You will revisit the concept of hashing many times throughout
many computing courses.

Basically, hashing is the process of taking a value (like a string) and turning it into a number. This number is much
faster and easier to check than the original string. You can do a simple version of hashing just by converting the
numbers to their ascii integer versions and adding them all up.

```
"CAT" -> [67, 65, 84] -> 155  
"DOGGY" -> [68, 79, 71, 71, 89] -> 378
```

If you do this, you end up with a single number that represents that string - of course, any jumble of those same
letters would have achieved the same hashed number.

```
"ACT" -> [65, 67, 84] -> 155  
"YGGOD" -> [89, 71, 71, 79, 68] -> 378
```

We'll learn a better way to hash strings, but first let's talk about _why_ we want to hash.

### Why Do we Hash?

Let's imagine a scenario:

  * Ada wants to send Babbage a message without Pumpkin changing the contents of the message.
  * When Ada _encrypts_ the message, she's making it confidential so that Pumpkin cannot read it - however, what if Pumpkin decides to mess with the message even if he doesn't know what it says?
  * Perhaps Ada could find a more secure way to send the message, but that could be difficult if it was a very long message (say, a 10MB essay on why dogs rule and cats drool).
  * Instead, Ada can calculate the cryptographic _hash_ of the message and get a single, short number.
  * Then Ada only needs to securely tell Babbage the hashed number, which is not very long at all (they could do so over the phone), and can send the message itself however she wants.
  * Babbage can decrypt Ada's message, hash the result, and then compare the hash code he got from Ada to confirm that the message was received unchanged.
  * But if the hash and the message don't match, Babbage knows that Pumpkin must have tampered with it, and he can let Ada know.

Ideally, all possible string values could be hashed to a unique number. At the same time, we also want a hash number to
be _much_ shorter than the original value. Even if we have a super long string (like, say, the text of an entire book),
the hashed version needs to only be a dozen or so digits. We achieve this by allowing some strings to "collide" with
each other - producing the same hashed number. As long as we use big enough numbers, it's unlikely that any given pair
of strings will collide. In cryptography, we also want a "cryptographically secure" hashing function which is "one-way".
If someone gives you the hashed number, it should be very computationally difficult to calculate the original value.
That way, Pumpkin can't just reverse the hash function.

### How Our Algorithm Works

So, let's break down the math of our better hashing algorithm. We begin by converting our message to a list of integers,
using `ord` and `chr`. Then we have to map a curious formula over each integer to generate a new number:

```
new value = (index + base) ** (old value)
```

This formula will depend on an arbitrarily chosen `base`. For mathematical reasons, we wish to have a prime number -
this makes it harder for someone to reverse our math, since [primes are often difficult to involve in
computations](https://crypto.stackexchange.com/questions/20867/why-are-primes-important-for-encryption). Most real hashing algorithms use a much bigger base, but for now we'll arbitrarily use 31.

The formula also requires an `index`. This will be the position of the character from the original string. So for the
string `"CAT"`, the first letter's index will be `0`, the second letter's index will be `1`, and the third letter will
be `2`.

Remember, we're applying the formula to each element of a string; that's why we want to take position into account.
Then, we have to add the new values together and hash based on a `hash_size`.

```
hashed value = sum(all the new values) % hash_size
```

### An Example

Let's apply this formula to the "CAT" values ([67, 65, 84]) from earlier:

The first (0) element is 67:

```python
print((0+31)**67)
# 8341295116763783101242214530037512645920899177987598203537434247253767513206111213488516390334626911
```

The second (1) element is 65:

```python
print((1+31)**65)
# 68351585149469122636640694597425667667286544715412888638305331450311031224980497600734786781970432
```

The third (2) element is 84:

```python
print((2+31)**84)
# 35906324357811432983835510485410216480190897616731123104932324864582947382402655361077065845208720508790429280946504247030088321
```

Are you seeing how ridiculous big those numbers are? With just a few simple calculations, we're hitting 126 digit
numbers! It's gonna get even crazier next, because now we have to add all those numbers together. In this case, we end
up with:

```
Total Sum = 35906324357811432983835510493819863182104149840609978329567263178171133105105666453252805423912799053221520992035755424146685664
```

Now, the whole goal was to have a short and sweet number. That's where our hash_size parameter comes in. We use modulo
to cut it down to a fixed size, say 10**9 (one billion):

```
= Total Sum % (10**9)  
= 146685664
```

That number right there is our hashed value. If we modified the original string even just a little, we'd end up with a
wildly different value. And because we're modulo-ing, we keep things pretty small in the end.

Hashing is powerful, but a little tricky. It's fine if you don't understand it perfectly yet, you'll have plenty of time
in the future to understand it better. But for now, you need to be able to do it by hand!

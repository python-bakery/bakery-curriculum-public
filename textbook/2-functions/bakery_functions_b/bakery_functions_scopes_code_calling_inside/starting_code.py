from bakery import assert_equal

def improve_message(a_string: str) -> str:
    return a_string.replace('dog', 'doggo')

def combine_messages(first: str, second: str, third: str) -> str:
    return first + '\n' + second + '\n' + third

first = 'That dog is cute.'
second = "I want to pet the dog."
third = "I will ask the dog's owner."
assert_equal(combine_messages(first, second, third),
             ("That doggo is cute.\n"+
              "I want to pet the doggo.\n"+
              "I will ask the doggo's owner."))
from cisc108 import assert_equal

def str_to_list(message: str) -> [int]:
    values = []
    for char in message:
        values.append(ord(char))
    return values    

def rotate_text(ints: [int], rotation: int) -> [int]:
    values = []
    for i in ints:
        values.append( (i+rotation - 32) % 94 + 32)
    return values

def inject_tildes(ints: [int]) ->[int]:
    values = []
    for i in ints:
        values.append(i)
        if i < 48:
            values.append(126)
    return values

def list_to_str(ints: [int]) -> str:
    combined = ""
    for i in ints:
        combined += chr(i)
    return combined

def encrypt_text(message: str, rotation: int) -> str:
    ints = str_to_list(message)
    ints = rotate_text(ints, rotation)
    ints = inject_tildes(ints)
    return list_to_str(ints)


def filter_tildes(ints: [int]) -> [int]:
    values = []
    for i in ints:
        if i != 126:
            values.append(i)
    return values

def decrypt_text(message: str, rotation: int) -> str:
    ints = str_to_list(message)
    ints = filter_tildes(ints)
    ints = rotate_text(ints, -rotation)
    return list_to_str(ints)

def roll_hash(ints: [int], base: int) -> [int]:
    values = []
    index = 0
    for i in ints:
        new = (index + base) ** i
        values.append(new)
        index += 1
    return values

def hash_text(message: str, base: int, hash_size: int) -> int:
    ints = str_to_list(message)
    ints = roll_hash(ints, base)
    total = sum(ints)
    return total % hash_size

def main_error(action: str):
    print("You gave an invalid action:", action)
    
def main_encrypt():
    message = input("What will your message be?")
    encrypted = encrypt_text(message, 4)
    hashed = hash_text(message, 31, 10**9)
    print(encrypted)
    print("Hash:", hashed)

def main_decrypt():
    message = input("What was your message?")
    decrypted = decrypt_text(message, 4)
    print(decrypted)
    expected_hash = hash_text(decrypted, 31, 10**9)
    print("Expected hash:", expected_hash)
    given_hash = int(input("What is your hash?"))
    print("Given hash:", given_hash)
    if given_hash != expected_hash:
        print("There was an error, hashes did not match.")
    else:
        print("Hashes match!")

def main():
    action = input("What do you want to do?")
    if action == "encrypt":
        main_encrypt()
    elif action == "decrypt":
        main_decrypt()
    else:
        main_error(action)
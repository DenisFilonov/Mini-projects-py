import random as rd
import string as st


def generate_password(min_len: int, numbers: bool = True, spec_chars: bool = True) -> str:
    letters = st.ascii_letters
    digits = st.digits
    special = st.punctuation

    characters = letters
    if numbers:
        characters += digits
    if spec_chars:
        characters += special

    password = ""
    validation = False
    has_numbers = False
    has_special = False

    while not validation or len(password) < min_len:
        new_char = rd.choice(characters)
        password += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        validation = True
        if numbers:
            validation = has_numbers
        if spec_chars:
            validation = validation and has_special

    return password


print(generate_password(10))

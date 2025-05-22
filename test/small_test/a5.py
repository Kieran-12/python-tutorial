characters_in_word = []
cap_phrase = []


def show_letters(word):
    characters_in_word.clear()  # Clear list before adding new letters
    for character in word:
        characters_in_word.append(character)


def capitalize_word(word):
    show_letters(word)  # Populate characters_in_word

    if not characters_in_word:  # Avoid errors for empty words
        return ""

    letter = characters_in_word[0]
    ascii_value = ord(letter)

    # Convert only if it's a lowercase letter
    if "a" <= letter <= "z":
        ascii_value -= 32

    capitalized = chr(ascii_value)

    characters_in_word[0] = capitalized  # Replace only the first letter
    return "".join(characters_in_word)  # Convert list back to string


def capitalize_this(s):
    cap_phrase.clear()  # Clear before adding new words
    words = s.split()  # Split the sentence into words

    for word in words:
        capitalized_word = capitalize_word(word)
        cap_phrase.append(capitalized_word)

    return " ".join(cap_phrase)


print(capitalize_this(input()))

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',

                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.', '0':'-----',

                    ',':'--..--', '.':'.-.-.-', '?':'..--..',
                    '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

# Empty List
new_string = []

# Ask user for input
user_input = input("Please Enter, DO NOT type spaces: ")

# Loop through input
for char in user_input:

    # Convert lowercase letters to uppercase
    char = char.upper()
    new_string.append(MORSE_CODE_DICT[char])

    # Check for numbers
    if char is type(int):
        new_string.append(MORSE_CODE_DICT[char])

# Join full response into a string
print(' '.join(new_string))

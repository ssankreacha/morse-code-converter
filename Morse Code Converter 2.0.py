# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',

    ' ': '/'  # Space converted to "/" in Morse
}

# Ask user for input (Allow spaces)
user_input = input("Enter text to convert to Morse Code (spaces allowed): ")

# Convert to Morse Code
morse_code = []
for char in user_input.upper():  # Convert to uppercase
    morse_code.append(MORSE_CODE_DICT.get(char, ''))  # Handle unknown characters

# Join the Morse Code output
converted_text = ' '.join(morse_code).strip()  # Remove extra spaces
print(f"🔠 Input Text: {user_input}")
print(f"📡 Morse Code: {converted_text}")

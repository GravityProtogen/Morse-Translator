import os
# Morse code Dictionary
Morse_Code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", 
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----", ",": "--..--", ".": ".-.-.-", "?": "..--..",
    "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-", " ": "/"
}
# -----------------------------------------------

# Function that removes accents
def remove_accents(input_str):
    accents = "áàâäãåçéèêëíìîïñóòôöõúùûü"
    no_accents = "aaaaaaceeeeiiiinooooouuuu"  # Each accent has a corresponding character

    translation_table = str.maketrans(accents, no_accents)
    return input_str.translate(translation_table)

# -----------------------------------------------

# Function to Encrypt
def Encrypt():
    message = input("Type the message you want to encrypt: ")
    message = remove_accents(message)  # Remove accents
    cypher = ""
    for letter in message.upper():
        if letter in Morse_Code:
            cypher += Morse_Code[letter] + " "  # Space that separates the codes
        else:
            cypher += " "  # 
    return print("Encrypted Morse Code:",cypher.strip())
# -----------------------------------------------

def Decrypt():
    message = input("Type the message you want to decrypt: ")
    message += " "
    decypher = ""
    combination = ""
    i = 0
    for letter in message:
        # verifyes if letter is not space and resets the space count
        if letter != " ":
            i = 0
            combination += letter
        else:
            i += 1 
            # two spaces == new word
            if i == 2:
                decypher += " "
            # morse to character
            elif combination:
                decypher += list(Morse_Code.keys())[list(Morse_Code.values()).index(combination)]
                combination = ""
    return print("Decrypted Morse Code:",decypher)
# -----------------------------------------------

# Commands dict for the input
commands = {
    'encrypt': Encrypt,
    'decrypt': Decrypt,
}
# -----------------------------------------------

# User Area
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    choice = input("Do you want to [Encrypt] or [Decrypt]? you can also [Exit] ").lower()

    if choice in commands:
        os.system('cls' if os.name == 'nt' else 'clear')
        commands[choice]()
    elif choice == "exit":
        break
    else:
        print("Please, choose one of the options listed.")

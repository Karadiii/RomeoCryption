"""
Author: Ido Karadi
Program name: RomeoCryption
Description: Encrypts and decrypts love letters from string into int and vice versa.
Date: 29/10/23
"""


from sys import argv
from bidict import bidict

OP = argv[1].lower()
TABLE = {'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44,
         'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 60, 'P': 61, 'Q': 62, 'R': 63,
         'S': 64, 'T': 65, 'U': 66, 'V': 67, 'W': 68, 'X': 69, 'Y': 10, 'Z': 11, 'a': 12,
         'b': 13, 'c': 14, 'd': 15, 'e': 16, 'f': 17, 'g': 18, 'h': 19, 'i': 30, 'j': 31,
         'k': 32, 'l': 33, 'm': 34, 'n': 35, 'o': 36, 'p': 37, 'q': 38, 'r': 39, 's': 90,
         't': 91, 'u': 92, 'v': 93, 'w': 94, 'x': 95, 'y': 96, 'z': 97, ' ': 98, ',': 99,
         '.': 100, ';': 101, "'": 102, '?': 103, '!': 104, ':': 105}
BITABLE = bidict(TABLE)
ITABLE = BITABLE.inverse


def encrypt():
    """
    Function "encrypt":
    Called when op is "encrypt".
    Encrypts a message into numbers using the hash table (only if it's a love letter).
    Input: user input for message.
    Output: encrypted message as a txt file.
    """
    letter = input("insert love letter\n")
    if "love" not in letter.lower():
        print("not a love letter")
        exit(0)
    encrypted = [TABLE[i] for i in letter]
    with open("encrypted_message.txt", "w") as f:
        f.write(str(encrypted))


def decrypt():
    """
    Function "decrypt":
    Called when op is "decrypt".
    Decrypts a message into text using the inverted hash table.
    Input: message txt file.
    Output: prints decrypted message.
    """
    with open("encrypted_message.txt", "r") as f:
        decrypted = f.readline().replace("]", "").replace("[", "").split(",")
        print(''.join([ITABLE[int(i)] for i in decrypted]))


def main():
    """
    Receives operator from sys.argv[1].
    Calls either encrypt or decrypt based on OP.

    """
    if OP == "encrypt":
        encrypt()
    elif OP == "decrypt":
        decrypt()
    else:
        print('Not a valid command!')


if __name__ == '__main__':
    main()


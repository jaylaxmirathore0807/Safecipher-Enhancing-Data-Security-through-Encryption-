from itertools import cycle

from string import ascii_uppercase as alphabet
# LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(key, plainText):
    plainText = plainText.replace(" ", "").upper()

    offset = ord("A")
    keyChar = cycle(key)
    cipherText = ""

    for character in plainText:
        characterSum = ord(character) + ord(next(keyChar))
        # print("characterSum : ", characterSum)
        characterSumWrapped = characterSum % len(alphabet)
        # print("characterSumWrapped: ", characterSumWrapped)
        tes = chr(characterSumWrapped + offset)
        # print("chr(characterSumWrapped + offset) : ", tes)
        cipherText = cipherText + chr(characterSumWrapped + offset)
        # print("chipertext : ", cipherText)

    return cipherText


def decrypt(key, cipherText):
    cipherText = cipherText.replace(" ", "").upper()

    offset = ord("A")
    keyChar = cycle(key)
    decryptedText = ""

    for character in cipherText:
        characterSum = ord(character) - ord(next(keyChar))
        characterSumWrapped = characterSum % len(alphabet)
        decryptedText = decryptedText + \
            chr(characterSumWrapped + offset)
    return decryptedText

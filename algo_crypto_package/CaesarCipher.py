LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(key, plainText):
    plainText = plainText.replace(" ", "")
    cipherText = ""

    for character in plainText:
        if character.upper() in LETTERS:
            # mencari posisi karakter yang kapital
            if character.isupper():
                position = LETTERS.find(character)
                position = position + key
                # Menjaga jika posisi >= panjang dari LETTERS
                if position >= len(LETTERS):
                    position = position - 26

                # Menambahkan karakter yang dienkripsi
                cipherText += LETTERS[position]

            else:
                position = LETTERS.find(character.upper())
                position = position + key
                # Menjaga jika posisi >= panjang dari LETTERS
                if position >= len(LETTERS):
                    position = position - 26

                # Menambahkan karakter yang dienkripsi
                cipherText = cipherText + LETTERS[position].lower()

        else:
            # Menambahkan karakter tanpa enkripsi
            cipherText = cipherText + character

    return cipherText


def decrypt(key, cipherText):
    cipherText = cipherText.replace(" ", "")
    decryptedText = ""

    for character in cipherText:
        if character.upper() in LETTERS:
            # mencari posisi karakter yang kapital
            if character.isupper():
                position = LETTERS.find(character)
                position = position - key

                # Menjaga jika posisi >= panjang dari LETTERS
                if position < 0:
                    position = position + 26

                # Menambahkan karakter yang dienkripsi
                decryptedText = decryptedText + LETTERS[position]

            else:
                position = LETTERS.find(character.upper())
                position = position - key

                # Menjaga jika posisi >= panjang dari LETTERS
                if position < 0:
                    position = position + 26

                # Menambahkan karakter yang dienkripsi
                decryptedText = decryptedText + LETTERS[position].lower()

        else:
            # Menambahkan karakter tanpa enkripsi
            decryptedText = decryptedText + character

    return decryptedText

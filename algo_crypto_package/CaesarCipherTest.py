import CaesarCipher


def run_test():
    key = 4

    plainText = "HELLO"
    cipherText = CaesarCipher.encrypt(key, plainText)
    decryptedText = CaesarCipher.decrypt(key, cipherText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    print("decryptedtext: " + decryptedText + "\n")

    plainText = "BELAJAR KRIPTOGRAFI UNTUK INDONESIA MERDEKA"
    cipherText = CaesarCipher.encrypt(key, plainText)
    decryptedText = CaesarCipher.decrypt(key, cipherText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    print("decryptedtext: " + decryptedText + "\n")

    plainText = "Hello123+/="
    cipherText = CaesarCipher.encrypt(key, plainText)
    decryptedText = CaesarCipher.decrypt(key, cipherText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    print("decryptedtext: " + decryptedText + "\n")

    plainText = "belajar KRIPTOGRAFI untuk INDONESIA merdeka"
    cipherText = CaesarCipher.encrypt(key, plainText)
    decryptedText = CaesarCipher.decrypt(key, cipherText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    print("decryptedtext: " + decryptedText + "\n")

    plainText = "BeLajaR KRIPTOGRAFI untuk INDONESIA merdeka"
    cipherText = CaesarCipher.encrypt(key, plainText)
    decryptedText = CaesarCipher.decrypt(key, cipherText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    print("decryptedtext: " + decryptedText + "\n")
    return


if __name__ == "__main__":
    run_test()

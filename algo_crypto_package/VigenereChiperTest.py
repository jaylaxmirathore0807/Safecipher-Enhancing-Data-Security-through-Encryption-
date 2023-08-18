import VigenereCipher


def run_test():

    key = "INFORMATIKA"

    plainText = "BELAJAR KRIPTOGRAFI UNTUK INDONESIA MERDEKA"
    cipherText = VigenereCipher.encrypt(key, plainText)
    # decryptedText = VigenereCipher.decrypt(key, cipherText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    # print("decryptedtext: " + decryptedText + "\n")

    # plainText = "belajar krptiografi untuk indonesia merdeka"
    # cipherText = VigenereCipher.encrypt(key, plainText)
    # decryptedText = VigenereCipher.decrypt(key, cipherText)

    # print("plaintext: " + plainText)
    # print("ciphertext: " + cipherText)
    # print("decryptedtext: " + decryptedText + "\n")

    # plainText = "BeLajaR KRIPTOGRAFI untuk INDONESIA merdeka"
    # cipherText = VigenereCipher.encrypt(key, plainText)
    # decryptedText = VigenereCipher.decrypt(key, cipherText)

    # print("plaintext: " + plainText)
    # print("ciphertext: " + cipherText)
    # print("decryptedtext: " + decryptedText + "\n")

    # plainText = "belajar KRIPTOGRAFI untuk INDONESIA merdeka"
    # cipherText = VigenereCipher.encrypt(key, plainText)
    # decryptedText = VigenereCipher.decrypt(key, cipherText)

    # print("plaintext: " + plainText)
    # print("ciphertext: " + cipherText)
    # print("decryptedtext: " + decryptedText + "\n")

    return


if __name__ == "__main__":
    run_test()

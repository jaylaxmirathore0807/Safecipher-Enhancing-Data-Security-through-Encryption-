import CaesarCipher
import RailFence
import VigenereCipher


def run_test():
    key2 = "INFORMATIKA"
    key1 = 2

    plainText = "BELAJAR KRIPTOGRAFI UNTUK INDONESIA MERDEKA"

    cipherText = CaesarCipher.encrypt(key1, plainText)
    cipherText = RailFence.encrypt(cipherText, key1)
    cipherText = VigenereCipher.encrypt(key2, cipherText)

    decryptedText = VigenereCipher.decrypt(key2, cipherText)
    decryptedText = RailFence.decrypt(decryptedText, key1)
    decryptedText = CaesarCipher.decrypt(key1, decryptedText)

    print("plaintext: " + plainText)
    print("ciphertext: " + cipherText)
    print("decryptedtext: " + decryptedText + "\n")

    return


if __name__ == "__main__":
    run_test()

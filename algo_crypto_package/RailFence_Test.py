
import RailFence


def run_test():

    plaintext = "BELAJAR KRIPTOGRAFI UNTUK INDONESIA MERDEKA"     # Q1, Q2
    cipher_text = RailFence.encrypt(plaintext, 4)
    decrypted_text = RailFence.decrypt(cipher_text, 4)
    print("plaintext: " + plaintext)
    print("ciphertext: " + cipher_text)
    print("Key: 4")
    print("decryptedtext: " + decrypted_text + "\n")

    plaintext = "Hello!"    # Q1, Q2
    cipher_text = RailFence.encrypt(plaintext, 3)
    decrypted_text = RailFence.decrypt(cipher_text, 3)
    print("plaintext: " + plaintext)
    print("ciphertext: " + cipher_text)
    print("Key: 3")
    print("decryptedtext: " + decrypted_text + "\n")

    plaintext = "Hello123+/="   # Q3
    cipher_text = RailFence.encrypt(plaintext, 5)
    decrypted_text = RailFence.decrypt(cipher_text, 5)
    print("plaintext: " + plaintext)
    print("ciphertext: " + cipher_text)
    print("Key: 5")
    print("decryptedtext: " + decrypted_text + "\n")

    return


if __name__ == "__main__":
    run_test()

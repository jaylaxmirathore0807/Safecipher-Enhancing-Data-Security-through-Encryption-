from flask import Flask, render_template, request, jsonify
from algo_crypto_package import CaesarCipher, RailFence, VigenereCipher

app = Flask(__name__, template_folder='templates')


@app.route("/")
def Caesar():
    return render_template("caesar.html")


@app.route("/super/")
def Super():
    return render_template("super.html")


@app.route("/api/super/", methods=["POST"])
def super_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text = data["text"]
    key1 = int(data["key1"])
    key2 = int(data["key2"])
    key3 = data["key3"]
    if operation == "encrypt":
        cipherText = CaesarCipher.encrypt(key1, text)
        cipherText = RailFence.encrypt(cipherText, key2)
        cipherText = VigenereCipher.encrypt(key3, cipherText)
        return jsonify({"output": cipherText})
    else:
        decryptedText = VigenereCipher.decrypt(key3, text)
        decryptedText = RailFence.decrypt(decryptedText, key2)
        decryptedText = CaesarCipher.decrypt(key1, decryptedText)
        return jsonify({"output": decryptedText})


if __name__ == "__main__":
    app.run(debug=True)

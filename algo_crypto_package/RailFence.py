def encrypt(plainText, key):
    plainText = plainText.replace(" ", "")
    # Membuat matriks untuk cipher
    # key = rows
    # length(text) = columns
    # Mengisi jalur(rail) matriks
    # Untuk membedakan yang sudah terisi
    # dari yang masih kosong
    rail = [["\n" for i in range(len(plainText))] for j in range(key)]
    directionDown = False
    row, col = 0, 0
    for i in range(len(plainText)):
        # Cek arah aliran
        # balik arah jika sudah mengisi
        # jalur atas atau bawah
        if row == 0 or row == key-1:
            directionDown = not directionDown

        # mengisi alphabet pada plainteks
        rail[row][col] = plainText[i]
        col += 1

        # mencari baris berikutnya dengan
        # direction flag
        if directionDown:
            row = row + 1
            # print("ya", directionDown)
        else:
            row = row - 1
            # print("tidak", directionDown)

    # Konstruksi cipher dengan rail matriks
    result = []

    for i in range(key):
        for j in range(len(plainText)):
            if rail[i][j] != "\n":
                result.append(rail[i][j])

    cipherText = "".join(result)
    return cipherText


def decrypt(cipherText, key):
    cipherText = cipherText.replace(" ", "")

    # Membuat matriks untuk cipher
    # key = rows
    # length(cipherText) = columns
    # Mengisi jalur(rail) matriks
    # Untuk membedakan yang sudah terisi
    # dari yang masih kosong
    rail = [["\n" for i in range(len(cipherText))] for j in range(key)]

    # Mencari arah
    directionDown = None
    row, col = 0, 0
    # taruh tanda dengan '*'
    for i in range(len(cipherText)):
        if row == 0:
            directionDown = True
        if row == key-1:
            directionDown = False

        # taruh penanda
        rail[row][col] = "*"
        col += 1

        # cari baris selanjutnya
        # dengan direction flag
        if directionDown:
            row = row + 1
        else:
            row = row - 1

    # Konstruksi cipher dengan rail matriks
    # isi rail matriks
    index = 0
    for i in range(key):
        for j in range(len(cipherText)):
            if rail[i][j] == "*" and index < len(cipherText):
                rail[i][j] = cipherText[index]
                # print(rail[i][j], i, j)
                index = index + 1
    result = []
    row, col = 0, 0

    for i in range(len(cipherText)):
        # Cek arah aliran
        if row == 0:
            directionDown = True
        if row == key - 1:
            directionDown = False

        # Taruh penanda
        if rail[row][col] != "*":
            result.append(rail[row][col])
            # print(result)
            col = col + 1

        # cari baris selanjutnya
        # dengan direction flag
        if directionDown:
            row = row + 1
        else:
            row = row - 1

    plainText = "".join(result)
    return plainText

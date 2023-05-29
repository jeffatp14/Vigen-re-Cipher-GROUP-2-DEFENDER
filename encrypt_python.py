def vigenereEncrypt(data, key):
    dataLength = len(data)
    keyLength = len(key)
    encryptedData = ""

    for i in range(dataLength):
        dataChar = data[i].lower()
        keyChar = key[i % keyLength].lower()

        if dataChar.isalnum():
            if dataChar.isdigit():
                dataChar = int(dataChar)
            else:
                dataChar = ord(dataChar) - ord('a') + 10

            if keyChar.isdigit():
                keyChar = int(keyChar)
            else:
                keyChar = ord(keyChar) - ord('a') + 10

            encryptedChar = (dataChar + keyChar) % 36

            if encryptedChar < 10:
                encryptedChar = str(encryptedChar)
            else:
                encryptedChar = chr(encryptedChar + ord('a') - 10)

            encryptedData += encryptedChar
        else:
            encryptedData += dataChar

    return encryptedData


def encryptString(plaintext, key):
    encryptedData = vigenereEncrypt(plaintext, key)
    return encryptedData

# Example usage
inputFile = 'plaintext.txt'
outputFile = 'encrypted.txt'
encryptionKey = 'santa132'

# Read plaintext from input file
with open(inputFile, 'r') as file:
    plaintext = file.read().strip()

# Encrypt the plaintext
encryptedText = encryptString(plaintext, encryptionKey)

# Write encrypted text to output file
with open(outputFile, 'w') as file:
    file.write(encryptedText)

print("Encryption complete. Encrypted text written to", outputFile)

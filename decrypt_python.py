def vigenereDecrypt(encryptedData, key):
    dataLength = len(encryptedData)
    keyLength = len(key)
    decryptedData = ""
    keyIndex = 0

    for i in range(dataLength):
        encryptedChar = encryptedData[i].lower()
        keyChar = key[keyIndex % keyLength].lower()

        if encryptedChar.isalnum():
            if encryptedChar.isdigit():
                encryptedChar = int(encryptedChar)
            else:
                encryptedChar = ord(encryptedChar) - ord('a') + 10

            if keyChar.isdigit():
                keyChar = int(keyChar)
            else:
                keyChar = ord(keyChar) - ord('a') + 10

            decryptedChar = (encryptedChar - keyChar) % 36

            if decryptedChar < 10:
                decryptedChar = str(decryptedChar)
            else:
                decryptedChar = chr(decryptedChar + ord('a') - 10)

            decryptedData += decryptedChar
        else:
            decryptedData += encryptedChar

        if encryptedChar == '\n':
            keyIndex = 0  # Reset the key index for a new line
        else:
            keyIndex += 1

    return decryptedData


def decryptString(encryptedText, key):
    decryptedData = vigenereDecrypt(encryptedText, key)
    return decryptedData


inputFile = 'encrypted.txt'
outputFile = 'decrypted.txt'
encryptionKey = 'santa132'

# Read encrypted text from input file
with open(inputFile, 'r') as file:
    encryptedText = file.read().strip()

# Decrypt the encrypted text
decryptedData = decryptString(encryptedText, encryptionKey)

# Write decrypted data to output file
with open(outputFile, 'w') as file:
    file.write(decryptedData)

print("Decryption complete. Decrypted data written to", outputFile)

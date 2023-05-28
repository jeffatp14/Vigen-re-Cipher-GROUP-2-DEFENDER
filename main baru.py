def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

def write_file(filename, lines):
    with open(filename, "w") as file:
        file.writelines(lines)

def add_line(lines):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    new_line = f"{name},{phone}\n"
    lines.append(new_line)
    print("Line added successfully.")

def display_lines(lines):
    for line in lines:
        print(line.strip())

def update_line(lines):
    display_lines(lines)
    line_number = int(input("Enter the line number to update: "))
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return

    name = input("Enter the updated name: ")
    phone = input("Enter the updated phone number: ")
    updated_line = f"{name},{phone}\n"
    lines[line_number - 1] = updated_line
    print("Line updated successfully.")

def delete_line(lines):
    display_lines(lines)
    line_number = int(input("Enter the line number to delete: "))
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return

    del lines[line_number - 1]
    print("Line deleted successfully.")

def display_menu():
    print("1. Add a new line")
    print("2. Read all lines")
    print("3. Update a specific line")
    print("4. Delete a specific line")
    print("5. Exit")

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


def vigenereDecrypt(encryptedData, key):
    dataLength = len(encryptedData)
    keyLength = len(key)
    decryptedData = ""

    for i in range(dataLength):
        encryptedChar = encryptedData[i].lower()
        keyChar = key[i % keyLength].lower()

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

    return decryptedData


def encryptString(plaintext, key):
    encryptedData = vigenereEncrypt(plaintext, key)
    return encryptedData


def decryptString(encryptedText, key):
    decryptedData = vigenereDecrypt(encryptedText, key)
    return decryptedData


def main():
    filename = input("Enter the file name: ")
    is_encrypted = input("Is the file encrypted? (y/n): ")

    if is_encrypted.lower() == "y":
        encryptionKey = input("Enter the decryption key: ")
        encryptedLines = read_file(filename)
        decryptedLines = [decryptString(line.strip(), encryptionKey) for line in encryptedLines]
        lines = decryptedLines
        print("Decryption complete.")
    else:
        lines = read_file(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_line(lines)
        elif choice == "2":
            display_lines(lines)
        elif choice == "3":
            update_line(lines)
        elif choice == "4":
            delete_line(lines)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

    should_export = input("Do you want to export the file? (y/n): ")
    if should_export.lower() == "y":
        export_menu(lines, filename)

    if is_encrypted.lower() == "y":
        should_encrypt = input("Do you want to encrypt the data before exporting? (y/n): ")
        if should_encrypt.lower() == "y":
            encryptionKey = input("Enter the encryption key: ")
            encryptedLines = [encryptString(line.strip(), encryptionKey) for line in lines]
            write_file(filename, encryptedLines)
            print("Encryption and export complete.")
        else:
            write_file(filename, lines)
            print("Export complete.")
    else:
        write_file(filename, lines)
        print("Export complete.")


def export_menu(lines, filename):
    should_encrypt = input("Do you want to encrypt the data before exporting? (y/n): ")
    if should_encrypt.lower() == "y":
        encryptionKey = input("Enter the encryption key: ")
        encryptedLines = [encryptString(line.strip(), encryptionKey) for line in lines]
        write_file(filename, encryptedLines)
        print("Encryption and export complete.")
    else:
        write_file(filename, lines)
        print("Export complete.")


if __name__ == "__main__":
    main()

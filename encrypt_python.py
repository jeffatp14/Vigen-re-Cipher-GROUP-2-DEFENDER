def encrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[key_index]) - ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(keyword)
        elif char.isdigit():
            base = ord('0')
            shift = ord(keyword[key_index]) - ord('A')
            encrypted_digit = chr((ord(char) - base + shift) % 10 + base)
            ciphertext += encrypted_digit
            key_index = (key_index + 1) % len(keyword)
        else:
            ciphertext += char

    return ciphertext


def encrypt_file_vigenere(file_path, keyword):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        encrypted_lines = []
        for line in lines:
            line = line.strip()
            if ',' in line:
                name, phone = line.split(',', 1)
                encrypted_name = encrypt_vigenere(name, keyword)
                encrypted_phone = encrypt_vigenere(phone, keyword)
                encrypted_line = f"{encrypted_name},{encrypted_phone}"
                encrypted_lines.append(encrypted_line)
            else:
                encrypted_lines.append(line)

        with open(file_path, 'w') as file:
            file.write('\n'.join(encrypted_lines))

        print("File encrypted successfully.")
    except IOError:
        print("Error: File not found or could not be accessed.")


file_path = "capekdh.txt"
keyword = "santa132"

# Encrypt the file
encrypt_file_vigenere(file_path, keyword)
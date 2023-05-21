
def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[key_index]) - ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(keyword)
        elif char.isdigit():
            base = ord('0')
            shift = ord(keyword[key_index]) - ord('A')
            decrypted_digit = chr((ord(char) - base - shift) % 10 + base)
            plaintext += decrypted_digit
            key_index = (key_index + 1) % len(keyword)
        else:
            plaintext += char

    return plaintext


def decrypt_file_vigenere(file_path, keyword):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        decrypted_lines = []
        for line in lines:
            line = line.strip()
            if ',' in line:
                encrypted_name, encrypted_phone = line.split(',', 1)
                decrypted_name = decrypt_vigenere(encrypted_name, keyword)
                decrypted_phone = decrypt_vigenere(encrypted_phone, keyword)
                decrypted_line = f"{decrypted_name},{decrypted_phone}"
                decrypted_lines.append(decrypted_line)
            else:
                decrypted_lines.append(line)

        with open(file_path, 'w') as file:
            file.write('\n'.join(decrypted_lines))

        print("File decrypted successfully.")
    except IOError:
        print("Error: File not found or could not be accessed.")


# Example usage
file_path = "capekdh.txt"
keyword = "santa132"

# Decrypt the file
decrypt_file_vigenere(file_path, keyword)

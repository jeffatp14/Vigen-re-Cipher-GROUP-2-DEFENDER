#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_SIZE 100
#define MAX_NAME_SIZE 50
#define MAX_PHONE_SIZE 20

void generateKey(char *str, char *key, int keyLength);
void encryptData(char *data, char *key);
void decryptData(char *data, char *key);

void generateKey(char *str, char *key, int keyLength)
{
    int strLength = strlen(str);
    int i, j = 0;

    for (i = 0; i < strLength; ++i)
    {
        key[i] = key[j];
        j = (j + 1) % keyLength;
    }
    key[i] = '\0';
}

void encryptData(char *data, char *key)
{
    int dataLength = strlen(data);
    int keyLength = strlen(key);

    for (int i = 0; i < dataLength; i++)
    {
        char dataChar = toupper(data[i]);
        char keyChar = toupper(key[i % keyLength]);

        // Convert to the range 0-35
        if (isalnum(dataChar))
        {
            if (isdigit(dataChar))
                dataChar -= '0';
            else
                dataChar -= 'A' - 10;

            if (isdigit(keyChar))
                keyChar -= '0';
            else
                keyChar -= 'A' - 10;

            // Perform encryption using Vigenere algorithm
            char encryptedChar = (dataChar + keyChar) % 36;

            // Convert back to ASCII representation
            if (encryptedChar < 10)
                encryptedChar += '0';
            else
                encryptedChar += 'A' - 10;

            // Update the data
            data[i] = encryptedChar;
        }
    }
}

void decryptData(char *data, char *key)
{
    int dataLength = strlen(data);
    int keyLength = strlen(key);

    for (int i = 0; i < dataLength; i++)
    {
        char dataChar = toupper(data[i]);
        char keyChar = toupper(key[i % keyLength]);

        // Convert to the range 0-35
        if (isalnum(dataChar))
        {
            if (isdigit(dataChar))
                dataChar -= '0';
            else
                dataChar -= 'A' - 10;

            if (isdigit(keyChar))
                keyChar -= '0';
            else
                keyChar -= 'A' - 10;

            // Perform decryption using Vigenere algorithm
            char decryptedChar = (dataChar - keyChar + 36) % 36;

            // Convert back to ASCII representation
            if (decryptedChar < 10)
                decryptedChar += '0';
            else
                decryptedChar += 'A' - 10;

            // Convert to lowercase
            decryptedChar = tolower(decryptedChar);

            // Update the data
            data[i] = decryptedChar;
        }
    }
}

int main()
{
    char data[MAX_SIZE][MAX_NAME_SIZE + MAX_PHONE_SIZE + 1];
    int rowCount;

    printf("Enter the number of rows: ");
    scanf("%d%*c", &rowCount); // Skip the newline character

    if (rowCount > MAX_SIZE)
    {
        printf("Error: Maximum row count exceeded.\n");
        return 1;
    }

    printf("Enter the data in the format 'name,phone':\n");
    for (int i = 0; i < rowCount; i++)
    {
        printf("Row %d: ", i + 1);
        scanf("%[^,\n]%*c", data[i]); // Read until the comma (,) or newline character
    }

    char key[9] = "santa132";

    // Encrypt the data
    for (int i = 0; i < rowCount; i++)
    {
        encryptData(data[i], key);
    }

    // Print the encrypted data
    printf("\nEncrypted Data:\n");
    for (int i = 0; i < rowCount; i++)
    {
        printf("%s\n", data[i]);
    }

    // Decrypt the data
    for (int i = 0; i < rowCount; i++)
    {
        decryptData(data[i], key);
    }

    // Print the decrypted data
    printf("\nDecrypted Data:\n");
    for (int i = 0; i < rowCount; i++)
    {
        printf("%s\n", data[i]);
    }

    return 0;
}


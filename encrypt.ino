#include <ctype.h>
#include <string.h>

#define MAX_SIZE 100
#define MAX_NAME_SIZE 50
#define MAX_PHONE_SIZE 20

void generateKey(char *str, char *key, int keyLength);
void encryptData(char *data, char *key);

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
    char dataChar = tolower(data[i]);
    char keyChar = tolower(key[i % keyLength]);

    // Convert to the range 0-35
    if (isalnum(dataChar))
    {
      if (isdigit(dataChar))
        dataChar -= '0';
      else
        dataChar -= 'a' - 10;

      if (isdigit(keyChar))
        keyChar -= '0';
      else
        keyChar -= 'a' - 10;

      // Perform encryption using Vigenere algorithm
      char encryptedChar = (dataChar + keyChar) % 36;

      // Convert back to ASCII representation
      if (encryptedChar < 10)
        encryptedChar += '0';
      else
        encryptedChar += 'a' - 10;

      // Update the data
      data[i] = encryptedChar;
    }
  }
}

void setup()
{
  Serial.begin(9600);

  char data[MAX_SIZE][MAX_NAME_SIZE + MAX_PHONE_SIZE + 1];
  int rowCount;

  Serial.print("Enter the number of rows: ");
  while (!Serial.available())
    ; // Wait for user input

  rowCount = Serial.parseInt();
  Serial.read(); // Read the newline character

  if (rowCount > MAX_SIZE)
  {
    Serial.println("Error: Maximum row count exceeded.");
    return;
  }

  Serial.println("Enter the data in the format 'name,phone':");
  for (int i = 0; i < rowCount; i++)
  {
    Serial.print("Row ");
    Serial.print(i + 1);
    Serial.print(": ");

    while (!Serial.available())
      ; // Wait for user input

    int bytesRead = Serial.readBytesUntil('\n', data[i], MAX_NAME_SIZE + MAX_PHONE_SIZE + 1);
    data[i][bytesRead] = '\0'; // Null-terminate the string
  }

  char key[9] = "santa132";

  // Encrypt the data
  for (int i = 0; i < rowCount; i++)
  {
    encryptData(data[i], key);
  }

  // Print the encrypted data
  Serial.println("\nEncrypted Data:");
  for (int i = 0; i < rowCount; i++)
  {
    Serial.println(data[i]);
  }
}

void loop()
{
  // Your code here
}



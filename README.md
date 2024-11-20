# PRODIGY_CS_01
This program is an implementation of the Caesar Cipher encryption and decryption technique. It provides a simple way to encrypt and decrypt messages by shifting the letters of the alphabet by a specified number of places. Below is an explanation of how the program works:

Steps:
Welcome Message
The program starts by displaying a welcome message:
"=== Caesar Cipher Program ==="

User Choice
The program prompts the user to choose an option:

(E) for Encrypting a message
(D) for Decrypting a message
The user's input is converted to uppercase (.upper()) to ensure it's case-insensitive. If the input is invalid (not 'E' or 'D'), the program displays an error message and restarts the choice process.

Input Message and Shift Value
The user is asked to input:

The message they want to encrypt or decrypt.
The shift value (an integer) that determines how many positions each letter will be shifted.
Processing the Message
The program iterates through each character in the input message:

It checks if the character is a letter (alphabetic) using char.isalpha().
If the character is a letter:
The base ASCII value is determined:
65 for uppercase letters ('A' to 'Z').
97 for lowercase letters ('a' to 'z').
Depending on the user's choice:
Encrypt (E): The program shifts the character forward by the shift value.
Decrypt (D): The program shifts the character backward by the shift value.
The new character is calculated using the formula:
chr((ord(char) - base ± shift) % 26 + base)
This ensures the character wraps around the alphabet (e.g., 'Z' becomes 'A' for encryption and vice versa).
If the character is not a letter (e.g., a number or punctuation), it is added to the result unchanged.
Displaying the Result
Once all characters are processed, the final encrypted or decrypted message is displayed:
"Processed Message: <result>"

Repeat or Exit
The program asks the user if they want to perform another operation:

If the user enters 'y', the program restarts.
If the user enters anything else, the program thanks the user and exits.
Exit Message
The program ends with the message:
"Thank you for using the Caesar Cipher Program. Goodbye!"

Example of Usage:
Encrypt a Message:
Input:
Choice: E
Message: HELLO
Shift: 3
Output:
Processed Message: KHOOR
Decrypt a Message:
Input:
Choice: D
Message: KHOOR
Shift: 3
Output:
Processed Message: HELLO

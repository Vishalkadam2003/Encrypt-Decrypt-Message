# Encrypt-Decrypt-Message
Project Overview
This is a simple implementation of the Caesar Cipher algorithm using Python.
The Caesar Cipher is one of the oldest and simplest encryption techniques, 
which shifts each letter in the input message by a fixed number of positions in the alphabet. 
This project allows the user to both encrypt (encode) and decrypt (decode) messages.

 Features
Encrypt (encode) any text message.
Decrypt (decode) any previously encoded message.
Supports handling of special characters, numbers, and symbols without modification.
Allows multiple attempts for encoding/decoding until the user decides to exit.

 How It Works
User provides the message to be encoded or decoded.
The user specifies the shift value, which determines how many positions each letter in the message will be shifted.
The user chooses whether they want to encode (encrypt) or decode (decrypt) the message.
The script processes each letter:
Alphabets are shifted based on the shift value.
Numbers and symbols remain unchanged.
Displays the final encrypted or decrypted message to the user.
Prompts the user if they want to run the cipher again.

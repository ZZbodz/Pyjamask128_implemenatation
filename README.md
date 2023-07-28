## Pyjamask-128 Implementation: Encryption and Decryption in a Client-Server Application

This project showcases the implementation of Pyjamask-128 encryption and decryption in a Client-Server application. Pyjamask-128 is a cryptographic algorithm designed to secure data, and its detailed workings can be found in the provided PDF.

### How to Run

1. Open two terminals in the current repository.
2. In the first terminal, execute the following command to start the server:


The server will now be ready to listen for incoming clients on the specified port mentioned in the code.

3. In the second terminal, run the following command to initiate the client application:


Follow the prompts in the client application:
- To perform encryption:
  - Enter option "1" for the encryption process.
  - Input the plain text that you wish to encrypt.
  - Provide a 16-character hexadecimal key (e.g., 123456789abcdef) to use for encryption.
  - The server will respond by sending the encrypted text back to the client.

- To perform decryption:
  - Enter option "2" for the decryption process.
  - Input the cipher text in binary form with 128 bits that you want to decrypt.
  - Enter the 16-character hexadecimal key used for encryption to decrypt the text.
  - The server will respond by sending the decrypted text back to the client.

### Purpose

This project serves as a practical example of Pyjamask-128 encryption and decryption, demonstrating how this cryptographic algorithm can be utilized for secure data communication between a client and server. By running the client-server application and following the provided steps, users can observe the encryption and decryption process in action.

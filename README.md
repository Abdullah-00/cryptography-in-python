#Cryptography Using Python

This is an assignment of ICS444 (Computer & Network Security) course. The assignment is about using existing libraries to carry out cryptographic operations
in python language. It consists of 7 parts as follows:
- **Part 1.1:** Using SHA512 to compute a message digest
- **Part 1.2:** Using MD5 and RSA to generate a digital signature and save the public key (encoded)
- **Part 1.3:** Verifying the generated signature above using the public key
- **Part 1.4:** Using AES to encrypt a message and save the cipher and the key to a file
- **Part 1.5:** Decrypting the generated cipher from above
- **Part 1.6:** Implementing a program to allow two parties to agree on a symmetric key using Diffie-Hellman
- **Part 2.1:** Implementing GUI program allowing two parties (a client and a
server) to exchange a file securely. The client and the server start by agreeing
on a symmetric key using Diffie-Hellman. Then, the client encrypts the file and sends it.
Finally, the server, after receiving the data, decrypts it and prints the content of the file.

##Environment Configuration:
- **OS:** Ubuntu Server 14.04.5 LTS
- **Programing Language:** Python 3.4.3
- **Libraries:**
    * pycrypto==2.6.1
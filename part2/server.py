import socket
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

HOST = '127.0.0.1'  # localhost
PORT = 8000        # Port to listen on
base = 2  # This is 'g'
prime = 13  # This is 'p'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for client to connect...")
    conn, _ = s.accept()
    with conn:
        print("Client successfully connected")
        print("The shared prime and base are as follows:\n\tp = 13,\tg = 2")
        while True:
            r1 = conn.recv(1024)  # Receiving R1 from client
            if not r1:
                break

            # Asking Server to choose 'y'
            # Taking Server input for 'y'
            key = int(input("\n\nEnter your secret 'y': "))  # This holds Server secret 'y'
            # Computing R2, R2 = g^y mod p
            r2 = (base ** key) % prime  # R2

            # Now, Server will send R2 to Client
            conn.sendall(str.encode(str(r2)))

            r1 = int(r1.decode())  # Converting R1 back to integer
            k = (r1 ** key) % prime  # This is the shared key
            key = k.to_bytes(16, byteorder='little')  # This key will be used to decrypt the message

            print("K = " + str(k))

            f = open('recvFile.txt', 'wb')
            print("Server is receiving some data...")

            iv = conn.recv(4096)
            conn.sendall(b'recv')
            cipherText = conn.recv(4096)
            f.write(cipherText)
            print("Finished receiving")
            print("Cipher text:\n" + str(cipherText))
            print("\nDecrypting the cipher text...")

            cipher = AES.new(key, AES.MODE_CBC, iv)  # Creating a new AES object using the random key and operating in CBC mode
            message = cipher.decrypt(cipherText)  # Decrypting the cipher text
            message = unpad(message, AES.block_size)  # Removing the padding from the original message
            print("\nThe decrypted message is: \n" + message.decode())

            f.close()

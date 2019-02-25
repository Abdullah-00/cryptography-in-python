import socket
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8000        # The port used by the server
base = 2  # This is 'g'
prime = 13  # This is 'p'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Announcing the public 'g' and 'p'
    print("The shared prime and base are as follows:\n\tp = 13,\tg = 2")

    # Asking Client to choose 'x'
    # Taking Client input for 'x'
    key = int(input("\n\nEnter your secret 'x': "))  # This holds Client secret 'x'
    # Computing R1, R1 = g^x mod p
    r1 = (base ** key) % prime  # R1

    # Now, Client will send R1 to Server
    s.sendall(str.encode(str(r1)))

    r2 = s.recv(1024)  # Receiving R2 from server
    r2 = int(r2.decode())  # Converting R2 back to integer

    k = (r2 ** key) % prime  # This is the shared key

    print("K = " + str(k))

    f = open('message.txt', 'r')  # Open the file containing the message for read
    message = f.read()  # Read the message
    f.close()
    messageInByte = str.encode(message)  # Encode the message to bytes (the API accept text encoded in bytes)
    key = k.to_bytes(16, byteorder='little')  # This key will be used to encrypt the message
    cipher = AES.new(key, AES.MODE_CBC)  # Creating a new AES object using the random key and operating in CBC mode
    messageInByte = pad(messageInByte, AES.block_size)  # Padding the message to make its length a multiple of 16 bytes
    cipherText = cipher.encrypt(messageInByte)  # Encrypting the padded message

    print("Client is sending some data...")
    s.sendall(cipher.iv)
    data = s.recv(1024)
    s.sendall(cipherText)

    print("Finished sending")

    f = open('message.txt', 'r')
    message = f.read()


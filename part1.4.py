from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad
if __name__ == '__main__':
    f = open('message.txt', 'r')  # Open the file containing the message for read
    message = f.read()  # Read the message
    messageInByte = str.encode(message)  # Encode the message to bytes (the API accept text encoded in bytes)
    key = get_random_bytes(16)  # This key will be used to encrypt the message
    cipher = AES.new(key, AES.MODE_CBC)  # Creating a new AES object using the random key and operating in CBC mode
    messageInByte = pad(messageInByte, AES.block_size)  # Padding the message to make its length a multiple of 16 bytes
    cipherText = cipher.encrypt(messageInByte)  # Encrypting the padded message
    cipherFile = open("cipherText.txt", "wb")  # Creating a file to save the cipher text
    cipherFile.write(cipherText)  # Writing the cipher text to the file
    cipherFile.close()
    print("Cipher text saved to 'cipherText.txt'.")
    keyFile = open("secKey.txt", 'wb')  # Creating a file to save the secret key
    keyFile.write(key)  # Writing the secret key to the file
    keyFile.close()
    print("Secret key saved to 'secKey.txt'.")
    ivFile = open('iv.txt', 'wb')  # Creating a file to save the IV
    ivFile.write(cipher.iv)  # Writing the IV to the file
    ivFile.close()
    print("IV saved to 'iv.txt'.")

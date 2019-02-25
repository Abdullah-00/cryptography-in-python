# *** Important Note: This part should be executed only after executing 'part1.4.py' ***
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
if __name__ == '__main__':
    cipherFile = open('cipherText.txt', 'rb')  # Opening the file containing the cipher text for read
    cipherText = cipherFile.read()  # Reading the cipher text
    keyFile = open('secKey.txt', 'rb')  # Opening the file containing the secret key for read
    key = keyFile.read()  # Reading the secret key
    ivFile = open('iv.txt', 'rb')  # Opening the file containing the IV for read
    iv = ivFile.read()  # Reading the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Creating a new AES object using the random key and operating in CBC mode
    message = cipher.decrypt(cipherText)  # Decrypting the cipher text
    message = unpad(message, AES.block_size)  # Removing the padding from the original message
    print("The decrypted message is: \n" + message.decode())

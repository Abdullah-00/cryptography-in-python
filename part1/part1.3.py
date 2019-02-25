# *** Important Note: This part should be executed only after executing 'part1.2.py' ***
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_PSS
from Cryptodome.Hash import MD5

if __name__ == '__main__':
    # Verifying the Signature Generated From part1.2
    keyFile = open('pubKey.pem', 'r')  # Open the file containing the public key
    pubKey = RSA.import_key(keyFile.read())  # Importing the public key from the file created in the previous part
    verifier = PKCS1_PSS.new(pubKey)  # Creating a verifier with the public key
    messageFile = open('message.txt', 'r')  # Open the file containing the message for read
    message = messageFile.read()  # Read the message
    messageInByte = str.encode(message)  # Encode the message to bytes (the API accept text encoded in bytes)
    md5Hash = MD5.new(messageInByte)  # Generate the MD5 hash of the message
    signFile = open('signature.txt', 'rb')  # Open the file containing the signature for read
    signature = signFile.read()  # Saving the signature
    isAuth = verifier.verify(md5Hash, signature)  # Checking wether the signature is authentic or not
    if (isAuth):
        print("The signature is authentic.")
    else:
        print("The signature is not authentic.")
    # Finished Verifying

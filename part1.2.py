from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_PSS
from Cryptodome.Hash import MD5

if __name__ == '__main__':
    # Generating RSA Key Pair:
    key = RSA.generate(2048)  # Generate a key pair
    pubKey = key.publickey().export_key('PEM')  # Export the public key as encoded as PEM
    keyFile = open('pubKey.pem', 'wb')  # Open a new file to save the public key
    keyFile.write(pubKey)  # Save the public key
    keyFile.close()  # Close the file
    # Finished Generating the Key Pair

    # Signing the Message Using the Private Key:
    messageFile = open('message.txt', 'r')  # Open the file containing the message for read
    message = messageFile.read()  # Read the message
    messageInByte = str.encode(message)  # Encode the message to bytes (the API accept text encoded in bytes)
    md5Hash = MD5.new(messageInByte)  # Generate the MD5 hash of the message
    signature = PKCS1_PSS.new(key).sign(md5Hash)  # Sign the generated hash using the private RSA key
    signFile = open('signature.txt', 'wb')  # Open a new file to save the signature
    signFile.write(signature)  # Write the signature to the file
    signFile.close()
    # Finished Signing the Hash
    print("The public key has been saved to the file 'pubKey.pem'.\nThe signature has been saved to the file 'signature.txt' to be verified in the next part.")

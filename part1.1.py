from Cryptodome.Hash import SHA512
if __name__ == '__main__':
    f = open('message.txt', 'r')  # Open the file containing the message for read
    message = f.read()  # Read the message
    messageInByte = str.encode(message)  # Encode the message to bytes (the API accept text encoded in bytes)
    hash = SHA512.new()  # Create hash object
    hash.update(messageInByte)  # Compute the hash of the message
    digest = hash.hexdigest()  # Retrieve the digest in hex
    print('Original message:\n' + message + '\n')
    print('Digest in hex:\n' + digest)

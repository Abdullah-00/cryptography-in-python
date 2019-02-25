# The symmetric Diffie-Hellman key method is K = g^(xy) mod p
if __name__ == '__main__':
    base = 7  # This is 'g'
    prime = 23  # This is 'p'

    # Announcing the public 'g' and 'p'
    print("The shared prime and base are as follows:\n\tp = 23,\tg = 7")

    # Asking Alice to choose her 'x'
    # Taking Alice input for 'x'
    aliceKey = int(input("\n\nAlice, enter your 'x': "))  # This holds Alice secret 'x'
    # Computing R1, R1 = g^x mod p
    r1 = (base**aliceKey) % prime  # R1

    # Now, Alice will send her R1 to Bob
    print("\nAlice: My R1 is " + str(r1))

    # Asking Bob to choose his 'y'
    # Taking Bob input for 'y'
    bobKey = int(input("\n\nBob, enter your 'y': "))  # This holds Bob secret 'y'
    # Computing R2, R2 = g^y mod p
    r2 = (base ** bobKey) % prime  # R2

    # Now, Bob will send his R2 to Alice
    print("\nBob: My R2 is: " + str(r2))

    # Now, both parties will compute K, K = g^(xy) mod p = R2^x mod p = R1^y mod p
    k1 = r2**aliceKey % prime  # This is K computed by Alice
    k2 = r1**bobKey % prime  # This is K computed by Bob
    # Note: k1 should be equal to k2

    if (k1 == k2):
        print("\nThe shared key is " + str(k1))
    else:
        print("\nError, Alice and Bob computed different shared keys!")

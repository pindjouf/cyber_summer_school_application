import binascii

# Define the values
plaintext = [0, 1, 0, 1, 0, 0]
secret_key = [1, 0, 1, 0, 1, 0]
ciphertext = []

# Compare the bits
for x,y in zip(plaintext, secret_key):
    if x == y:
        ciphertext.append(0)
    else:
        ciphertext.append(1)

# Convert bit to decimal
deci_ciphertext = int(''.join(map(str, ciphertext)), 2)

print("The ciphertext is: {}".format(ciphertext))
print("Decimal value: {}".format(deci_ciphertext))

# water = binascii.crc32(b"water")

# XOR is an additive cipher that compares two bits to know if the result is true or false example:

# print(20 ^ 42) # Is equal to 62 (^ is the bitwise XOR operator)

# Why did we get 62 from this operation?
    # 20 =  10100
    # 42 = 101010
# result = 111110 = 62
# bit matches = 0 bit doesn't match = 1
# And obviously the first one is nothing so = 0
# In fact you have to very careful to compare it in that exact order and not like this:
    # 10100
    # 101010

# Let's test this with some code

# Using the same values from earlier put the bits in lists
x_bit = [0, 1, 0, 1, 0, 0]
y_bit = [1, 0, 1, 0, 1, 0]

# Compare the bits
for x,y in zip(x_bit, y_bit):
    if x == y:
        print("it matches!")
    else:
        print("it doesn't match!")

# Finding XOR key

## Thoughts

The word document was encrypted using a 256-bit XOR key. \
If I get a sample 256 bits from the file, and try to brute force by finding all the possible 256-bit combinations it would be too much and also analyzing the output would require a lot of time & energy.

That's why I have to find another way to decrypt it. \
So my next test will be to identify where plain text is written in a hex dump, this will allow me to put all my focus on that area. I have to find a flag which means the file probably doesn't contain much text so my sample will contain a string of similar length. \


# The search for the secret key

### Let's start by learning how XOR works with a simple example:

`20 ^ 42` Is equal to 62 (^ is the bitwise XOR operator) \
*Why did we get 62 from this operation?* \
Well XOR works with bits, so let's start by converting our decimal numbers to binary: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20 = &nbsp;&nbsp;10100 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;42 = 101010 \
&nbsp;result = 111110 = 62 \
*The `result` of this operation is also often called `ciphertext`*
#### A simple rule I like to follow is that if the bits match, it's equal to 0. But if they don't it's equal to 1
And in this case the first bit is non-existent so = 0
#### In fact you have to very careful to compare it in that exact order and not like this:
    10100
    101010

### You can checkout [xor.py](https://github.com/pindjouf/cyber_summer_school_application/blob/main/01%20-%20key%20size%20does%20not%20matter/xor.py) for an example of this being put into practice

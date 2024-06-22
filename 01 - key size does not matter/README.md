# The search for the secret key

## Answer

`[CSC2024RepeatingXORIsWeakEncryption]`

## Finding the key

I didn't know too much about xor so at first I did a little bit of research.
I even made a little program to understand it better [xor.py](https://github.com/pindjouf/cyber_summer_school_application/blob/main/01%20-%20key%20size%20does%20not%20matter/xor.py).

But that wasn't enough to get me to the key and the clock was ticking so I stopped relying on my limited programming skills and looked for an alternative way to find the key. In that search I found [xortool](https://github.com/hellman/xortool).

At that point I'd already spent too much time on this flag and couldn't develop a strategy to find it so I put it to the side while I tackled the other challenges.

But after finding the flag in [Writings from hell](https://github.com/pindjouf/cyber_summer_school_application/tree/main/07%20-%20Writings%20from%20Hell_1). I got to see what the flags looked like so I knew that if I used xortool to force the search for known plaintext containing `CSC` or `2024` I would at least get something.

So I did just that and got two potential keys, and in fact the first one gave me a file that contained the keyword "Microsoft Office Word" in its metadata so I knew I did something right. So I went ahead and opened it in google docs.

And there it was :D
![image](./assets/20240622_15h32m44s_grim.png)

## A little bit of history on this README before finding the flag

### Let's start by learning how XOR works with a simple example:

`20 ^ 42` Is equal to 62 (^ is the bitwise XOR operator) \
*Why did we get 62 from this operation?*

Well XOR works with bits, so let's start by converting our decimal numbers to binary: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20 = &nbsp;&nbsp;10100 \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;42 = 101010 \
&nbsp;result = 111110 = 62

*The `result` of this operation is also often called `ciphertext`*

#### A simple rule I like to follow is that if the bits match, it's equal to 0. But if they don't it's equal to 1

And in this case the first bit is non-existent so = 0

#### In fact you have to very careful to compare it in that exact order and not like this:
    10100
    101010

### You can checkout [xor.py](https://github.com/pindjouf/cyber_summer_school_application/blob/main/01%20-%20key%20size%20does%20not%20matter/xor.py) for an example of this being put into practice

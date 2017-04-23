Question:

>RSA encryption/decryption is based on a formula that anyone can find and use, as long as they know the values to plug in. Given the encrypted number 150815, d = 1941, and N = 435979, what is the decrypted number?

Hints:

>decrypted = (encrypted) ^ d mod N

Points: 50

Well this one was fun. I decided to use python, because of the awesome `pow()` function. Look at the python file for more.

The flag is `133337`

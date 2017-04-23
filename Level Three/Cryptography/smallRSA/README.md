Question:
>You intercepted a single message. However, it appears to be encrypted. Can you decrypt it? [Message](https://webshell2017.picoctf.com/static/9eb112487fc2fb2d537967d243124ae1/clue.txt)

Hints:
>Normally, you pick e and generate d from that. What appears to have happened in this case? What is likely about the size of d?

This problem can be solved by Wiener's attack. I used [this tool](https://github.com/pablocelayes/rsa-wiener-attack) to find `d`, and then cracked the ciphertext `c`. I edited the python file to make it specific to this problem.

The flag is `flag{Are_any_RSA_vals_good_13441315963}`

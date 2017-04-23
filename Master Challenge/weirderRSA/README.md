Type: Cryptography

Points: 175

Question:
>Another message encrypted with RSA. It looks like some parameters are missing. Can you still decrypt it? [Message](https://webshell2017.picoctf.com/static/99cf92a3853568ddec44756c1e3e97ef/clue.txt)

Hints:
>Is there some way to create a multiple of p given the values you have?
>Fermat's Little Theorem may be helpful.

I used the java program to find `d`, and the python program to get the flag.

The flag is `flag{wow_leaking_dp_breaks_rsa?_47689841281}`

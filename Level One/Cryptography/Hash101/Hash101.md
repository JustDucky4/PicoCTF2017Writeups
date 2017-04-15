Question: 
>Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:9661
>UPDATED 16:12 EST 1 Apr.

Hints:
>All concepts required to complete this challenge, including simple modular math, are quickly found by googling :)

All right, let's start by connecting to the shell.

`netcat shell2017.picoctfcom 9661`

```Welcome to Hashes 101!                                      
                                                            
There are 4 Levels. Complete all and receive a prize!       
                                                            
                                                            
-------- LEVEL 1: Text = just 1's and 0's --------          
All text can be represented by numbers. To see how different
 letters translate to numbers, go to http://www.asciitable.c
om/                                                         
                                                            
TO UNLOCK NEXT LEVEL, give me the ASCII representation of 01
1011000110111101110110011001010110110001111001 
```

It seems like the string it wants us to convert to ascii is in binary. Let's use a [binary to ascii converter.](http://www.binaryhexconverter.com/binary-to-ascii-text-converter)

The converted text is `lovely`

We just input that and press enter

```Correct! Completed level 1                                  
                                                            
------ LEVEL 2: Numbers can be base ANYTHING -----          
Numbers can be represented many ways. A popular way to repre
sent computer data is in base 16 or 'hex' since it lines up 
with bytes very well (2 hex characters = 8 binary bits). Oth
er formats include base64, binary, and just regular base10 (
decimal)! In a way, that ascii chart represents a system whe
re all text can be seen as "base128" (not including the Exte
nded ASCII codes)                                           
                                                            
TO UNLOCK NEXT LEVEL, give me the text you just decoded, lovely,
as its hex equivalent, and then the decimal equivalent o
f that hex number ("foo" -> 666f6f -> 6713199)
```

We use an [ascii to hex converter](https://www.browserling.com/tools/text-to-hex) and get:
`6c 6f 76 65 6c 79` but we must take the spaces out. After just removing spaces, we get `6c6f76656c79`

```
Good job! 6c6f76656c79 to ASCII -> lovely is lovely         
Now decimal
```
We already have the hex, so why not just do [hex to decimal?](http://www.binaryhexconverter.com/hex-to-decimal-converter)

The output is `119225983528057`

```
Good job! 119225983528057 to Hex -> 6c6f76656c79 to ASCII ->
 lovely is lovely
Correct! Completed level 2
```
Moving on!

```
----------- LEVEL 3: Hashing Function ------------          
A Hashing Function intakes any data of any size and irrevers
ibly transforms it to a fixed length number. For example, a 
simple Hashing Function could be to add up the sum of all th
e values of all the bytes in the data and get the remainder 
after dividing by 16 (modulus 16)                           
                                                            
TO UNLOCK NEXT LEVEL, give me a string that will result in a
 2 after being transformed with the mentioned example hashin
g function
```
Okay, so I know that there's probably a way to find it first guess and everything, but I just did guess and check.

```
>18                                                         
incorrect. sum of all characters = 105 mod 16 = 9 does not e
qual 2                                                      
>14                                                         
incorrect. sum of all characters = 101 mod 16 = 5 does not e
qual 2                                                      
>11                                                         
Correct! Completed level 3
```
Call it what you want, but it worked.

```--------------- LEVEL 4: Real Hash ---------------          
A real Hashing Function is used for many things. This can in
clude checking to ensure a file has not been changed (its ha
sh value would change if any part of it is changed). An impo
rtant use of hashes is for storing passwords because a Hashi
ng Function cannot be reversed to find the initial data. The
refore if someone steals the hashes, they must try many diff
erent inputs to see if they can "crack" it to find what pass
word yields the same hash. Normally, this is too much work (
if the password is long enough). But many times, people's pa
sswords are easy to guess... Brute forcing this hash yoursel
f is not a good idea, but there is a strong possibility that
, if the password is weak, this hash has been cracked by som
eone before. Try looking for websites that have stored alrea
dy cracked hashes.                                          
                                                            
TO CLAIM YOUR PRIZE, give me the string password that will r
esult in this MD5 hash (MD5, like most hashes, are represent
ed as hex digits):                                          
ac2f556a0eb415745b31e14a91d55d75
```

This one's fun. It's an md5 hash, so we can probably [crack it online](https://hashkiller.co.uk/md5-decrypter.aspx)
Just plug in the hash, and it gives back `ac2f556a0eb415745b31e14a91d55d75 MD5 : muc1d`

So `muc1d` is the password.

```
Correct! Completed level 4                                  
You completed all 4 levels! Here is your prize: c3ee093f26ba
147ccc451fd13c91ffce
```

And we get our flag. `c3ee093f26ba147ccc451fd13c91ffce`





Question:
>You stumbled upon a group [Message.](https://webshell2017.picoctf.com/static/60a7417f2afdb633c070ae183ddf75f4/clue.txt) Can you figure out what they were sending? The string sent is ascii encoded as a hex number (submit the ascii string as the flag)

Hints:
>The same message, with a small exponent, is being encrypted with several different n values

Points: 120

The name is another hint here. This is a broadcast attack. For this one, I used [RSA-Hastad](https://github.com/JulesDT/RSA-Hastad/blob/master/rsaHastad.py) with a few edits to make it specific for this program.

```
$ python Hastad.py 


	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	        RSA Hastad Attack         
	         JulesDT -- 2016          
	         License GNU/GPL          
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Decoded Hex :
62726f6164636173745f776974685f736d616c6c5f655f69735f6b696c6c65725f3134383036353339353436
---------------------------
As Ascii :
broadcast_with_small_e_is_killer_14806539546
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

The flag is `broadcast_with_small_e_is_killer_14806539546`

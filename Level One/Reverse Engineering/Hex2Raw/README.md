Question:
>This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to >/problems/3ced8dfe6c77c63010c94a84656fa6ea and turn that Hex2Raw!

Hints:
>Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

Points: 20

```
$ ./hex2raw                                               
Give me this in raw form (0x41 -> 'A'):                     
1a558acddabd64bbccdd94903eafdf18 
```

Okay, so we can try turning it directly into ascii and copy-pasting that, but it probably won't work due to unprintable characters. So, we can pipe it through:

```
$ echo "1a558acddabd64bbccdd94903eafdf18" | xxd -r -p | ./hex2raw
Give me this in raw form (0x41 -> 'A'):                     
1a558acddabd64bbccdd94903eafdf18                            
                                                            
You gave me:                                                
1a558acddabd64bbccdd94903eafdf18                            
Yay! That's what I wanted! Here be the flag:                
ceb80093717fd7e9aae149dacc7ac9b3                            
```

(Oh, just copy-pasting the original thing doesn't work. It converts the `you gave me` input to hex, so you have to do the xxd thing.)

Anyway, the flag is `ceb80093717fd7e9aae149dacc7ac9b3`

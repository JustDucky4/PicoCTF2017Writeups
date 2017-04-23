Question:
>This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/0dec9a999595d0801333c08899bf2b03 and turn that Raw2Hex!

Hints:
>Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

I'm not going to lie. I didn't do this problem while the competition was ongoing, but I finished it after it ended. It was a lot easier than I thought it was.


`./hex2raw | xxd -p`

```
$ ./raw2hex|xxd -p                                        
54686520666c61672069733ac3aeefde2d8fa0bc81f955314447a348
$
```

So, the flag is `54686520666c61672069733ac3aeefde2d8fa0bc81f955314447a348`

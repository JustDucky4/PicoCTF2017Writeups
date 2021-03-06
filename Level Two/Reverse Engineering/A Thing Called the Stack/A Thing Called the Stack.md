Question:
>A friend was stacking dinner plates, and handed you this, saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

Hints:
>Where is the return address saved on the stack?
>Which commands actually affect the stack?


For this write-up, the code is so short that I will just paste the entire thing here.

Without further ado, here's the contents of `assemble.s`

```
foo:
    pushl %ebp
    mov %esp, %ebp
    pushl %edi
    pushl %esi
    pushl %ebx
    sub $0x90, %esp
    movl $0x1, (%esp)
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
```

Well isn't this fun.

A good thing to do is convert the hex to decimal for readability. 
0x90 in decimal is 144.

After the `sub $0x90, %esp`, there are 4 more instructions. In 32 bit assembly, each instruction here moves 144 by 4. 

4 x 4 = 16.

We add 16 to 144. 
16 + 144 = 160.
The hex value of 160 is `0xA0`

So, the flag is `0xA0`

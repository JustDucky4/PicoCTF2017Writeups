Question:
>You found a text file with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

Hints:
>All of the commands can be found [here](https://en.wikipedia.org/wiki/X86_assembly_language) along with what they do.
>It may be useful to be able to run the code, with test values.

I'm going to put the full file here:

```
.global main

main:
    mov $XXXXXXX, %eax
    mov $0, %ebx
    mov $0x6, %ecx
loop:
    test %eax, %eax
    jz fin
    add %ecx, %ebx
    dec %eax
    jmp loop
fin:
    cmp $0x533a, %ebx
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
```

I'm not going to explain how the assembly works, just how to solve this problem.

For this one, 0x6 in decimal is 6 (no surprise there), and 0x533a is 21306

To get the flag, divide 21306 by 6, which is 3551. So, the number that $XXXXXXX should be is `0xddf`

Therefore, the flag is `0xddf`

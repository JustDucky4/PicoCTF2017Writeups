Question: 
>I was told to use the linux strings command on yarn, but it doesn't work. Can you help? I lost the flag in the binary somewhere, and would like it back

Hints:
>What does the strings command use to determine if something is a string?
>Is there an option to change the length of what strings considers as valid?

I decided to abandon the whole strings thing and take another route.

For windows, I recommend [HxD](https://mh-nexus.de/en/hxd/) For mac and linux, xxd works fine.


In the ascii data, we can find:

```
0000540: 5375 6200 6d69 7400 5f6d 6500 5f66 6f00  Sub.mit._me._fo.
0000550: 725f 4900 5f61 6d00 5f74 6800 655f 6600  r_I._am._th.e_f.
0000560: 6c61 6700 011b 033b 2800 0000 0400 0000  lag....;(.......
```
So, the flag is `Submit_me_for_I_am_the_flag`

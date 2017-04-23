Question: 
>We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:11511. Remember to use Ctrl-C to cut the connection if it overwhelms you!

Hints:
>There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

Points: 30

The stream of text is very fast, very long, and mostly garbage. We can use the grep command:

```
$ netcat shell2017.picoctf.com 11511 | grep "flag"

19:32:39 whatisflag: my parents want to see me to create a s
elf driving car                                             
19:32:39 personwithflag: Several heavily mustached dolphins 
give me hope to drink your milkshake                        
19:32:39 personwithflag: my homegirlz , in my well-educated 
opinion, are our best chance for what, I do not know        
19:32:39 personwithflag: My sworn enemy is our best chance t
o help me spell 'raspberry' correctly                       
19:32:40 personwithflag: my homegirlz are the best of friend
s for the future of humanity                                
19:32:40 whatisflag: A silly panda gives me hope to make a r
asberry pie                                                 
19:32:40 whatisflag: Cats with hats are the best of friends 
for what, I do not know                                     
19:32:41 personwithflag: A silly panda has attacked my toes 
to generate fusion power                                    
19:32:41 ihazflag: Only us give me hope to generate fusion p
ower                                                        
19:32:41 whatisflag: Only us have demanded my presence to ge
nerate fusion power                                         
19:32:41 personwithflag: A huge moose gives me hope to gener
ate fusion power                                            
19:32:41 personwithflag: a heavily bearded dolphin has attac
ked my toes for the future of humanity                      
19:32:43 whatisflag: You is our best chance to understand me
19:32:44 flagperson: this is part 1/8 of the flag - 8d84
19:32:45 whatisflag: that girl from that movie wants to stea
l my sloth to help me spell 'raspberry' correctly
```

That's a lot, even though it's filtered!

Let's further filter it, and only get flagperson's messages:
```
$ netcat shell2017.picoctf.com 11511 | grep "flagperson"
19:35:06 flagperson: this is part 1/8 of the flag - 8d84
19:35:10 flagperson: this is part 2/8 of the flag - 913f
19:35:10 flagperson: this is part 3/8 of the flag - 84bd
19:35:11 flagperson: this is part 4/8 of the flag - 68a4
19:35:11 flagperson: this is part 5/8 of the flag - 6576
19:35:16 flagperson: this is part 6/8 of the flag - 3e48
19:35:19 flagperson: this is part 7/8 of the flag - d9d9
19:35:25 flagperson: this is part 8/8 of the flag - ca1c
```

So, the flag is `8d84913f84bd68a465763e48d9d9ca1c`



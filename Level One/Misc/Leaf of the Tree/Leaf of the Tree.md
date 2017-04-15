Question:
>We found this annoyingly named directory tree starting at /problems/4052472b84e355d1e1a42f5899fe0e76. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

Hints:
>Tab completion is a wonderful, wonderful thing

It most certainly is.

Tab completion is for when you don't want to type out the full name of what you're looking for, if it is the only one in the directory with a similar enough name.

For example, if I have a directory, and two files named

asdfjkjhgsasfghj.txt
zxcbnmnbvcxzxcvb.txt

I can type a[tab], and it will autofill.

If I go to /problems/4052472b84e355d1e1a42f5899fe0e76, (it's really unfortunate that tab completion doesn't work here. Something about permission. These long hex paths are REALLY annoying.

I'll just copy-paste what I found:

```
$ ls                                                      
trunk
$ cd trunk                                                
$ ls                                                
branch04cf  trunkef9b
$ cd branch04cf/                                    
$ ls                                     
leaf6b5f  leafd6ec                                          
$ cd ..                                  
$ cd trunkef9b/                                     
$ ls                                      
trunk99e1
$ cd trunk99e1/                           
$ ls                            
branch1a36  branch6b01  trunk54f4             
$ cd branch1a36/                
$ ls                 
leaf33af                                                    
$ cd ..              
$ cd branch6b01/                
$ ls                 
leaf2ee6  leaf41c0  leaf518f                                
$ cd ..              
$ ls                            
branch1a36  branch6b01  trunk54f4
$ cd trunk54f4/                 
$ ls                  
branch9b67  branchb9e7  trunk61be               
$ cd branch9b67/      
$ ls       
leafc6aa                                                    
$ cd ..    
$ cd branchb9e7/      
$ ls       
leafc50a                                                    
$ cd ..    
$ cd trunk61be/       
$ ls        
branch00bc  branchbe5f  trunk89be
$ cd branch00bc/
$ ls
leaf94f2  leaf9ced                                          
$ cd ..
$ cd branchbe5f/
$ ls
leaf351b  leaf4304                                          
$ cd ..
$ cd trunk89be/                                                         
$ ls
trunk87bf
$ cd trunk87bf/
$ ls                                                
trunkb252
$ cd trunkb252/                                     
j$ ls                                      
branchd8bd  flag
$ cat flag                                
aae8c400f845fd47fdbb6a77ba027771
```

So, the flag is `aae8c400f845fd47fdbb6a77ba027771`

(I removed a whole wall of text which was mostly my username and the current directory from each prompt to make it more readable. If something doesn't make sense, let me know.)

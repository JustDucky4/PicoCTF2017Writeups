Question:
>We found an even bigger directory tree hiding a flag starting at /problems/57a246295d1345729cbddf98c16fcaed. It would be impossible to find the file named flag manually...

Hints:
>Is there a search function in Linux? Like if I wanted to 'find' something...

Points: 30

Luckily enough, there is. It's the `find` command. It's pretty awesome.

We can use it like this:
`find flag . -name 'flag'`

and get back 

`./treefced1e/trunka090/trunk957d/trunk6de6/trunke68e/trunkf287/trunk070b/trunke47a/branch4c77/flag`

so now we just cd to that path...

```
$ ls               
flag  leaf4ffb  leaf6a89                                    
$ cat flag         
b51adfb58ec99a8c81db853c7acdd7bd
```

Voila! the flag is `b51adfb58ec99a8c81db853c7acdd7bd`

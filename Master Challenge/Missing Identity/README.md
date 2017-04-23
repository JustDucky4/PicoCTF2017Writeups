Type: Forensics

Points: 100

Question:
>Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one [file](https://webshell2017.picoctf.com/static/e7c9d7d94f185625b578bf0004890b80/file) and find the flag. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out. The flag starts with the character z.

Hints:
>What file is this?
>What do you expect to find in the file structure?
>All characters in the file are lower case or numberical. There will not be any zeros.

The biggest problem here is trying to figure out what kind of file `file` is. 

```
$ file file
file: data
```

Gee, thanks.

After a little poking around, I discovered that it was some form of compressed file, most likely a .zip file. xxd showed what needed to be fixed:

```
XXXXXX...."D.J}.
..............fl
ag.png..g<[...C.
```

At the top, something has been X'd out. We need to figure out what that is in order to access flag.png. 

A zip file has a magic number of 4 bytes. The magic number is: `50 4b 03 04`. So that's 4 bytes, but we need 2 more. I just put in `00 00`, and it somehow uncorrupted the file.
Inside were flag.png, nottheflag1.png, nottheflag2.png, nottheflag3.png, and nottheflag4.png.

The flag is: `zippidydooda88938568`

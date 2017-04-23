Question: 
>Can you help me find the data in this [littleschoolbus.bmp?](https://webshell2017.picoctf.com/static/a08a97410634f3250e9659a1793a8908/littleschoolbus.bmp)

Hints:
>Look at least significant bit encoding!!

Ahhh, a steganography problem :)

The hint suggests that the message is hidden with LSB steganography. Luckily, there's a great tool called [zsteg](https://github.com/zed-0xff/zsteg) that can make this an easy feat.

```
$ zsteg littleschoolbus.bmp 
imagedata           .. text: "~vtsoljmkhhfgXWWNNNVUV~}"
b1,lsb,bY           .. text: "flag{remember_kids_protect_your_headers_c1a3}"
```

The flag is `flag{remember_kids_protect_your_headers_c1a3}`

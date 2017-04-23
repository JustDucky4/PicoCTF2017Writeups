Question:
>Find the location of the flag in the image: [image.jpg.](https://webshell2017.picoctf.com/static/b7e7b463b0a364ab1ca4955544e7f72d/image.jpg) Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

Hints:
>How can images store location data? Perhaps search for GPS info on photos.

I did this problem on a mac, where it's really easy to find the latitude and longitude.
(Double click on image -> Get Info)

I got

```
Latitude: 11
Longitude: 31
```

So, that's the important stuff. Now we just have to find the flag. Let's see the hex dump of the file:

(By the way, I'm cutting out only the important stuff. The dump is ~2000 lines long.

```
0005bc0: 0000 0000 00ff fe00 7522 596f 7572 2066  ........u"Your f
0005bd0: 6c61 6720 6973 2066 6c61 675f 325f 6d65  lag is flag_2_me
0005be0: 7461 5f34 5f6d 655f 3c6c 6174 3e5f 3c6c  ta_4_me_<lat>_<l
0005bf0: 6f6e 3e5f 3233 6331 2e20 4e6f 7720 6669  on>_23c1. Now fi
0005c00: 6e64 2074 6865 2047 5053 2063 6f6f 7264  nd the GPS coord
0005c10: 696e 6174 6573 206f 6620 7468 6973 2069  inates of this i
0005c20: 6d61 6765 2120 2844 6567 7265 6573 206f  mage! (Degrees o
0005c30: 6e6c 7920 706c 6561 7365 2922 ffdb 0084  nly please)"....
```
`Your flag is flag_2_meta_4_me_<lat>_<lon>_23c1. Now find the GPS coordinates of this image! (Degrees only please)"`

Cool. I have the latitude and longitude, so I just need to plug them in:

`flag_2_meta_4_me_11_31_23c1`

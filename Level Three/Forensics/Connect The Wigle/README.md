Points: 140

Question:
>Identify the data contained within [wigle](https://webshell2017.picoctf.com/static/9a447c975a6c373583ba6d3dd4527412/wigle) and determine how to visualize it. Update 16:26 EST 1 Apr If you feel that you are close, make a private piazza post with what you have, and an admin will help out.

Hints:
>Perhaps they've been storing data in a database. How do we access the information?
>How can we visualize this data? Maybe we just need to take a step back to get the big picture?
>Try zero in the first word of the flag, if you think it's an O.
>If you think you're super close, make a private piazza post with what you think it is.

This is a fun one, once you stop ripping your hair out. A good tool to visualize this is [this site](https://www.darrinward.com/lat-long/)

The file I have linked in this folder has a `.sqlite3` file extension. The original did not. I found the type of file it was with the `file` command, and just added the extension so I could open it up with [DB Browser for SQLite](http://sqlitebrowser.org/)

To get the flag, we need to graph the lat and lon coordinates.

I used the python file to get them into a format in which I could copy-paste.

The coordinates can be copy-pasted into the box in the site.

Once plotted, the groups of coordinates can be identified as letters (zoom in if you can't see it.)

To find the flag, each letter must be identified.

The flag is `FLAG{F0UND_M3_20C860C7}`

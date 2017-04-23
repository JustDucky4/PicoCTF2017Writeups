Type: Web Exploitation

Points: 50

Question: 
>I really need to login to this [website](http://shell2017.picoctf.com:35895/), but the developer hasn't implemented login yet. Can you help?

Hints:
>Where does the password check actually occur?
>Can you interact with the javascript directly?

Javascript file:
http://shell2017.picoctf.com:35895/static/client.js

In this problem, when the submit button is clicked, `process_password()` is run. Inside `process_password()`, it sets `res` to `validate(pword)`. The `validate()` function is incomplete, right now all it does is `return false`.  
Then, it calls `make_ajax_req(false)`, which prevents login.

If we want to get in, we have to change the function that is called by the onlick from
`<button type="button" onclick="process_password()">Submit</button>`

to

`<button type="button onclick="make_ajax_req(true)`

which reveals the flag: `client_side_is_the_dark_sidebde1f567656f8c9b654a1ec24e1ff889`

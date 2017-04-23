Question: 
>I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:44840?

Hints:
>Use the nc command to connect!
>I hear python is a good means (among many) to generate the needed input.
>It might help to have multiple windows open

Points: 20

Just as the hint suggests, I used a python file. The question had a certain format. It was always something along the lines of:

```
To prove your skills, you must pass this test.
Please give me the 'K' character 625 times, followed by a 
single '4'.
To make things interesting, you have 30 seconds.
Input:
```

So the flag is `with_some_recognition_and_training_delusions_become_glimpses_97b1f7514342008e75bd0238aa007d09`

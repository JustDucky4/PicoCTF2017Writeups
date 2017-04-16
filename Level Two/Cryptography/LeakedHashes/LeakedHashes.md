Question: 
>Someone got hacked! Check out some service's password hashes that were leaked at [hashdump.txt](https://webshell2017.picoctf.com/static/f8a67abd9fe25806eb8b550404def163/hashdump.txt)! Do you think they chose strong passwords? We should check... The service is running at shell2017.picoctf.com:46881!

Hints:
>See if you can crack any of the login credentials and then connect to the service as one of the users. What's the chance these hashes have actually already been broken by someone else? Are there websites that host those cracked hashes? Connect from the shell with nc.

This one's fun.

Unfortunately, not all of the hashes here can be cracked, but one is enough.

let's just take the top 5:

```
root:be3f7de032d2e398ec542a7df71e0417
christene:5ddb0142dc7f8e56bf99e6f25425fd29
nadia:91f7fceef0044b405d862d132fa667e9
myra:435fc037deebaf8d9e3c4a4fb3e2fac7
sharell:96e68796a3b073205bb8d5688ded0934
```
and run the hashes through [this site](https://crackstation.net/)

Two of the hashes, christene and sharell, are successfully cracked as md5 hashes. The passwords are `ch4sm` and `h4ugh` respectively.

So, when we connect to the service, 

```
enter username:                                             
sharell                                                     
sharell's password:h4ugh                                    
welcome to shady file server. would you like to access the c
at ascii art database? y/n                                  
y                                                           
                                                            
     /\_/\                                                  
    ( o o )                                                 
  G-==_Y_==-M                                               
      `-'                                                   

  /\ /\                                                     
  (O o)                                                     
=(: ^ :)=                                                   
  '*v*'                                                     

 |\_/|                                                      
 (. .)                                                      
  =w= (\                                                    
 / ^ \//                                                    
(|| ||)                                                     
,""_""_ .                                                   
                                                            
     /\_/\                                                  
    ( o o )                                                 
   -==_Y_==-                                                
      `-'                                                   
    /\**/\                                                  
   ( o_o  )_)                                               
   ,(u  u  ,),                                              
  {}{}{}{}{}{}                                              

  /\_/\                                                     
 ( o.o )                                                    
  > ^ <                                                     

       /\_/\                                                
  /\  / o o \                                               
 //\ \~(*)~/                                                
 `  \/   ^ /                                                
    | \|| ||                                                
    \ '|| ||                                                
     \)()-())                                               

   A_A                                                      
  (-.-)                                                     
   |-|                                                      
  /   \                                                     
 |     |  __                                                
 |  || | |  \___                                            
 \_||_/_/                                                   

     /\__/\                                                 
    /`    '\                                                
  === 0  0 ===                                              
    \  --  /    - flag is 18e27fcac2c4b21329e0b118898794c0  
                                                            
   /        \                                               
  /          \                                              
 |            |                                             
  \  ||  ||  /                                              
   \_oo__oo_/#######o                                       

  /\___/\                                                   
 ( o   o )                                                  
 (  =^=  )                                                  
 (        )                                                 
 (         )                                                
 (          )))))))))))                                     

 /\ /\                                                      
 (O o)                                                      
=(:^:)=                                                     
   U                                                        

    _,,/|                                                   
    \o o'                                                   
    =_~_=                                                   
    /   \ (\                                                
   (////_)//                                                
   ~~~                                                      

   /\     /\                                                
  {  `---'  }                                               
  {  O   O  }                                               
~~|~   V   ~|~~                                             
   \  \|/  /                                                
    `-----'__                                               
    /     \  `^\_                                           
   {       }\ |\_\_   W                                     
   |  \_/  |/ /  \_\_( )                                    
    \__/  /(_E     \__/                                     
      (  /                                                  
       MM                                                   

              ("`-''-/").___..--''"`-._                     
               `6_ 6  )   `-.  (     ).`-.__.`)             
               (_Y_.)'  ._   )  `._ `. ``-..-'              
             _..`--'_..-_/  /--'_.' ,'                      
           (il),-''  (li),'  ((!.-'                         

from http://user.xmission.com/~emailbox/ascii_cats.htm
```

So, the flag is `18e27fcac2c4b21329e0b118898794c0`

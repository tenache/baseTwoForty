ReadMe
# Base 240 
Just use the **function** base240(x), with x being a decimal number, and you'll get my idea of a new type of numeric system. 
Heads up, base240(240) is == [1,0]. It gives you a list of ... let's call them "digits". Each digit can in turn have multiple digits, so from now on 
I'll distinguish them by calling them **DIGITS**. To avoid confusion, 
it prints out each digit in a separate line, so 240 will be printed out as:
1
0
The reason for this, is that there is not actually a single symbol for each value from 1 to 240. In stead, there is are symbols from 1 to 20, and
then a different symbol for each factor of 120. DIGITS are obtained by summing symbols in a single line (or in a single element of the list which
base240() returns). DIGITS are the same as decimal or binary or hexagesimal digits. So, for example, 361 = 240 + 120 + 1. So, in this case the program will print:
1
(symbol for 120)(space)1

... and it will return the list:
[[1],[(symbol for 120),1]]

##Why 240
You might be thinking I pulled 240 directly out of my ass. And although I do love pulling numbers out of my ass, I actually have a reason for 
this base. 240 is a highly composite number, and as such, it is great for dividing! This video got me thinking about it: [Video on English coinage](https://www.youtube.com/watch?v=R2paSGQRwvo). Also, this video [Video on number systems](https://www.youtube.com/watch?v=l4bmZ1gRqCc&t=343s), and 
this one [Video on cuneiform numbers](https://www.youtube.com/watch?v=RR3zzQP3bII), and this one: [Video on base 12](https://www.youtube.com/watch?v=U6xJfP7-HCc) got me thinking on number systems in general. For most of humanity, most people were illiterate. Did they really think of numbers in a decimal way? Shure, we get it beating into us because that's how we write numbers, but how about people who didn't write their numbers. They still had to buy and sell things, they still had to do everyday maths. How did they manage it? My suspicion, is that this system of 240 helped, and it might not have meant anything to them that it wasn't a round number. My program here is a very lazy attempt to capture how their heads might have processed maths. 
Or, it's just another side project helping me learn how to code, whatever. 


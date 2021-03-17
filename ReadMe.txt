ReadMe
# Base 240 
Just use the function base240(x), with x being a decimal number, and you'll get my idea of a new type of numeric system. 
Heads up, base240(240) is == [1,0]. It gives you a list of ... let's call them "digits". Each digit can in turn have multiple digits, so from now on 
I'll distinguish them by calling them DIGITS. To avoid confusion, 
it prints out each digit in a separate line, so 240 will be printed out as:
1
0
The reason for this, is that there is not actually a single digit for each value from 1 to 240. In stead, there is are digits from 1 to 20, and
then a different digit for each factor of 120. DIGITS are obtained by summing digits in a single line (or in a single element of the list which
base240() returns). DIGITS are the same as decimal or binary or hexagesimal digits. So, for example, 361 = 240 + 120 + 1. So, in this case the program will print:
1
(symbol for 120)(space)1

... and it will return the list:
[[1],[(symbol for 120),1]]

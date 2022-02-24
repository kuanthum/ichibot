import mymath

mymath.add(1,3)
mymath.sub(1,3)

from mymath import add, sub

add(19,5)
sub(5, 4)

from colorama import Fore, Style, init


init(convert=True)

print (Fore.RED, "Hello world")

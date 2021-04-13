# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools 

s = input()  #input of the string..

for k,a in itertools.groupby(s):  #passing the string 
    print("({}, {})".format(len(list(a)),k),end=" ")

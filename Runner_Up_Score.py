n = int(input()) #tells about the size..
A = list(map(int,input().strip().split()))  #input of the list using map...
S = set(A)  #converting into set so that duplicate elements can be removed..
L = list(S)  #again converting into list so that it can be sorted..

L.sort(reverse=True)   #in descending order..
print(L[1])  #printing the first runner up..

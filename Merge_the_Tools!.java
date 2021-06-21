def merge_the_tools(string, k):
    # your code goes here
   n = len(string)  #first calculated the length of the string..
   i=0
   j=1
   while i in range(n):  #traversing the string(and changing the index accordingly.)
    s = string[i:k*j]  #Extracted particular sub-string..
    t=""  #empty string..
    for p in s:
        if(p in t):
            pass
        else:
            t = t+p
    print(t)          #making a new string which won't contain the duplicates..
    i=k*j  #increase the value of i..(for new substring)
    j=j+1  #same with the j..
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

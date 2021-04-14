n = int(input())  #input the size of the tuple..
 
t = tuple(map(int,input().split()))   #input of the elements in tuple using map function...

#list1 = []
#for i in range(0,n):
    
#   value = input()
#   list1.append(int(value))
#t = tuple(list1)

print(hash(t))   #print the hash value of the tuple passed..

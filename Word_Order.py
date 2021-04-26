# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())  #number of words..
words = list()

for i in range(0,n):
    words.append(input())  #input word..
word_distinct = set(words) #inorder to get the distinct words.

print(len(word_distinct))  #Number of distinct words..

counts = dict() #creating a dictionary
for word in words:
    counts[word] = counts.get(word,0) + 1

for v in counts.values():
    print(v,end=" ")

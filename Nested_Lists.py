if __name__ == '__main__':
    m = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=list()
        l.append(score)
        l.append(name)
        
        m.append(l)
m.sort()
#print(m)
maxmin = m[0][0]
for i in range(1,len(m)):
    if(m[i][0]>maxmin):
        maxmin=m[i][0]
        break
name = list()       
for i in range(0,len(m)):
    if(m[i][0]==maxmin):
        name.append(m[i][1])
name.sort()
for i in range(0,len(name)):
    print(name[i])          

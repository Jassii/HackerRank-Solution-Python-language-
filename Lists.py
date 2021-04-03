if __name__ == '__main__':
    l = []
    N = int(raw_input())  #number of commands..
    for x in range(N):
        cmd = raw_input()  #command
        o = cmd.split()
        if(o[0]=='insert'):
            i = int(o[1]) #index
            e = int(o[2]) #element
            l.insert(i,e)
        elif(o[0]=='print'):
            print(l)
        elif(o[0]=='remove'):
            e = int(o[1])
            l.remove(e)
        elif(o[0]=='append'):
            e = int(o[1])
            l.append(e)
        elif(o[0]=='sort'):
            l.sort()
        elif(o[0]=='pop'):
            l.pop()
        elif(o[0]=='reverse'):
            l.reverse()

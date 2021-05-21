if __name__ == '__main__':
    n = int(input())
    student_marks = {}  #this is our dictionary..
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
for i in student_marks:
    if(i==query_name):
        s = sum(student_marks[i])
        avg = s/len(student_marks[i])
        break
 #when you have to print upto two decimal places...we should use this...   
avgr = "{:.2f}".format(avg)
print(avgr)        

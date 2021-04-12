def is_leap(year):
    leap = False
    if(year%4==0):  #divided by 4..
        
        if(year%100==0):  #divided by 100 and 4..
            
            if(year%400==0): #divided by 100,4 and now 400..
                
                leap = True 
            else: #not divided by 400 but divided by 100.
                
                leap = False          
        else:  #not divided by 100 but divided by 4..
            leap = True
    else: #not divided by 4
        leap=False
                     
    return leap   
  
  
year = int(input())  #input of the year..
print(is_leap(year))  #calling the is_leap function to check whether the year passed is leap year or not..

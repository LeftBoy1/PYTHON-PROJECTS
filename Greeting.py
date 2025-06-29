import time

a=time.localtime().tm_hour
b=time.localtime().tm_min
c=time.localtime().tm_sec

if(a>=0 and a<12):
    period = "AM"
    
elif(a>=12):
    period = "PM"


if a == 0:
    display_hour = 12  
elif a > 12:
    display_hour = a - 12  
else:
    display_hour = a 



if(a>=0 and a<12):
    print(f"{display_hour}:{b}:{c} {period}")
    print("Good Morning Sir")
    
elif(a>=12 and a<=16):
    print(f"{display_hour}:{b}:{c} {period}")
    print("Good AfterNoon Sir")
        
else:
    print(f"{display_hour}:{b}:{c} {period}")
    print("Good Night Sir")
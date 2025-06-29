import time

#CASE 1- (Using strftime())
t = time.strftime('%H:%M:%S')
print(t)

#CASE 2-( Using localtime() )
a=time.localtime()

print(a.tm_hour,":",a.tm_min,":",a.tm_sec)


#CASE 3-( Using strtime() with 12 hour format )

t = time.strftime('%I:%M:%S %p')
print(t)

#CASE 4-( Using localtime() with 12 hour format)

a= time.strftime('%I:%M:%S %p', time.localtime())
print(a)



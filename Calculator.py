a= input("Enter Your First No.: ")
b= input("Enter Your Second No.: ")
c= input("Enter Your Operator: \n 1.ADDITION \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Percentage \n =>")

# operation = input()

if c =="1":
     
    print("Your Sum is: ", str(float(a)+float(b)))
    
    
elif c =="2":

    print("Your Difference is: ", str(float(a)-float(b)))
    
    
elif c =="3":

    print("Your Multiply is: ", str(float(a)*float(b)))
    
    
elif c =="4":

    print("Your Divison is: ", str(float(a)/float(b)))


elif c =="5":

    print("Your Percentage is: ", str(float(a)%float(b)))

else:
    print("Please Enter a Valid Number")
    
    
    
    

import time

def breath(n):
    print("\033[1mTAKE A BREATH\033[0m")
        
    for i in range(1, n+1):
        time.sleep(1)
        print(i)
        
        
def hold(n):
    print("\033[1mHOLD IT\033[0m")
        
    for i in range(1, n+1):
        time.sleep(1)
        print(i)
    
    
def release(n):
    print("\033[1mNOW RELEASE\033[0m")
        
    for i in range(1, n+1):
        time.sleep(1)
        print(i)
    print("-"*20)
        
n = int(input("Enter the number to count up to: "))
t = int(input("How many times do you want to repeat?: "))

for _ in range(t):
    breath(n)
    hold(n)        
    release(n)
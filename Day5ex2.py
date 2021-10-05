x = 0
while x !=100:
    print("please input your number")
    x=int(input())
    if x > 100 : print("too high, try again")
    elif x < 100 : print("too small, try again")
    else: 
        print("good job, is a nice number")
        break
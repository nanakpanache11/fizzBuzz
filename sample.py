a=int(input("Enter a number."))

if (a%5==0 and a%3==0):
    print("fizzBuzz.")
    
elif(a%5==0):
    print("fizz.")
    
elif(a%3==0):
    print("Buzz.")
    
else: 
    print(a)
    
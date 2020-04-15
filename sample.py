# name1=input(">>")
# print("Hello ",name1)nput

x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))



def great(a,b,c):
    if a>b and a>c:
        print("The greatest number is ",a)
    elif b>a and b>c:
        print("The greatest number is ",b)
    else:
        print("the greatest number is ",c)
    
great(x,y,z)
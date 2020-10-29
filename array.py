class A:
    def Enter_record(self,n):
        Name=input("Enter employee name: ")
        Division=input("Enter Employee Division: ")
        Experiance=input("Enter Experiance of employee: ")
        Age=int(input("Enter AGe of employee: "))
        while Age>60 or Age<40:
            print("Wrong input: ")
            Age=int(input("Enter AGe of employee: "))
        if(Age>50 and Age<60):
            n=n+1
        return n
        
x=0
y=int(input("No. of employee: "))#By default given in question 10  but i want to take dynamic input
for i in range(y):
    Object=A()
    x=Object.Enter_record(x)
print(x)
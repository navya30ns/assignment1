#Fibonacci Series (THIRD PROGRAM)

num=int(input("Enter the number till which you want to generate fibonacci series: "))
count=0
n1=0
n2=1
if num<0:
    print("Invalid Input.")
elif num==0:
    print("Fibonacci: 0")
elif num==1:
    print(f"Fibonacci: {n1}")
else:
    print("Fibonacci series : ",end=" ")
    while count<num:
        print(n1,end=" ")
        n=n1+n2
        n1=n2
        n2=n
        count+=1
n=int(input("enter the number: "))
s=1
s1=0
k=n
while k>0:
    p=int(k%10)
    for i in range(1,p+1):
        s=s*i
        print(s)
    s1=s1+s
    s=1
    k=int(k/10)
if(n==s1):
    print("it is a krishnamurthy number")
else:
    print("it is not a krishnamurthy number")
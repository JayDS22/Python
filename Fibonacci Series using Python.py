#Fibonacci Series using Python 
#Fibonacci Series is Summation of two consecutive elements
def fibonaccii(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibonaccii(n-1)+fibonaccii(n-2))#Adding 2 consecutive Numbers

n=int(input())
print("Fibonacci Series: ",end='')#Prints the var. name
for n in range(0,n):
    print(fibonaccii(n),end='')#Prints the Numbers
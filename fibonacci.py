def generate_fibo(n):
    fibo_list=[]
    a=0
    b=1
    for i in range(n):
        fibo_list.append(a)
        a=b
        b=a+b
    return fibo_list

user_input=int(input("Enter the number of terms for the fibonacci sequence: "))

if user_input<=0:
    print("enter positive integer")
else:
    fibo_output = generate_fibo(user_input)
    print("Fibonacci Sequence: ",fibo_output)
    for i in fibo_output:
        print(i)
def generate_fact(n):
    fact=1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            fact = fact*i
    return fact

user_input=int(input("Enter a number to calculate factorial: "))

fact_val=generate_fact(user_input)
print(f"the factorial of {user_input} is ", fact_val)
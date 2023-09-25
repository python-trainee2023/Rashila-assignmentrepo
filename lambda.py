start = int(input("enter start value:"))
stop = int(input("enter stop value:"))


num_list = list(range (start, stop+1))
print(num_list)

even = sum(list(filter(lambda x: x % 2 == 0, num_list)))
odd = sum(list(filter(lambda x: x % 2 != 0, num_list)))

print("sum of even number", even)
print("sum of odd number", odd)
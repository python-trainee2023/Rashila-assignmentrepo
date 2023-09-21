int_list=[]
str_list=[]

userinput =input("Enter multiple values separated by ,")
inputlist =userinput.split(',')

for i in inputlist:
    if i.isdigit():
        int_list.append(int(i))
    else:
        str_list.append(i)
print(int_list)
print(str_list)
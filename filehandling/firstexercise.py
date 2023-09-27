
# class firstfile:
#     def __init__(self,filename,mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with firstfile("student.text",w) as f:
#     f.write("Name: Demo")

L = ["Name: Example\n", "Gender: Female\n", "Grade: High\n"]
with open('student.txt', 'w') as file:
   file.writelines(L)

content = open('student.txt', "r")
lines = content.readlines()
# print(lines)

f = open("newfile.txt", "w")
for line in lines:
    uppercase_line = line.upper()
    f.writelines([uppercase_line])


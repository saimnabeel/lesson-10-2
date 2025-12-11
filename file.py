file = open("text.txt" , 'r')

print("File In Read Mode--")

print(file.read())

file.close()

file1 = open("text.txt" , 'w')

print("File In Write Mode--")

file1.write("write somthing new")


file1.close()

file2 = open("text.txt" , 'a')

print("File In Append Mode--")

file2.write("if you forgot to write somthing you can append it\n")


file2.close()
"""Create a file using exact path"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file.txt",'x')
# file.write("new file")
# file.close()

"""Create a file using relative path"""
# import os
# file = open("Part 1(Python)/file3.txt",'x')
# file.write("new file")
# file.close()

"""Reading a file"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file2.txt",'r')
# print(file.read())
# file.close()

"""reading 5 characters"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file.txt",'r')
# print(file.read(5))
# file.close()

"""reading a line"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file2.txt",'r')
# print(file.readline())
# file.close()

"""reading 10 characters"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file2.txt",'r')
# print(file.readline(10))
# file.close()

"""reading all lines"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file2.txt",'r')
# print(file.readlines())
# file.close()

"""reading using loop"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file2.txt",'r')
# for line in file:
#   print(line, end='') #enter is already present at the end of line in file
# file.close()

"""writing"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file4.txt",'w')
# file.write("Writing in a file")
# file.close()

"""appending"""
# import os
# file = open("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file4.txt",'a')
# file.write("\nWriting in a file")
# file.close()

"""deleting a file"""
# import os
# if os.path.exists("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file4.txt"):
#   os.remove("C:/Users/prashant/Desktop/Data Science/Part 1(Python)/file4.txt")
# else:
#   print('file doesnot exists')

"""creating a folder"""
# import os
# os.mkdir("C:/Users/prashant/Desktop/Data Science/Part 2")

"""deleting a folder"""
# import os
# os.rmdir("C:/Users/prashant/Desktop/Data Science/Part 2")

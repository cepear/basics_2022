 # FILES:
 # CRUD - create(write to a file), read(get info from file), update (update file )
# Data handling files:
# txt for small size
# csv
#json
#xml  this 3 files used for outputs
#Yaml/yml

# Simple info files:
# documenting code executions
 # log
 # txt

# Coding:
#sql
#py
# java
# html
# rb
# sh
# bash
# bat (powershell in windows, batch script)
# application configuration files:
 # json
  # xml
  # .config

#user facing document:
# pdf
# docx
# excel
# txt

# Chapter 10 Files and Exceptions

# with open('filepath') as aliasnameForTheFile:
#     line1 = aliasnameForTheFile.readline()
#     line2 = aliasnameForTheFile.readline()
#     line3 = aliasnameForTheFile.readline()
#     line4 = aliasnameForTheFile.readline()
#
#     all_lines = aliasnameForTheFile.readlines()
#     file_content = aliasnameForTheFile.read()
#
#     closing_file = aliasnameForTheFile.close() # need to use only when opening file "with open()' method
#
filepath1 = '../data/products.txt'
filepath = 'c:/dev22/basics_2022/data/products.txt'
print("************************ READ File *************************")
with open(filepath) as prod_list:
    contents = prod_list.read()
    print("Content of the file 1 :\n", contents.strip())


with open(filepath) as prod_list:
    print('Now we are trying to loop through contents of file 1')
    all_lines = prod_list.readlines()
    print(all_lines)
print('Printing line 4 from file 1: ', all_lines[3])

for line in all_lines:
    print(line)

# with open(filepath, 'a') as prod_list:
#     contents = prod_list.read()
#     print("Content of the file :\n", contents)
#
# filepath2 = '../data/learning_python.txt'
# #filepath = 'c:/dev22/basics/data/products.txt'
#
# with open(filepath2) as prod_list:
#     contents = prod_list.read()
#     print("Content of the file 2 :\n", contents)
#
#
# with open(filepath2) as prod_list:
#     print('Now we are trying to loop through contents of file 2')
#     all_lines = prod_list.readlines()
#     print(all_lines)
# print('Printing line 3 from file 2: ',all_lines[3])
# for line in all_lines:
#     print(line)

# print("*************** WRITE file appending new content to file *****************")
# with open(filepath, 'a') as prod_list:
#     prod_list.write('spider jacket\n')
#     prod_list.write('batman jacket\n')
#     prod_list.write('superhero jacket\n')
#     prod_list.write('smart TV\n')
#     prod_list.write('bookshelf\n')
#     print("Content of the file 1 :\n", contents)

#print("*************** WRITE file with deleting existing content of the file*****************")
# with open(filepath, 'w') as prod_list:
#     prod_list.write('spider jacket')
#     prod_list.write('batman jacket')
#     prod_list.write('super hero jacket')
#     prod_list.write('spider jacket')
#     prod_list.write('spider jacket')
#     print("Content of the file 1 :\n", contents)
# HW 10.3 - 10.

print('-------------homework 10.1-----------')
filepath4 = '../data/learning_python.txt'
with open(filepath4, 'w') as learning_list:
    print('This is how I am expressing my love to python')
    learning_list.write('I like Python.\n')
    learning_list.write('Python is best for automation testing.\n')
    learning_list.write('I can automate my testing in Python.\n')
    learning_list.write('Python is the most popular among modern languages.\n')
    learning_list.write('I like to use Python for DB testing and DB analysis.\n')
    learning_list.write('I like my testing.\n')


with open(filepath4) as learning_list:
    contents4 = learning_list.read()
    print("Content of the contents4 is:\n", contents4)

print('Appending extra lines in the file')
with open(filepath4, 'a') as learning_list:
    learning_list.write('I like Programming.\n')
    learning_list.write('I love creating new codes.\n')
    print("Content of the contents4 is :\n", contents4)

message = "I really like Python."
message.replace('Python', 'Java')
with open(filepath4, 'a') as learning_list:
    learning_list.write(message)
    print("Content of the contents4 is :\n", contents4)

print("-----replacing word in the text and printing updated content----------")
with open(filepath4) as learning_list:
    contents4 = learning_list.read().replace('Python', 'Java')

with open(filepath4, 'a') as a:
    a.write(contents4)

print("Content of the contents4 is :\n", contents4)

# with open(filepath4, 'r') as r:
#     text = r.read().replace('Python', 'Java')
# with open(filepath4, 'a') as a:
#     a.write(text)


    # for a in learning_list:
    #     if a == 'Python':
    #         a == 'Java'
    #         print("Replaced words in file \n", contents4)











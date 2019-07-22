#file = open('sample.txt','r')
#contents = file.read()
#file.close()
#print(contents)

with open('file_example.txt', 'r') as file:
    contents = file.read()
print(contents)

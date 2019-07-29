filename = input("Enter file name to backup: ")

with open(filename, 'r') as inputfile, open(filename+'.bak', 'w') as outputfile:
    content = inputfile.read()
    outputfile.write(content)

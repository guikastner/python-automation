inputfile = open("inputFile.txt", "r")
for line in inputfile:
    line_split = line.split()
    if line_split[2] == "P":
        print (line)
    
print (inputfile.read())
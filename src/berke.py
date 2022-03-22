from sys import argv

# tokens
key = "BERK"
u_keywords = [x.upper() for x in key] # + ASCII
l_keywords = [x.lower() for x in key] # - ASCII

file = open(argv["1"], "r").read().split("\n")

commentLines = [] # this is comment line indexes
codeLines = [] # this is code line indexes
for i in range(len(file)):
    if file[i].startswith("BERKE"):
        commentLines.append(i)
    elif len(file[i]) == 0:
        pass
    else:
        codeLines.append(i)

codeLineCONTENT = []
for i in codeLines:
    codeLineCONTENT.append(file[i])

#print(commentLines)
#print(codeLines)

interpetedLines = []

for i in codeLineCONTENT:
    i = i.replace("B", "+1")\
            .replace("E", "+2")\
            .replace("R", "+3")\
            .replace("K", "+65")\
            .replace("b", "-1")\
            .replace("e", "-2")\
            .replace("r", "-3")\
            .replace("k", "-65")
    
    #print(eval(i))
    asd = eval(i)
    print(chr(asd))
    #print(i)

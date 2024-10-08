varList = []
varValue = []
line = []
controlCode = []
fileName = input()
file = open(fileName, "r")
def incr(varName):
    i = 0
    for y in varList:
        if y == varName:
            varValue[i] = varValue[i] + 1
            break
        else:
            i += 1
def decr(varName):
    i = 0
    for y in varList:
        if y == varName:
            varValue[i] -= 1
            break
        else:
            i += 1

def run(x):
    z = x.find(" ")
    while z == 0:
        x = x[z + 1:]
        z= x.find(" ")
    z = x.find(" ")
    controlKey = x[:z]
    controlCode.append(controlKey)
    w = x[z + 1:]
    p = w.find(" ")
    q = w.find(";")
    if p == -1 or p > q:
        varName = w[:q]
    else:
        varName = w[:p]
    match controlKey:
        case "clear":
            varList.append(varName)
            varValue.append(0)
        case "incr":
            incr(varName)
        case "decr":
            decr(varName)
        case "while":
            print(x)
            p = w.find(" ")
            w = w[p+5:]
            p = w.find(" ")
            w = int(w[:p])
            flag = False
            
            while True:
                for y in varList:
                    i = 0
                    if y == varName:
                        Varval = varValue[i]
                        break
                    else:
                        i += 1
                if Varval == w:
                    break
                if flag == False:
                    a = str(file.readline())
                    line.append(a)
                
                    
                else:
                    a = line[k -1]
                z = a.find(" ")
                while z == 0:
                    a = a[z + 1:]
                    z= a.find(" ")
            
                if a == "end;":
                    flag = False
                    k = len(line) - 2
                    while True:
                        if controlCode[k] == "while":
                            flag = True
                            k += 1
                            break
                        k -= 1
                    while k is not len(line):
                        
                        run(line[k])
                        k+= 1
                else:
                    run(a)
for x in file:
    line.append(x)
    run(x)

print(varList)
print(varValue)
file.close()
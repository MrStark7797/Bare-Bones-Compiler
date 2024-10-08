varList = []
varValue = []
stack = []
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
def addwhileLoop(x):
    whileStack = [x]
    cntrlKey = ""
    
    while True:
        a = str(file.readline())
        z = a.find(" ")     
        while z == 0:
            a = a[z + 1:]
            z= a.find(" ")
        cntrlKey = a[:z]
        if z == -1:
            break
        if cntrlKey == "while":
           a = addwhileLoop(a)
        whileStack.append(a)
    return whileStack
def clear(varName):
    found = False
    i = 0
    for x in varList:
        if x == varName:
            found = True
            varValue[i] = 0
        else:
            i += 1
    if found == False:
        varList.append(varName)
        varValue.append(0)

def run(pStack):
    for x in pStack:
        if type(x) == str:
            z = x.find(" ")
            while z == 0:
                x = x[z + 1:]
                z= x.find(" ")
            z = x.find(" ") 
            w = x[z + 1:]
            p = w.find(" ")
            q = w.find(";")
            if p == -1 or p > q:
                varName = w[:q]
            else:
                varName = w[:p]
            controlKey = x[:z]
            savedLine = x
            match controlKey:
                case "clear":
                    clear(varName)
                case "incr":
                    incr(varName)
                case "decr":
                    decr(varName)
                case "while":
                    p = w.find(" ")
                    w = w[p+5:]
                    p = w.find(" ")
                    w = int(w[:p])
                    i = 0
                    for y in varList:
                            
                        if y == varName:
                            Varval = varValue[i]
                            break
                        else:
                            i += 1
                    if varValue[i] == w:
                        return
                    check = varValue[i]
                    while varValue[i] != w:
                        for x in pStack:
                            j = 0
                            x == pStack[j]
                            if type(x) == str:
                                z = x.find(" ")
                                cntkey = x[:z]
                                if cntkey == "while":
                                    pStack.remove(x)
                                    break
                            else:
                                j += 1
                            
                        run(pStack)
                        pStack.insert(0, savedLine)
                        print(pStack)
                        if varValue[i] == w:
                            return


        else:
            run(x)
for x in file:
    z = x.find(" ")
    while z == 0:
        x = x[z + 1:]
        z= x.find(" ")
    z = x.find(" ") 
    controlKey = x[:z]
    w = x[z + 1:]
    p = w.find(" ")
    q = w.find(";")
    if controlKey != "while":
        stack.append(x)
    else:
        stack.append(addwhileLoop(x))

run(stack)
print(varList)
print(varValue)
file.close()
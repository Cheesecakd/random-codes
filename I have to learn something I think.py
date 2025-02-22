## This file reads umm A.txt, remove symbols, space, etc and make it only "-" in between, and put the output in B.txt

def main():
    original = open("A.txt","r", encoding="utf-8")
    olines = original.read()
    original.close()

    re_methods = [",",".","?","!","/","-","/","'","\"",":","(",")","“","”","’","="]
    re_layers = []
    for ite in range(len(re_methods)):
        if ite == 0:
            re_layers.append(olines.replace(re_methods[ite - 1]," "))
        else:
            re_layers.append(re_layers[ite - 1].replace(re_methods[ite - 1]," "))

    op1 = re_layers[len(re_layers)-1].strip().split(" ")
    mainop = []
    for str2 in op1:
        if str2 != "":
            mainop.append(str2)

    maintxt = ""
    for txt in mainop:
        maintxt += txt
        maintxt += "-"

    maintxt2 = maintxt[:len(maintxt)-1]

    new = open("B.txt","w")

    new.write(maintxt2)
    new.close()

main()

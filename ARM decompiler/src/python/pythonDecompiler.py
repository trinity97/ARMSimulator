import re
variableMap={"r0":"var0","r1":"var1","r2":"var2","r3":"var3","r4":"var4","r5":"var5","r6":"var6","r7":"var7","r8":"var8"}
allowedRegisters=["r0","r1","r2","r3","r4","r5","r6","r7","r8","r9","r10"]

file = open('F:\\Semester 3\\Computer Organization\\Project\\ARM decompiler\\input\\testCode.txt',"r")
temp=file.read()
temp=re.sub(",","",temp)
lines=temp.split('\n')
for k in range(len(lines)):
	lines[k]=lines[k].split()


for i in lines:
	if i[0]=="MOV":
		if i[2] in allowedRegisters:
			print(variableMap[i[1]]+"="+variableMap[i[2]])
		else:
			print(variableMap[i[1]]+"="+i[2][1:])
	if i[0]=="ADD":
		if i[3] in allowedRegisters:
			print(variableMap[i[1]]+"="+variableMap[i[2]]+"+"+variableMap[i[3]])
		else:
			print(variableMap[i[1]]+"="+variableMap[i[2]]+"+"+i[3][1:])
	if i[0]=="SWI":
		if i[1]=="0x6c":
			print("%(r0)s" % variableMap, end="")
			print("=int(input())")
		if i[1]=="0x11":
			break
		if i[1]=="0x6b":
			print("print(%(r1)s)" % variableMap)
	if i[0]=="SUB":
		if i[3] in allowedRegisters:
			print(variableMap[i[1]]+"="+variableMap[i[2]]+"-"+variableMap[i[3]])
		else:
			print(variableMap[i[1]]+"="+variableMap[i[2]]+"-"+i[3][1:])


file.close()
# print(file)
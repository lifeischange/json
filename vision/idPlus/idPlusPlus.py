# -*- coding: UTF-8 -*-
import os
# 获取当前目录的位置 \\转义字符

def idplus():
	path = os.getcwd()
	filePath = path+'\\'+'多轮.json'

	f = open(filePath, 'r', encoding='UTF-8')
	f1 = open(path+'\\'+"out.json", 'w', encoding='UTF-8')
	ID = open(path+'\\'+'id.csv','r',encoding='UTF-8')

#自动添加的id
	try:
		ids=ID.readlines()
		temp=ids[-1].strip()
		temp=int(temp)+50
	
	except:
		ids=[]
		temp = 10001
	

	ID.close()
	ID = open(path+'\\'+'id.csv','a+',encoding='UTF-8')
# for line in f.readlines():
	line = f.readline()
	while line:
		if('"taskName"' in line):
			ID.write('\n'+line.strip().rstrip(',')+'\n')
		if('"id":' in line):
		# while(temp in ids):
			# temp+=1
			f1.write('"id":'+str(temp)+',\n')
			ID.write(str(temp)+'\n')
			temp = temp+1
			#print(temp)
		else :
			f1.write(line)
		line = f.readline()
	f.close()
	f1.close()
	ID.close()
	#os.remove("../多轮.json")

    # print(line)
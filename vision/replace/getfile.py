#-*-coding:utf-8-*-

import shutil
import os
import re
import zipfile


#找到文件 本地运行
# class extract(object):

	# def path(self):
		# return os.getcwd()
		
	# def findfile(self):
		# print(self.path()+"\..")
		# files=os.listdir(self.path())#+"/../")
		# print(files)
		# mod=re.compile(r".*\.xmind$")
		# for file in files:
			# if re.search(mod,file):
				# shutil.copyfile(self.path()+"/../"+file,self.path()+"/../"+"123.rar")
				# with zipfile.ZipFile("../123.rar","r") as z:
					# z.extract("content.xml","../")
				#os.remove("../123.rar")
					
# if __name__=="__main__":
	# head=extract()
	# head.findfile()

class extract(object):

	def path(self):
		return os.getcwd()
		
		
	def findfile(self):
		files=os.listdir(self.path())
		#print(files)
		mod=re.compile(r".*\.xmind$")
		for file in files:
			if re.search(mod,file):
				#print(self.path()+"\\"+file)
				shutil.copyfile(self.path()+"\\"+file,self.path()+"\\"+"123.rar")
				with zipfile.ZipFile("123.rar","r") as z:
					z.extract("content.xml")
				os.remove("123.rar")

# if __name__=="__main__":
	# head=extract()
	# head.findfile()

	
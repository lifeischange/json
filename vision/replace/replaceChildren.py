#-*-coding:utf-8-*-


from getfile import extract
import re
from bs4 import BeautifulSoup as bs


#找到文件
# def subchild():
	# goal=extract()
	# goal.findfile()
	# with open("../content.xml","r",encoding="utf-8") as f:
		# temp=f.read()
		# content=re.sub("children","child",temp)
	# with open("../content.xml","w",encoding="utf-8") as f:
		# f.write(content)
		
# def subchild():
	# goal=extract()
	# goal.findfile()
	# with open("content.xml","r",encoding="utf-8") as f:
		# temp=f.read()
		# content=re.sub("children","child",temp)
	
	# with open("content.xml","w",encoding="utf-8") as f:
		# f.write(content)
def subchild():
	goal=extract()
	goal.findfile()
	with open("content.xml","r",encoding="utf-8") as f:
		temp=f.read()
		content=re.sub("children","child",temp)
	tree=bs(content,features="lxml-xml")
	with open("content.xml","w",encoding="utf-8") as f:
		f.write(tree.prettify())
		
#subchild()






	
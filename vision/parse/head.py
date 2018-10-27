#-*-coding:utf-8-*-

from bs4 import BeautifulSoup as bstree

#soup=bstree(open("content.xml","r",encoding="utf-8"),features="lxml")

#json头
#content=soup.sheet.topic
#print(content.prettify())

class xmltojson(object):
	def __init__(self,file):
		self.soup=bstree(open(file,"r",encoding="utf-8"),"lxml-xml")
		#from bs4.diagnose import diagnose
		#print(diagnose((open(file,"r",encoding="utf-8"))))
		
	#startup
	def startup(self):
		return self.soup.title.string.split()
	
	#xml头
	def head(self):
		#print(type(self.soup.sheet.topic))
		return self.soup.sheet.topic
	
	#taskname
	def taskName(self):
		return self.head().next_sibling.next_sibling.string.strip()
	
	#understanddefault的三句话	
	def understanddefault(self): 
		self.understands=self.head().find("notes",recursive=False).plain.string
		return self.understands.split()
		
	#finisheddefault	
	def finisheddefault(self): 
		return self.head().find("labels",recursive=False).label.string
		
	def tree(self):
		return self.soup
		
	
# if __name__=="__main__":
	# Head=xmltojson("../contents.xml")
	# print(Head.taskName())
	# print(type(Head.startup()))
	
	
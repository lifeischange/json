#-*-coding:utf-8-*-

from bs4 import BeautifulSoup as bstree

class getbody(object):
	def __init__(self,bst):#bst必须是beautifulsoup解析出来的树结构
		self.soup=bst

	def __call__(self):
		try:
			return self.soup.name
		except:
			return None
	
	#ask
	def ask(self):
		try:
			return self.soup.title.string.strip()		
		except:
			return None	
	
	#understand的三句话	
	def understand(self):
		try:
			return self.soup.topic.find("notes",recursive=False).plain.string.split()
		except:
			return None
		
		
	#match 返回的是list
	def matchlist(self):
		try:
			return self.soup.child.topics.find_all("topic",recursive=False)		#不能递归	
		except:
			return None
		
	#递归的结束点判断或填空	
	def endpoint(self):
		return self.soup.child.child
	
			
	def slot(self):
		if self.soup.child==None:
			return True
	def blank(self):
		if self.soup.child.title and self.soup.child.title.string.strip()=="":
			return True

			
	def origintree(self):
		return self.soup
		
	def match(self):
		try:
			return self.soup.parent.parent.parent.title.string.strip().split()			
		except:

			return None
			
	def name(self):
		return self.soup.title.string.strip()



		
		
	
	
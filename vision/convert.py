# -*- coding: UTF-8 -*-
#！/usr/bin/env python
import sys
import os
import json
import copy
sys.path.append(os.getcwd()+"//replace")
sys.path.append(os.getcwd()+"//parse")
sys.path.append(os.getcwd()+"//generatejson")
sys.path.append(os.getcwd()+"//idPlus")

from getfile import extract
from replace import replaceChildren
from parse import head,body
from generatejson import xjson
from idPlus import idPlusPlus

#解压文件
def madehead(jsontemplate):
	file=extract()
	file.findfile()
	replaceChildren.subchild()
#获取json头
	Head=head.xmltojson("content.xml")
	taskName=Head.taskName()
	startUp=Head.startup()
	try:
		understand_default=Head.understanddefault()
	except:
		understand_default=[
            "您可以输入“是”、“否”告知我您的选择。",
            "请您输入“是”、“否”告知我您的选择。",
            "这个问题我记下了。咱们聊点别的吧。"
        ]
	try:
		finished_default=Head.finisheddefault()
	except:
		finished_default=["感谢您的使用，祝您生活愉快！"]
	
	content=jsontemplate.jsonhead(taskName,startUp,understand_default,finished_default)
	return content,Head.tree().topic.topic.extract()
	
		
#写入文件内
def writefile(dict):
	with open("多轮.json","w",encoding="utf-8") as f:
		f.write(json.dumps(dict,ensure_ascii=False,indent=4))
		
#标注id
def addid():
	ids=idPlusPlus.idplus()
#递归读取并写入
def generate(export,importNode,jsontemplate):
	#print(importNode.name())
	if importNode.slot():
		if importNode.match():
			temp=jsontemplate.end(finished=importNode.ask().split(),match=importNode.match())
			#print(temp)
		else:
			temp=jsontemplate.end(finished=importNode.ask().split())
			
		export.append(temp)	
		return None
		
	if importNode.match()==None:
		temp=jsontemplate.answer("single",ask=importNode.ask())
	else:
		temp=jsontemplate.answer("single",ask=importNode.ask(),match=importNode.match())
	export.append(temp)	
	#print(temp)
	
	for node_match in importNode.matchlist():#遍历match
		match_func=body.getbody(node_match)
		if match_func.matchlist() == None:
			temp=jsontemplate.end()
			#print(temp)
			export[-1]["answer"].append(temp)#这里一定要使用-1.用1会报错
		elif len(match_func.matchlist())>1:
			temp=jsontemplate.answer("multi",match=node_match.title.string.strip().split())
			export[-1]["answer"].append(temp)
			index=0
			for node_question in match_func.matchlist():#遍历next——question
				new_node_question=copy.copy(node_question)
				new_tree=body.getbody(new_node_question)
				generate(export[-1]["answer"][0]["answer"],new_tree,jsontemplate)
				# print(json.dumps(export[0]["answer"][0]["answer"],ensure_ascii=False,indent=4))
				# if index==2:
					# exit("跳出")
				# index+=1
				
			
	
		else:
			subtree=body.getbody(node_match.child.topic)
			generate(export[-1]["answer"],subtree,jsontemplate)
		
	
	

if __name__=="__main__":
	function=xjson.makejson()
	list,tree=madehead(function)
	#print(tree.parent)
	sons=body.getbody(tree)
	generate(list["data"]["tasks"]["answer"],sons,function)
	writefile(list)
	addid()
	os.remove("多轮.json")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

#-*-coding:utf-8-*-


#找到文件
class makejson(object):
	#建立新文件
	def __init__(self):
		self.content={
    "edit": "0",
    "type": "tasks",
    "data": {
        "taskName": "青年创业一次性开办费扶持政策",
        "matchs": {},
        "processes": [],
        "startUp": [
            "青年创业一次性开办费扶持政策",
            "我要办理青年创业一次性开办费扶持政策"
        ],
        "understand_default": [
            "您可以输入“是”、“否”告知我您的选择。",
            "请您输入“是”、“否”告知我您的选择。",
            "这个问题我记下了。咱们聊点别的吧。"
        ],
        "finished_default": [
            "感谢您的使用，祝您生活愉快！"
        ],
        "tasks": {
			"id":11428,
            "name": "青年创业一次性开办费扶持政策",
            "state": "wait",
            "type": "multi",
            "answer": [
            ]
        }
    }
}
		
	#写文件头
	def jsonhead(self,taskName,startUp,understand_default,finished_default):
		self.content["data"]["taskName"]=taskName
		self.content["data"]["startUp"]=startUp
		self.content["data"]["understand_default"]=understand_default
		self.content["data"]["finished_default"]=finished_default
		self.content["data"]["tasks"]["name"]=taskName
		return self.content
		
	#写answer
	def answer(self,type,**kw):
		answer=   {
							"id":11430,
                            "name": "信用代码合格",
                            "state": "wait"  
                        }
		
		
		answer["type"]=type
		for key in kw:
			answer[key]=kw[key]
		answer["answer"]=[]
		return answer
	
	#写结束节点
	def end(self,**kw):
		answer=   {
							"id":11430,
                            "name": "信用代码合格",
                            "state": "wait",
                            "isLeaf": True
                        }
		answer["match"]=[]
		for key in kw:
			answer[key]=kw[key]
		return answer
					
# if __name__=="__main__":
	# head=extract()
	# head.findfile()





	
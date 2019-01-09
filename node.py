class Node:
	def __init__(self, char):
		self.char=char
		self.nodes=[]
		self.nodeChars=[]
		self.root=None
		self.endNode=False
		self.dic={}

	def addLink(self,node):
		self.nodes.append(node)
		self.nodeChars.append(node.char)
		return(node)

	def getNode(self,char):
		for x in range(0,len(self.nodeChars)):
			if self.nodeChars[x] == char:
				return(self.nodes[x])
		return None

	def addWord(self,word):
		if len(word)==0:
			self.endNode=True
			return
		else:
			r=self.addLink(newNode(word[0],self.root))
			r.addWord(word[1:len(word)])

	def findWord(self,word):
		if len(word)==0:
			return self
		else:
			query=word[0]
			for x in range(0,len(self.nodeChars)):
				if(self.nodeChars[x]==query):
					return(self.nodes[x].findWord(word[1:len(word)]))
			return None
	def newWord(self,word):
		if len(word)==0:
			self.endNode=True
			return
		else:
			query=word[0]
			for x in range(0,len(self.nodeChars)):
				if(self.nodeChars[x]==query):
					self.nodes[x].newWord(word[1:len(word)])
					return
			self.addWord(word)

def newNode(char,root):
	node=Node(char)
	node.root=root
	return(node)

def printNode(root,tabs=0,word=""):
	st=""
	word+=root.char
	for x in range(0, tabs):
		st+="  "
	st+="|-" +word
	print(st)
	for x in range(0,len(root.nodes)):
		printNode(root.nodes[x],tabs+1,word)

def buildTree(root,lis):
	root.dic={}
	for word in lis:
		root.dic[word]=0
		root.newWord(word)

def countHits(root,stream):
	hits=0
	pointer=root
	index=0
	while index<len(stream):
		nex=pointer.getNode(stream[index:index+1])
		if nex is not None:
			pointer=nex
			index+=1
		else:
			if pointer is root:
				index+=1
			pointer=root
		if pointer.endNode is True:
			hits+=1
	if pointer.endNode is True:
		hits+=0
	return(hits)

def main():
	a=Node('\n')
	a.root=a
	buildTree(a,["james","leonard","jamesxxx","baker","baykey"])
	print(countHits(a,"james leonard jamesxxx"))
	#printNode(a)

if __name__ == '__main__':
	main()
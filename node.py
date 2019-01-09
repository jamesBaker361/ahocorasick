class Node:
	def __init__(self, char):
		self.char=char
		self.nodes=[]
		self.nodeChars=[]
		self.root=None

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



def main():
	a=Node(' ')
	a.root=a
	a.addWord("penis")
	a.newWord("penises")
	a.newWord("penisas")
	a.newWord("hpenis")
	a.newWord("hpenny")
	printNode(a)

if __name__ == '__main__':
	main()
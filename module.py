import sys														#Here I am importing modules by which concept of modularity is satisfied.
from random import randrange

move=''
coinslist=[]
xx=0

class Person:														#The Parent class
	def __init__(self,x,y):												#A class itself is encapsulated with data and functions.So, encapsulation is sati															  sfied here
		self.score=0
		self.x=x
		self.y=y

	def position(self):
		return (self.x,self.y)

	def changeposition(self,x,y):
		self.x=x
		self.y=y

	def printscore(self):
		return self.score
	
	global coinslist
	global board

	def setscore(self,u):
		self.score=u
	
	def collectCoin(self):												#The function that has to be implemented
		self.score=self.score+1
		
	def moveright(self,r,e):
		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
		 	self.x=a
			if(b!=34):
			 	self.y=b+1
				if(board[self.x][self.y] == "C"):
					self.collectCoin()
					board[self.x][self.y]="P"
					board[a][b]="."
					if (self.x,self.y) in coinslist:
						coinslist.remove((self.x,self.y))
						if coinslist == []:
							arrangeboard()
							initialprintboard()
				elif(checkWall(self.x,self.y) == 1):
					board[a][b]="."
					board[self.x][self.y]="P"
					self.changeposition(a,b+1)
				else:
				 	self.changeposition(a,b)
						
	def moveleft(self,r,e):
		 (a,b)=self.position()
		 if(a<15 and b<35 and a>=0 and b>=0):
		 	self.x=a
			if(b!=0):
				self.y=b-1
				if(board[self.x][self.y] == "C"):
					self.collectCoin()
					board[self.x][self.y]="P"
					board[a][b]="."
					if (self.x,self.y) in coinslist:
						coinslist.remove((self.x,self.y))
						if coinslist == []:
							arrangeboard()
							initialprintboard()
				elif(checkWall(self.x,self.y) == 1):
					board[a][b]="."
					board[self.x][self.y]="P"
					self.changeposition(a,b-1)
				else:
					self.changeposition(a,b)
		 		
	def moveup(self,r,e):
		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
			self.y=b
			if(a!=0):
				self.x=a-1
				if(board[self.x][self.y] == "C"):
					self.collectCoin()
					board[self.x][self.y]="P"
					board[a][b]="."
					if (self.x,self.y) in coinslist:
						coinslist.remove((self.x,self.y))
						if coinslist == []:
							arrangeboard()
							initialprintboard()
				elif(checkWall(self.x,self.y) ==1):
					board[a][b]="."
					board[self.x][self.y]="P"
	 	                        self.changeposition(a-1,b)
				else:
					self.changeposition(a,b)
		

	def movedown(self,r,e):
		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
			self.y=b
			if(a!=14):
				self.x=a+1
				if(board[self.x][self.y] == "C"):
					self.collectCoin()
					board[self.x][self.y]="P"
					board[a][b]="."
					if (self.x,self.y) in coinslist:
						coinslist.remove((self.x,self.y))
						if coinslist == []:
							arrangeboard()
							initialprintboard()
				elif(checkWall(self.x,self.y) == 1):
					board[a][b]="."
					board[self.x][self.y]="P"
	                                self.changeposition(a+1,b)
				else:
					self.changeposition(a,b)
		


class Pacman(Person):												#The concept of inheritence is satisfied here
														#A class itself is encapsulated with data and functions.So, encapsulation is sati													                  sfied here

	def __init__(self,x,y,i):
		Person.__init__(self,x,y)
		self.score=i


class Ghost(Person):												#The concept of inheritence is satisfied here
	def __init__(self,x,y):
		Person.__init__(self,x,y)					

	def moveright(self,r,e):										#The concept of polymorphism is satisfied here I am over-riding the method moveright() in 														  ghost sub-class instead using that of parent class method
		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
			self.x=a
			if(b!=34):
				self.y=b+1
				if(board[self.x][self.y] == "C"):
					if(self.x,self.y) not in coinslist:
						board[a][b]="."
						board[self.x][self.y]="G"
					else:
						board[a][b]="."
						board[self.x][self.y]="G"
					self.changeposition(a,b+1)
				elif(board[self.x][self.y] != "X"):
					board[a][b]="."
					board[self.x][self.y]="G"
					self.changeposition(a,b+1)
				else:
					self.changeposition(a,b)
					if(e==2):
						self.movedown(1,0)
					elif(e==1):
						self.moveup(1,0)
					elif(e==0):
						self.moveleft(1,-1)
					else:
						self.changeposition(a,b)
		if(r==1):
			if (a,b) in coinslist:
				board[a][b]="C"

	def moveleft(self,r,e):											#The concept of polymorphism is satisfied here by over-riding the methodleft() different 														  from that of parent class function
		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
			self.x=a
			if(b!=0):
				self.y=b-1
				if(board[self.x][self.y] == "C"):
					if(self.x,self.y) not in coinslist:
						board[a][b]="."
						board[self.x][self.y]="G"
					else:
						board[a][b]="."
						board[self.x][self.y]="G"
					self.changeposition(a,b-1)
				elif(board[self.x][self.y] !="X"):
					board[a][b]="."
					board[self.x][self.y]="G"
					self.changeposition(a,b-1)
				else:
					self.changeposition(a,b)
					if(e==2):
						self.movedown(1,0)
					elif(e==1):
						self.moveup(1,0)
					elif(e==0):
						self.moveright(1,-1)
					else:
						self.changeposition(a,b)
	        if(r==1):
			if (a,b) in coinslist:
				board[a][b]="C"
	
	def moveup(self,r,e):   										 #The concept of polymorphism is satisfied here by over-riding the methodup() different                                                                                                                    from that of parent class function
		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
			self.y=b 
			if(a!=0):
				self.x=a-1
				if(board[self.x][self.y] == "C"):
					if(self.x,self.y) not in coinslist:
						board[a][b]="."
						board[self.x][self.y]="G"
					else:   
						board[a][b]="."
						board[self.x][self.y]="G"
				        self.changeposition(a-1,b)
				elif(board[self.x][self.y] !="X"):
					board[a][b]="."
					board[self.x][self.y]="G"
					self.changeposition(a-1,b)
				else:
					self.changeposition(a,b)
					if(e==2):
						self.moveright(1,0)
					elif(e==1):
						self.moveleft(1,0)
					elif(e==0):
						self.movedown(1,-1)
					else:
						self.changeposition(a,b)
		if(r==1):
			if (a,b) in coinslist:
				board[a][b]="C"

	def movedown(self,r,e): 										 #The concept of polymorphism is satisfied here by over-riding the methoddown() different                                                                                                                  from that of parent class function

		(a,b)=self.position()
		if(a<15 and b<35 and a>=0 and b>=0):
			self.y=b 
			if(a!=14):
				self.x=a+1
				if(board[self.x][self.y] == "C"):
					if(self.x,self.y) not in coinslist:
						board[a][b]="."
						board[self.x][self.y]="G"
					else:   
						board[a][b]="."
						board[self.x][self.y]="G"
					self.changeposition(a+1,b)
				elif(board[self.x][self.y] !="X"):
					board[a][b]="."
					board[self.x][self.y]="G"
					self.changeposition(a+1,b)
				else:
					self.changeposition(a,b)
					if(e==2):
						self.moveright(1,0)
					elif(e==1):
						self.moveleft(1,0)
					elif(e==0):
						self.moveup(1,-1)
					else:
						self.changeposition(a,b)
		if(r==1):
			if (a,b) in coinslist:
				board[a][b]="C"






def ghostmovement(ghost,i,o,u,p):
	global board
	if((i-o)==0 and (u-p)==0):
		for a in xrange(15):
			for b in xrange(35):
				if(board[a][b]=="P"):
					board[a][b]="G"
				sys.stdout.write(board[a][b]+" ")
			sys.stdout.write("\n")
		sys.stdout.write("Score : "+str(pacman.printscore()))
		sys.stdout.write("\n")
		sys.exit(0)
	elif((i-o)>=0 and (u-p)>=0):
		if((i-o)>=(u-p)):
			ghost.movedown(1,2)
		else:
			ghost.moveright(1,2)
	elif((i-o)<=0 and (u-p)>=0):
		if((o-i)>=(u-p)):
			ghost.moveup(1,2)
		else:
			ghost.moveright(1,1)
	elif((i-o)>=0 and (u-p)<=0):
		if((i-o)>=(p-u)):
			ghost.movedown(1,1)
		else:
			ghost.moveleft(1,2)
	elif((i-o)<=0 and (u-p)<=0):
		if((o-i)>= (p-u)):
			ghost.moveup(1,1)
		else:
			ghost.moveleft(1,1)

			
def initialprintboard():
	global coinslist
	global board
	global move
	global coinslist
	for a in xrange(15):
		for b in xrange(35):
			sys.stdout.write(board[a][b]+" ")
		sys.stdout.write("\n")	
	print "Score : "+str(pacman.printscore())
	(o,p)=ghostPosition()
	(o1,p1)=ghostPosition1()
	(i,u)=pacman.position()
	if(checkGhost() == 0):
		sys.exit(0)
	if(checkGhost1() == 0):
		sys.exit(0)
	sys.stdout.write("Enter move: ")
	move=raw_input()
	if(move == "q"):
		sys.exit(0)
	if(move == "d"):
		pacman.moveright(0,0)
		(i,u)=pacman.position()
		ghostmovement(ghost,i,o,u,p)
		ghostmovement(ghost1,i,o1,u,p1)
		initialprintboard()
	elif(move == "a"):
	  	pacman.moveleft(0,0)
		(i,u)=pacman.position()
		ghostmovement(ghost,i,o,u,p)
		ghostmovement(ghost1,i,o1,u,p1)
		initialprintboard()
	elif(move == "w"):
	  	pacman.moveup(0,0)
	   	(i,u)=pacman.position()
	  	ghostmovement(ghost,i,o,u,p)
		ghostmovement(ghost1,i,o1,u,p1)
		initialprintboard()
	elif(move == "s"):
	  	pacman.movedown(0,0)
	  	(i,u)=pacman.position()
		ghostmovement(ghost,i,o,u,p)
		ghostmovement(ghost1,i,o1,u,p1)
		initialprintboard()
	else:
		print "Invalid Input"
		initialprintboard()
				
board=[['.' for x in xrange(35)] for x in xrange(15)]

def randomgenerator(x):
	return randrange(x)

pacmanp=()
ghostp=()
ghost1p=()
def arrangeboard():
      	global board
	global pacmanp
	global ghostp
	global ghost1p
	for a in xrange(15):
		for b in xrange(35):
			board[a][b]="."
	for a in xrange(15):
		if a<5 or a>6:
			board[a][11]="X"
		board[8][15]="."
		board[5][18]="."
		d=randomgenerator(34)
		board[a][d]="C"
		coinslist.append((a,d))
		board[a][14]="C"
		coinslist.append((a,14))
	for a in xrange(10):
		board[8][a]="X"
	for a in xrange(12,20):
		board[8][a]="X"
	for a in xrange(21,35):
		board[8][a]="X"
	d=randomgenerator(14)
	e=randomgenerator(34)
	if(board[d][e] != "X"):
		board[d][e]="P"
		pacmanp=(d,e)
	else:
		board[1][5]="P"
		pacmanp=(1,5)
	d=randomgenerator(14)
	e=randomgenerator(34)
	if(board[d][e] != "X"):
		board[d][e]="G"
		ghostp=(d,e)
	else:   
		board[11][15]="G"
		ghostp=(11,15)
	d=randomgenerator(14)
	e=randomgenerator(34)
	if(board[d][e] != "X"):
		board[d][e]="G"
		ghost1p=(d,e)
	else:   
		board[10][34]="G"
		ghost1p=(10,34)
	global pacman
	global ghost
	global ghost1
	global xx
	xx=xx+1
	livescore=0
	if xx>1:
		livescore=pacman.score
	pacman=Pacman(pacmanp[0],pacmanp[1],livescore)
	ghost=Ghost(ghostp[0],ghostp[1])
	ghost1=Ghost(ghost1p[0],ghost1p[1])
	 

def ghostPosition():													#The function that has to be implemented
	return ghost.position()

def ghostPosition1():
	return ghost1.position()

def checkGhost():													#The function that has to be implemented
	(q,w)=pacman.position()
	(c,v)=ghost.position()
	if((q-c)==0 and (w-v)==0):
		return 0
	else:
	 	return 1

def checkGhost1():
	(q,w)=pacman.position()
	(c,v)=ghost1.position()
	if((q-c)==0 and (w-v)==0):
		return 0
	else:   
		return 1

def checkWall(t,y):
	global board
	if(board[t][y] !="X"):
		return 1
	else:
		return 0
		
pacman=object()
ghost=object()
ghost1=object()

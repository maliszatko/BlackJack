from random import randint
from graphics import *

class _BBox(GraphicsObject):
    # Internal base class for objects represented by bounding box
    # (opposite corners) Line segment is a degenerate case.
    
    def __init__(self, p1, p2, options=["outline","width","fill"]):
        GraphicsObject.__init__(self, options)
        self.p1 = p1.clone()
        self.p2 = p2.clone()

    def _move(self, dx, dy):
        self.p1.x = self.p1.x + dx
        self.p1.y = self.p1.y + dy
        self.p2.x = self.p2.x + dx
        self.p2.y = self.p2.y  + dy
                
    def getP1(self): return self.p1.clone()

    def getP2(self): return self.p2.clone()
    
    def getCenter(self):
        p1 = self.p1
        p2 = self.p2
        return Point((p1.x+p2.x)/2.0, (p1.y+p2.y)/2.0)


class Player(GraphWin,_BBox):
	'''
	Player setup is a list of two tuples
	First number in a tuple stands for Suits (1 - is Clubs, 2 - is Diamonds, 3 - is Hearts, 4 - is Spades)
	Second number stands for Figures (2-10 is normal, 11 is Jack, 12 is Queen, 13 is King and 14 is Ace)
	'''
	def __init__(self):
		self.setup=[]

	def won(self,value):
		'''
		adds given value to players balance
		'''
		self.balance=self.balance + value

	def set(self):
		self.setup=[(randint(1,4),randint(2,14)),(randint(1,4),randint(2,14))]

	def bet(self,value):
		'''
		checks if player can bet given value - if he can reduces this ammount by given value and returns True
		'''
		if value > self.balance:
			return False
		else: 
			self.balance=self.balance - value
			return True
	def hit(self):
		'''
		returns a new tuple list - appended tuple is a new card 
		'''
		return self.setup.append((randint(1,4),randint(2,14)))

	def count(self):
		card_sum=0
		for suit,figure in self.setup:
			if 14 > figure > 10:
				figure=10
			elif figure == 14:
				if card_sum + 11 > 21:
					figure = 1
				else:
					figure = 11
			card_sum=card_sum+figure
		return card_sum

	def draw(self,win):
		'''
		draws players deck to the screen
		'''
		dx=0
		for suit,figure in self.setup:
			self.card_outline=Rectangle(Point(50+dx,800),Point(100+dx,700))
			self.card_outline.setFill(color_rgb(255,255,255))
			self.card_outline.draw(win)
			if suit == 1: # Clubs
				self.circle1 = Circle(Point(75+dx,735),6)
				self.circle2 = Circle(Point(70+dx,742),6)
				self.circle3 = Circle(Point(80+dx,742),6)
				self.circle1.setFill('black')
				self.circle2.setFill('black')
				self.circle3.setFill('black')
				self.triangle=Polygon(Point(75+dx,742),Point(73+dx,755),Point(77+dx,755))
				self.triangle.setFill('black')
				self.circle3.draw(win)
				self.circle2.draw(win)
				self.circle1.draw(win)
				self.triangle.draw(win)
				if figure == 11:
					self.txt=Text(Point(75+dx,770),'J')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 12:
					self.txt=Text(Point(75+dx,770),'Q')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 13:
					self.txt=Text(Point(75+dx,770),'K')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 14:
					self.txt=Text(Point(75+dx,770),'A')
					self.txt.draw(win)
					self.txt.setSize(18)
				else:
					self.txt=Text(Point(75+dx,770),f'{figure}')
					self.txt.draw(win)
					self.txt.setSize(18)

			elif suit == 2: # Diamonds
				self.card_suit=Polygon(Point(75+dx,725),Point(65+dx,740),Point(75+dx,755),Point(85+dx,740))
				self.card_suit.setFill(color_rgb(255,0,0))
				self.card_suit.draw(win)
				if figure == 11:
					self.txt=Text(Point(75+dx,770),'J')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 12:
					self.txt=Text(Point(75+dx,770),'Q')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 13:
					self.txt=Text(Point(75+dx,770),'K')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 14:
					self.txt=Text(Point(75+dx,770),'A')
					self.txt.draw(win)
					self.txt.setSize(18)
				else:
					self.txt=Text(Point(75+dx,770),f'{figure}')
					self.txt.draw(win)
					self.txt.setSize(18)

			elif suit == 3: # Hearts
				self.circle1=Circle(Point(70+dx,730),6)
				self.circle2=Circle(Point(80+dx,730),6)
				self.triangle=Polygon(Point(64+dx,732),Point(86+dx,732),Point(75+dx,750))
				self.circle2.setFill(color_rgb(255,0,0))
				self.circle2.setOutline(color_rgb(255,0,0))
				self.circle1.setFill(color_rgb(255,0,0))
				self.circle1.setOutline(color_rgb(255,0,0))
				self.triangle.setFill(color_rgb(255,0,0))
				self.triangle.setOutline(color_rgb(255,0,0))
				self.circle1.draw(win)
				self.circle2.draw(win)
				self.triangle.draw(win)
				if figure == 11:
					self.txt=Text(Point(75+dx,770),'J')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 12:
					self.txt=Text(Point(75+dx,770),'Q')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 13:
					self.txt=Text(Point(75+dx,770),'K')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 14:
					self.txt=Text(Point(75+dx,770),'A')
					self.txt.draw(win)
					self.txt.setSize(18)
				else:
					self.txt=Text(Point(75+dx,770),f'{figure}')
					self.txt.draw(win)
					self.txt.setSize(18)

			elif suit == 4: # Spades
				self.triangle1=Polygon(Point(75+dx,725),Point(63+dx,740),Point(87+dx,740))
				self.triangle1.setFill('black')
				self.circle1=Circle(Point(70+dx,740),6)
				self.circle1.setFill('black')
				self.circle2=Circle(Point(80+dx,740),6)
				self.circle2.setFill('black')
				self.triangle2=Polygon(Point(75+dx,747),Point(73+dx,750),Point(77+dx,750))
				self.triangle2.setFill('black')
				self.triangle2.draw(win)
				self.triangle1.draw(win)
				self.circle2.draw(win)
				self.circle1.draw(win)
				if figure == 11:
					self.txt=Text(Point(75+dx,770),'J')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 12:
					self.txt=Text(Point(75+dx,770),'Q')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 13:
					self.txt=Text(Point(75+dx,770),'K')
					self.txt.draw(win)
					self.txt.setSize(18)
				elif figure == 14:
					self.txt=Text(Point(75+dx,770),'A')
					self.txt.draw(win)
					self.txt.setSize(18)
				else:
					self.txt=Text(Point(75+dx,770),f'{figure}')
					self.txt.draw(win)
					self.txt.setSize(18)

			dx=dx+100

class Computer(GraphWin,_BBox):
	def __init__(self):
		self.setup=[]

	def set(self):
		self.setup=[(randint(1,4),randint(2,14)),(randint(1,4),randint(2,14))]
		
	def hit(self):
		'''
		returns a new tuple list - appended tuple is a new card 
		'''
		return self.setup.append((randint(1,4),randint(2,14)))

	def count(self):
		card_sum=0
		for suit,figure in self.setup:
			if 14 > figure > 10:
				figure=10
			elif figure == 14:
				if card_sum + 11 > 21:
					figure = 1
				else:
					figure = 11
			card_sum=card_sum+figure
		return card_sum

	def decide(self):
		if self.count() == 16 or self.count() == 17:
			shuff=randint(1,2)
			if shuff == 1:
				return 'hit'
			else:
				return 'stay'
		elif self.count() == 18:
			shuff=randint(1,3)
			if shuff == 1:
				return 'hit'
			else:
				return 'stay'
		elif self.count() == 19:
			shuff=randint(1,4)
			if shuff == 1:
				return 'hit'
			else:
				return 'stay'
		elif self.count() <= 15:
			return 'hit'
		else:
			return 'stay'


	def draw(self,win):
		'''
		draws computer deck to the screen - it skips the first card, making in uknown to the
		player
		'''
		card_outline=Rectangle(Point(50,400),Point(100,300))
		card_outline.setFill(color_rgb(255,255,255))
		card_outline.draw(win)
		txt=Text(Point(75,350),"?")
		txt.setSize(30)
		txt.draw(win)
		dx=100
		for suit,figure in self.setup[1:]:
			card_outline=Rectangle(Point(50+dx,400),Point(100+dx,300))
			card_outline.setFill(color_rgb(255,255,255))
			card_outline.draw(win)
			if suit == 1: # Clubs
				circle1 = Circle(Point(75+dx,335),6)
				circle2 = Circle(Point(70+dx,342),6)
				circle3 = Circle(Point(80+dx,342),6)
				circle1.setFill('black')
				circle2.setFill('black')
				circle3.setFill('black')
				triangle=Polygon(Point(75+dx,342),Point(73+dx,355),Point(77+dx,355))
				triangle.setFill('black')
				circle3.draw(win)
				circle2.draw(win)
				circle1.draw(win)
				triangle.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)


			elif suit == 2: # Diamonds
				card_suit=Polygon(Point(75+dx,325),Point(65+dx,340),Point(75+dx,355),Point(85+dx,340))
				card_suit.setFill(color_rgb(255,0,0))
				card_suit.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)

			elif suit == 3: # Hearts
				circle1=Circle(Point(70+dx,330),6)
				circle2=Circle(Point(80+dx,330),6)
				triangle=Polygon(Point(64+dx,332),Point(86+dx,332),Point(75+dx,350))
				circle2.setFill(color_rgb(255,0,0))
				circle2.setOutline(color_rgb(255,0,0))
				circle1.setFill(color_rgb(255,0,0))
				circle1.setOutline(color_rgb(255,0,0))
				triangle.setFill(color_rgb(255,0,0))
				triangle.setOutline(color_rgb(255,0,0))
				circle1.draw(win)
				circle2.draw(win)
				triangle.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)

			elif suit == 4: # Spades
				triangle1=Polygon(Point(75+dx,325),Point(63+dx,340),Point(87+dx,340))
				triangle1.setFill('black')
				circle1=Circle(Point(70+dx,340),6)
				circle1.setFill('black')
				circle2=Circle(Point(80+dx,340),6)
				circle2.setFill('black')
				triangle2=Polygon(Point(75+dx,347),Point(73+dx,350),Point(77+dx,350))
				triangle2.setFill('black')
				triangle2.draw(win)
				triangle1.draw(win)
				circle2.draw(win)
				circle1.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)

			dx=dx+100
	def drawall(self,win):
		'''
		draws computer deck to the screen - it skips the first card, making in uknown to the
		player
		'''
		dx=0
		for suit,figure in self.setup:
			card_outline=Rectangle(Point(50+dx,400),Point(100+dx,300))
			card_outline.setFill(color_rgb(255,255,255))
			card_outline.draw(win)
			if suit == 1: # Clubs
				circle1 = Circle(Point(75+dx,335),6)
				circle2 = Circle(Point(70+dx,342),6)
				circle3 = Circle(Point(80+dx,342),6)
				circle1.setFill('black')
				circle2.setFill('black')
				circle3.setFill('black')
				triangle=Polygon(Point(75+dx,342),Point(73+dx,355),Point(77+dx,355))
				triangle.setFill('black')
				circle3.draw(win)
				circle2.draw(win)
				circle1.draw(win)
				triangle.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)


			elif suit == 2: # Diamonds
				card_suit=Polygon(Point(75+dx,325),Point(65+dx,340),Point(75+dx,355),Point(85+dx,340))
				card_suit.setFill(color_rgb(255,0,0))
				card_suit.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)

			elif suit == 3: # Hearts
				circle1=Circle(Point(70+dx,330),6)
				circle2=Circle(Point(80+dx,330),6)
				triangle=Polygon(Point(64+dx,332),Point(86+dx,332),Point(75+dx,350))
				circle2.setFill(color_rgb(255,0,0))
				circle2.setOutline(color_rgb(255,0,0))
				circle1.setFill(color_rgb(255,0,0))
				circle1.setOutline(color_rgb(255,0,0))
				triangle.setFill(color_rgb(255,0,0))
				triangle.setOutline(color_rgb(255,0,0))
				circle1.draw(win)
				circle2.draw(win)
				triangle.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)

			elif suit == 4: # Spades
				triangle1=Polygon(Point(75+dx,325),Point(63+dx,340),Point(87+dx,340))
				triangle1.setFill('black')
				circle1=Circle(Point(70+dx,340),6)
				circle1.setFill('black')
				circle2=Circle(Point(80+dx,340),6)
				circle2.setFill('black')
				triangle2=Polygon(Point(75+dx,347),Point(73+dx,350),Point(77+dx,350))
				triangle2.setFill('black')
				triangle2.draw(win)
				triangle1.draw(win)
				circle2.draw(win)
				circle1.draw(win)
				if figure == 11:
					txt=Text(Point(75+dx,370),'J')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 12:
					txt=Text(Point(75+dx,370),'Q')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 13:
					txt=Text(Point(75+dx,370),'K')
					txt.draw(win)
					txt.setSize(18)
				elif figure == 14:
					txt=Text(Point(75+dx,370),'A')
					txt.draw(win)
					txt.setSize(18)
				else:
					txt=Text(Point(75+dx,370),f'{figure}')
					txt.draw(win)
					txt.setSize(18)

			dx=dx+100

class Stay_Button(GraphWin,_BBox):

	def __init__(self,p1,p2):
		self.p1=Point(p1.x,p1.y)
		self.p2=Point(p2.x,p2.y)

	def draw(self,win):
		rectangle=Rectangle(self.p1,self.p2)
		rectangle.setFill(color_rgb(0,255,0))
		rectangle.setOutline(color_rgb(255,0,0))
		rectangle.draw(win)
		txt=Text(Point(850,455),'STAY')
		txt.setSize(30)
		txt.setTextColor(color_rgb(0,255,0))
		txt.draw(win)

class Hit_Button(GraphWin,_BBox):

	def __init__(self,p1,p2):
		self.p1=Point(p1.x,p1.y)
		self.p2=Point(p2.x,p2.y)

	def draw(self,win):
		rectangle=Rectangle(self.p1,self.p2)
		rectangle.setFill(color_rgb(255,0,0))
		rectangle.setOutline(color_rgb(0,255,0))
		rectangle.draw(win)
		txt=Text(Point(650,455),'HIT')
		txt.setSize(30)
		txt.setTextColor(color_rgb(255,0,0))
		txt.draw(win)

class Balance(GraphWin,_BBox):

	def __init__(self):
		self.balance=1000
		self.txt=""

	def won(self,value):
		'''
		adds given value to players balance
		'''
		self.balance=self.balance + value

	def bet(self,value):
		'''
		checks if player can bet given value - if he can reduces this ammount by given value and returns True
		'''
		if value > self.balance:
			return True
		else: 
			self.balance=self.balance - value
			return False
	def draw(self,win):
		self.txt=Text(Point(125,850),f'Balance: ${self.balance}')
		self.txt.setSize(30)
		self.txt.setTextColor(color_rgb(255,255,255))
		self.txt.draw(win)
	def undraw(self):
		self.txt.undraw()

class Bet_Button(GraphWin,_BBox):

	def __init__(self,p1,p2):
		self.p1=Point(p1.x,p1.y)
		self.p2=Point(p2.x,p2.y)

	def draw(self,win):
		self.rectangle=Rectangle(self.p1,self.p2)
		self.rectangle.setFill(color_rgb(255,255,255))
		self.rectangle.setOutline(color_rgb(255,255,255))
		self.rectangle.draw(win)
		self.txt=Text(Point(750,825),'BET')
		self.txt.setSize(30)
		self.txt.setTextColor(color_rgb(255,255,255))
		self.txt.draw(win)
	def undraw(self):
		self.txt.undraw()
		self.rectangle.undraw()
from graphics import *
from config import *

def click(win):
	while True:
		click=win.getMouse()
		if 700.0 > click.x > 600.0 and 575.0 > click.y > 475.0:
			return 'hit'
			break
		elif 900.0 > click.x > 800.0 and 575.0 > click.y > 475.0:
			return 'stay'
			break
		elif 800.0 > click.x > 700.0 and 950.0 > click.y > 850.0:
			return 'bet'
			break
		else:
			continue
def bet_ammount(decision,win,value):
	if decision == 'bet':
		txt=Text(Point(500,450),'Enter amount you want to bet:')
		txt.setTextColor(color_rgb(255,255,255))
		txt.setSize(30)
		txt.draw(win)
		input_box=Entry(Point(500,500),5)
		input_box.setSize(30)
		input_box.draw(win)
		while True:
			key=win.getKey()
			try:
				bet=int(input_box.getText())
				if key=='Return' and bet <= value:
					txt.undraw()
					input_box.undraw()
					stay_button=Stay_Button(Point(800,575),Point(900,475))
					stay_button.draw(win)
					hit_button=Hit_Button(Point(600,575),Point(700,475))
					hit_button.draw(win)
					return bet
					
				else:
					continue

				
			except:
				continue




def main():
	
	# set background
	win=GraphWin('Black Jack Game',1000, 1000)
	win.setBackground('black')
	head_text=Text(Point(500,50),'Black Jack Game ')
	head_text.setSize(30)
	head_text.setTextColor(color_rgb(255,255,255))
	head_text.draw(win)
	comp_text=Text(Point(125,225),"Computer's cards:")
	comp_text.setSize(30)
	comp_text.setTextColor(color_rgb(255,255,255))
	comp_text.draw(win)
	player_text=Text(Point(125,625),"Player's deck:")
	player_text.setSize(30)
	player_text.setTextColor(color_rgb(255,255,255))
	player_text.draw(win)
	txt=Text(Point(500,100),'Click to start')
	txt.setSize(30)
	txt.setTextColor(color_rgb(255,0,0))
	txt.draw(win)
	bet_button=Bet_Button(Point(700,850),Point(800,950))
	bet_button.draw(win)
	#stay_button=Stay_Button(Point(800,575),Point(900,475))
	#stay_button.draw(win)
	#hit_button=Hit_Button(Point(600,575),Point(700,475))
	#hit_button.draw(win)
	win.getMouse()
	balance=Balance()
	balance.draw(win)

	# starting setup
	txt.undraw()
	player=Player()
	player.set()
	player.draw(win)
	enemy=Computer()
	enemy.set()
	enemy.draw(win)
	head_text.undraw()
	print(player.count())
	print(enemy.setup)
	print(enemy.count())
	print(player.setup)
	print(player.count())
	
	# waiting for players bet
	while  balance.balance > 0:
		bet=bet_ammount(click(win),win,balance.balance)
		head_text.undraw()
	#actions after bet
		balance.bet(bet)
		balance.undraw()
		balance.draw(win)
		bet_button.undraw()
		player.draw(win)
		enemy.draw(win)
		coverup_player=Rectangle(Point(225,700),Point(1000,800))
		coverup_player.setFill('black')
		coverup_player.draw(win)
		coverup_computer=Rectangle(Point(225,300),Point(1000,400))
		coverup_computer.setFill('black')
		coverup_computer.draw(win)
		player_decision=click(win)
		while player_decision == 'hit' and player.count() <= 21:
			player.hit()
			player.draw(win)
			player_decision=click(win)
			player.count()
			if player.count() > 21:
				head_text.undraw()
				head_text=Text(Point(500,50),'Computer Won')
				head_text.setSize(30)
				head_text.setTextColor(color_rgb(255,255,255))
				head_text.draw(win)
				enemy.drawall(win)
		if player.count() <= 21:
			enemy.decide()
			while enemy.decide() == 'hit' and enemy.count() <=21 :
				enemy.hit()
				enemy.draw(win)
				enemy.decide()
				enemy.count()
			if 21 >= enemy.count() > player.count():
				head_text.undraw()
				head_text=Text(Point(500,50),'Computer Won')
				head_text.setSize(30)
				head_text.setTextColor(color_rgb(255,255,255))
				head_text.draw(win)
				enemy.drawall(win)
			elif 21 >= player.count() > enemy.count():
				head_text.undraw()
				head_text=Text(Point(500,50),'You Won')
				head_text.setSize(30)
				head_text.setTextColor(color_rgb(255,255,255))
				head_text.draw(win)
				enemy.drawall(win)
				print(bet*2)
				balance.won(bet*2)
				balance.undraw()
				balance.draw(win)
			elif enemy.count() > 21:
				head_text.undraw()
				head_text=Text(Point(500,50),'You Won')
				head_text.setSize(30)
				head_text.setTextColor(color_rgb(255,255,255))
				head_text.draw(win)
				enemy.drawall(win)
				balance.won(bet*2)
				balance.undraw()
				balance.draw(win)
		bet_button.draw(win)
		player.set()
		enemy.set()
	head_text.setText('GAME OVER!')

	
	#don't close
	win.getMouse()
	win.close()
main()
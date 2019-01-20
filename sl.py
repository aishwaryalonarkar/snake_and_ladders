import random

snake=[23,17,45,5,52,33,67,23,90,50,99,24]
ladder=[8,29,22,61,54,68,65,97,72,93]
winners=[]
players={"a":0,"b":0,"c":0,"d":0}

global dice_value
global curr_player

def throw_dice():
	global dice_value
	global curr_player
	print("throw dice")
	dice_value=random.randint(1,6)
	print("You got ",dice_value)
	is_player_in(curr_player,dice_value)

def is_player_in(curr_player,dice_value):
	print("is player in")
	if players.get(curr_player)==0 and dice_value>=6:
		status=0
		decision(status,dice_value,curr_player)
		return				
	if players.get(curr_player)>=1:
		status=1
		decision(status,dice_value,curr_player)
		return

def decision(status,score,player):
	print("decision")
	print("score",score)

	if status==1 and score==6:
		throw_dice()
		print(player, "You scored a 6. You get to play again")
		score=+score

	place=players.get(player)+score
	print("place=",place)

	if score in snake:
		sn=snake.index(score)
		if sn%2==0:
			sn=sn+1
			score=snake[sn]
	
	if score in ladder:
		lad=ladder.index(score)
		if lad%2==0:
			lad=lad+1
			score=ladder[lad]

	if score > 100:
		return 0
	
	print("decision score",score)
	if status==0 and score>=6:
		update_score(curr_player,score)
	

def update_score(player,score):
	print("sYour place is ",score) 
	players[curr_player]=score
	if score == 100:
		winner(player,score)
	else:
		player_sequence()
	
def player_sequence():
	global curr_player
	for i in range(0,4):
		curr_player=list(players)[i]
		print("----------------PLAYER ",curr_player)
		print("")
		if i<=4:
			throw_dice()
		else:
			display()
	display()

def print1():
	global curr_player
	global dice_value
	print(curr_player,dice_value)


def winner(curr_player,score):
	print("PLAYER",curr_player ,"You win")
	if score==100:
		winners.append(curr_player)
	print(winners)
	player_sequence()
	display()

def display():
	print("done")

player_sequence()

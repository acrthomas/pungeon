import random

CELLS = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5),
		(1,0), (1,1), (1,2), (1,3), (1,4), (1,5),
		(2,0), (2,1), (2,2), (2,3), (2,4), (2,5),
		(3,0), (3,1), (3,2), (3,3), (3,4), (3,5),
		(4,0), (4,1), (4,2), (4,3), (4,4), (4,5),
		(5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]

monster_lines = ["** Uh oh, the monster caught up to you, and won't stop speaking in memes. \nI'm a jonster, he insists, and this is my jungeon. Yikes. **",
				"** Oh no! The monster caught up to you and keeps trying to show you his blog. \nIt's super cool, she insists, but you're not sure. The layout is a MESS. Better luck next time, friend. **",
				"** The monster caught up to you, and won't stop telling Dad Jokes. \nHi, PLEASE DON'T EAT ME, they grin with a mouth full of bloodied teeth, I'm Dad. \nSorry, pal. **",
				"** Oh jeez, the monster caught up to you. Luckily, it didn't eat you. \nBut, well, it won't stop showing you cute pictures of its daughter. \nIt has an entire wallet folio full. And seven picture albums on hand. You're in it for the long haul, buddy. **",
				"** Oof. The monster caught up to you. You've already made awkward eye contact, it's too late to run. \nAw crap, he's got a CLIPBOARD. \nDo you have a few minutes, he asks, already blocking your path. Nice knowin' you, my guy. **",
				"** The monster caught up to you. He's seems a bit new to the whole monster business. \nInstead of eating you he took out a notebook. \nI wrote a poem, he threatens, shaking it in your direction. \nYou're done for, pal. **"]

nav_lines = ["All these rooms look the same. You hope you find the door soon.",
			"You've gotta keep yourself entertained in here. Say, what do you call an alligator in a suit? An InVESTigator!",
			"It's sno snark in snere. You're snarting to snose snope.",
			"After countless skeletons and their horrible jokes, you come across a ghost. \nMy name is Boo, the ghost tells you. You exchange pleasantries. \nBefore you move on, Boo calls after you, DON'T UWU... FORGET ABOUT ME... \nYou hate this place so much.",
			"You come across a sign: Feeling down or blue? Try Necromancy! It's sure to RAISE YOUR SPIRITS! \nYou turn away. You cannot believe that someone just made you read that with your own two eyes.",
			"You are coming to the grim realization that this dungeon is infecting you with its memeness. \nYou hope you can escape unsnathed--DAMNIT.",
			"Ugh, there's no reception down here. \nYou need to get out soon, or you'll miss the neko atsume daily password.",
			"This dungeon would be a great place to catch some rare pokémon, but.... therE'S NO RECEPTION.",
			"Honestly, after all these terrible puns, you HOPE the monster finds you.",
			"You come across a(nother) skeleton, arranged serenely. \nPlease tell me how to get out of here, you plead. \nYou can lead a horse to water, the skeleton tells you, You can leave your horse behind. \nBecause your horse don't dance and if he don't dance then he's no horse of mine. \nYou begin to weep.",
			"Hey buddy, a(nother) skeleton calls out to you. You start to walk faster. \nHow did Darth Vader survive the Death Star explosion? the skeleton shouts from behind you. \nHe EVADERED it! comes the gleeful response. \nI HATE THIS DUNGEON, you scream into the abyss. \nI think you mean PUNGEON, the abyss replies.",
			"As you pass through the last cell, you nearly trip over a skeleton. \nThis really rattles my bones, it chastises you. \nYou are horrified. Not even the dead can escape this dungeon's puns.",
			"Tag yourself: trapped in a dungeon verion! dark cell, dank cell, quiet cell, cell cell, didn't you just pass that cell? \ntag yourself, i'm cell cell.",
			"Man, this dungeon sure is dreary. But look on the bright side! You could be in a forest with Shia LaBeouf.",
			"You run into a(nother) skeleton. What are you doing down there, you ask. \nI'm skullking, it says with a straight face. You have GOT to get out of here."]

def get_locations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	player = random.choice(CELLS)

	if player == door or player == monster or door == monster:
		return get_locations()

	return monster, door, player


def move_player(player, move):
	x, y = player

	if move == 'LEFT':
		y -= 1
	elif move == 'RIGHT':
		y += 1
	elif move == 'UP':
		x -= 1
	elif move == 'DOWN':
		x += 1

	return x, y

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

	if player[1] == 0:
		moves.remove('LEFT')
	if player[1] == 5:
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == 5:
		moves.remove('DOWN')
	
	return moves

def draw_map(player):
	print (' _ _ _ _ _ _')
	tile = '|{}'

# okay so the index of a cell in CELLS, enumerated, starting from zero
	for idx, cell in enumerate(CELLS):
		# if the index of a cell is one of these
		if idx in [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34]:
			# and the player is in that cell
			if cell == player:
				# print  an X
				print(tile.format('X'), end = '')
			# if the player's not in one of these cells, format the tile like |_
			else:
				print(tile.format('_'), end = '')
		# for all the other cells, so indexes 1, 2, 10, 11, 16, 17, 22, 23, 28, 29, etc
		else:
			# if the player is in that cell, format the square like |X|
			# which means the above indexes should only be for the corners? and these are the middle blocks?
			# in the original, kenneth used the indexes for 0, 1, 3, 4, 6, 7 which was the leftmost column and the middle column
			# so this larger map should use at the LEAST
			if cell == player:
				print(tile.format('X|'))
			# if not, the cell should look like |_|
			else:
				print(tile.format('_|'))
# EDIT: THE OUTER ELSE LOOP FORMATS THE RIGHTMOST COLUMN, SO U GOTTA CALL THE INDEXES OF *EVERY OTHER FUCKING CELL*

monster, door, player = get_locations()
print("You seem to have found yourself in a dungeon. It's probably full of monsters, and gods know what else. You should leave.")

while True:
	moves = get_moves(player)
	
	draw_map(player)
	print("YOU ARE CURRENTLY IN ROOM {}".format(player)) 

	print(random.choice(nav_lines))
	print("You can move {}".format(moves)) 
	print("Enter QUIT to exit the game.")

	move = input("SO, WHICH WAY DO YOU WANNA GO? > ")
	move = move.upper()

	if move == 'QUIT':
		break

	if move in moves:
		player = move_player(player, move)
	else:
		print("** What do you think you are, a transient protein? That's a WALL! **")
		continue

	if player == door:
		print("** Whew! You managed to find your way out! Really dodged a bullet there. **")
		break
	elif player == monster:
		print(random.choice(monster_lines))
		break

import random

CELLS = [(0,0), (0,1), (0,2),
		(1,0), (1,1), (1,2),
		(2,0), (2,1), (2,2)]

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
	if player[1] == 2:
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == 2:
		moves.remove('DOWN')
	
	return moves

def draw_map(player):
	print (' _ _ _')
	tile = '|{}'

	for idx, cell in enumerate(CELLS):
		if idx in [0, 1, 3, 4, 6, 7]:
			if cell == player:
				print(tile.format('X'), end = '')
			else:
				print(tile.format('_'), end = '')
		else:
			if cell == player:
				print(tile.format('X|'))
			else:
				print(tile.format('_|'))

monster, door, player = get_locations()
print("You seem to have found yourself in a dungeon. It's probably full of monsters. You should leave.")

while True:
	moves = get_moves(player)

	print("You're currently in room {}".format(player)) 
	
	draw_map(player)

	print("That door's around here somewhere. You can move {}".format(moves)) 
	print("Enter QUIT to exit the game.")

	move = input("So, which way do you want to go? > ")
	move = move.upper()

	if move == 'QUIT':
		break

	if move in moves:
		player = move_player(player, move)
	else:
		print("** What do you think you are, a transient protein? That's a wall! **")
		continue

	if player == door:
		print("** Congrats! You managed to escape! **")
		break
	elif player == monster:
		print("** Uh oh, the monster caught up to you, and won't stop telling quoting memes. I'm a jonster, he insists, and this is my jungeon. Yikes. **")
		break
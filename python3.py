# program to learn about List by making the game Tic Tac Toe
#ga = (0,0,0,
#	0,0,0,
#	0,0,0)

#print (ga)
#print (type(ga))

#gam = [0,0,0,
#0,0,0,
#0,0,0]
#print (gam)

game = [[0,0,0],
[0,0,0],
[0,0,0]]
#print (game)
print ("     0  1  2")
count = 0
#for row in game:
#	print(count, row)
#	count += 1
"""
enumerate function all it does is return the item and its index
value as we iterate 
"""
for count, row in enumerate(game):
	print(count, row)
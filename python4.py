# learning about indexing in python

l = [1, 2, 3, 4, 5]
print (l[4])
print (l[1])
print(l[-1])
print(l[-3])

# slicing
# l[x:y] from index x to index y-1
print(l[2:4])
print(l[1:5])

# setting value at particular index
l[1] = 99
print(l)

# 2D list
game = [[0, 2, 0],
[0,0,0],
[0,0,0]]
print (game)
print(game[0][1])
game[0][2] = 3
print(game)
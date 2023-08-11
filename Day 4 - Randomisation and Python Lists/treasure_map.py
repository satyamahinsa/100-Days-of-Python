row1 = ['🟥', '🟥', '🟥']
row2 = ['🟥', '🟥', '🟥']
row3 = ['🟥', '🟥', '🟥']

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

treasure_position = input("Where do you want to put the treasure?:")
column = int(treasure_position[0]) - 1
row = int(treasure_position[1]) - 1

map[row][column] = '❎'
print(f"{row1}\n{row2}\n{row3}")
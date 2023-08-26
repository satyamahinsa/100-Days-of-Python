# 1. Variable within a function, it's only available within that function.
# 2. Variable within if block, while loop, for loop, ect, that does not count as creating a separate local scope.

player_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if player_level < 5:
  big_boss = enemies[0]

print(big_boss)
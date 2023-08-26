# ======= SCOPE =======

enemies = 1
def increase_enemies():
  enemies = 2
  print(f"Enemies inside functions: {enemies}")

increase_enemies()
print(f"Enemies outside functions: {enemies}")


# Local Scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
# print(potion_strength) # Error because can't access variabel in the drink_potion().


# Global Scope
player_health = 10

def game():
  def drink_potion():
    potion_strength = 2
    print(player_health) # player_health can be access anywhere.
  
  drink_potion()

game()

# ----------- FUNCTION BLOCK ------------
def guessColor():
  fruit = input("Write down the name of the fruit: ")
  # ----- BLOCK IF
  if fruit == "grape":
    print("Purple.")
  # -------------------
  # ----- ELIF BLOCK -----
  elif fruit == "orange":
    print("Orange.")
  # ---------------------
  # ----- BLOCK ELSE -----
  else:
    print("Fruits other than grapes and oranges.")
  # ---------------------

guessColor()
# Reproduce the bug.
from random import randint

# dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])

# Fix code above.
dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)

# Costum table with colors
color_table = ColorTable(theme=Themes.OCEAN)

color_table.add_column("Student Name", ["Eka", "Budi", "Siti"])
color_table.add_column("Age", [16, 15, 17])

print(color_table)

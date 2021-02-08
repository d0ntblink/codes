from prettytable import PrettyTable, ALL

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
table.hrules = ALL

print(table)
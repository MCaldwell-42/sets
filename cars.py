# Using set() to create a set
# languages = set('english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese')
# Apparently the above doesn't work?


# Using curly braces
languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }

showroom = set()

showroom.add("Ford")
showroom.add("Tesla")
showroom.add("BMW")
showroom.add("Porche")

print(len(showroom))

showroom.add("Tesla")

showroom.update({"Toyota", "minivan"})

showroom.discard("minivan")

junkyard = { 'BMW', 'Ford', 'el camino', 'dump truck', 'pick up truck'}

print(junkyard.intersection(showroom))

new_showroom = showroom.union(junkyard)

print(new_showroom)

junkyard.discard("BMW")
junkyard.discard("Ford")

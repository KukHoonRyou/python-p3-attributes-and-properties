class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name

guido = Human("Guido")
print(guido.species)
print(guido.name)

guido.species = "Python programmer"
guido.name = "Guido van Rossum"

print(guido.name)
print(guido.species)

guido.nationality = "Dutch"
print(guido.nationality)

getattr(guido, "name")
setattr(guido, "nationality", "Korea")

print(guido.name)
print(guido.nationality)


my_attr = "is_a_friend"
getattr(guido, my_attr, False)

setattr(guido, my_attr, True)
getattr(guido, my_attr, False)

hasattr(guido, "name")
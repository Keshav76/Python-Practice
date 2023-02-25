name = ['Keshav', 'Gauri', 'Nandan', 'Anika']
classes = ['BTech', '9th', '9th', '4th']

name_class = zip(name, classes)                  #it gives a zip type of object
print(name_class)
name_class = list(zip(name,classes))
print(name_class)
name_class = set(zip(name, classes))
print(name_class)
name_class = dict(zip(name,classes))
print(name_class)
name_class = tuple(zip(name, classes))
print(name_class)

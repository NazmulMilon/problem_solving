

names = ("Nazmul", 'Hasan', 'Milon' 'Milon')
coms = ('MS', 'Facebook', 'Google', 'Amazon')

# zipped = list(zip(names, coms))
# zipped = set(zip(names, coms))  # set only print the unique values
zipped = dict(zip(names, coms))

print(zipped)
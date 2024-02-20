word = "bananana"
i = word.find("na")
print(i)

data = 'From stephen.muiko@gmail.com Sat Jan 2004'
atpos = data.find('@')
print(atpos)

supos = data.find(' ',atpos)
print(data[atpos: supos])



# Uppgift 1


"""
ord = input("Skriv något: ")

konstanter = ["B","b", "C","c", "D","d", "F","f", "G","g", "H","h", "J","j", "K","k", "l","l", "M","m", "N","n", "P","p", "Q","q", "R","r", "S","s", "T","t", "V","v", "W","w", "X","x", "Z","z"]

översatt = ""
for i in ord:
    if i in konstanter:
        översatt += i + "o" + i
    else:
        översatt += i

print(översatt)
"""

# Uppgift 2


"""
ord = input("Skriv något: ")

reverse = ""
x = len(ord)-1
for i in ord:
    reverse += ord[x]
    x -= 1

print(reverse)
"""

# Uppgift 3


"""
dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
dic.update({"Danmark": "Köpenhamn"})
dic.pop("Finland")

print(dic)
"""

# Uppgift 4


"""
x = {"Banan", "Päron", "Äpple"}
y = {"Kiwi", "Annan", "Päron"}

print(x.union(y))
print(len(x.union(y)))
"""
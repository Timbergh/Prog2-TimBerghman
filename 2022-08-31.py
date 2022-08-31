# Uppgift 1
"""
for i in range(1000):
    if i % 7 == 0:
        print(i)

"""
# Uppgift 2

"""
siffror = input("Skriv in ett nummer: ")
antal = 0
for i in range(len(siffror)):
    try:
        int(siffror[i])
        antal += 1
    except:
        pass

print(antal)
"""
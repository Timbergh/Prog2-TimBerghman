

class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd
    
    glad = False

elev1 = Elev("Tim", 18, True)
if elev1.godkänd:
    elev1.glad = True

print(elev1.glad)
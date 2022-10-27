#Playing around with the ideas of classes

class Lightweight:
    '''Represents men in the UFC's 155lb divison'''

    def __init__(self, age, country, name):
        '''Creates a new Lightweight fighter with a specified
        name, country and age'''
        self.age = age
        self.country = country
        self.name = name

img = Lightweight("30", "Dagestan",  "Islam Makhachev")
cob = Lightweight("34", "Brazil", "Charles Oliviera")

print(img.name, img.age, img.country)
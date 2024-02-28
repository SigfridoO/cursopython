class Padre:
    def __init__(self): 
        print('Soy tu padre')

class Madre:
    def __init__(self):
        print('Soy tu madre')

class Hijo(Padre, Madre):
    def __init__(self):
        #super().__init__()
        Padre.__init__(self)
        Madre.__init__(self)
        print ('Soy hijo')

hijo = Hijo()
class Padre:
    def __init__(self): 
        print('Soy tu padre')



class Hijo(Padre):
    def __init__(self):
        super().__init__()
        print ('Soy hijo')

hijo = Hijo()

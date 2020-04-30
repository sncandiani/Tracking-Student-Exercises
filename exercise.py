class Exercise: 
    def __init__(self, name): 
        self.name = name
        self.language = ""
    def __repr__(self):
        return f'{self.name}'
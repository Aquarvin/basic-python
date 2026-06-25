class Driver:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        
    def info(self):
        return f"{self.name} - {self.points} очков"
    
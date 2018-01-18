class Ball:
    def __init__(self, radius, color, weight):
        self.radius = radius
        self.color = color
        self.weight = weight
    # terminal: 
    #     from ball import Ball
    #     red_ball = Ball(10, 'red', 2)
    #     blue_ball = Ball(12, 'blue', 5)

    #     red_ball.color => 'red'
    #     blue_ball.weight => 5

class Football:
    """A standard, regulation NFL ball"""
    def __init__(self, diameter, color, pressure):
        self.diameter = diameter
        self.color = color
        self.pressure = pressure

    def inflate(self, psi):
        self.pressure = self.pressure + psi

    def deflate(self, psi):
        self.pressure = self.pressure - psi
    
    #terminal:
        # from ball import Football
        # bears = Football(22, 'red', 13)
        # packers = Football(22, 'brown', 13)

        # bears.color => 'red'
        # packers.pressure(2)
        # packers.pressure => 15

class PatriotsBall(Football): # PatriotsBall inherits the Football class
    def inflate(self, psi):
        self.pressure = self.pressure - psi
    
    # terminal:
        # from ball import PatriotsBall
        # patriots = PatriotsBall(22, 'brown', 13)
        # patriots.inflate(2)
        # patriots.pressure => 11

        # dir(PatriotsBall) =>
        # ['__doc__', '__init__', '__module__', 'deflate', 'inflate']
        # dir(patriots) =>
        # ['__doc__', '__init__', '__module__', 'color', 'deflate', 'diameter', 'inflate', 'pressure']
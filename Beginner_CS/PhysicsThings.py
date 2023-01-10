Class PhysicsThings(weight, height, speed):
    GRAVITY = 9.8

    def getWeight(weight):
        return weight * GRAVITY

    def potentialEnergy(weight, height):
        return weight * height * GRAVITY

    def kineticEnergy(weight, speed):
        return weight * (speed ** 2) / 2

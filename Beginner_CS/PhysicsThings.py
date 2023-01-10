class PhysicsThings():
    GRAVITY = 9.8

    def getWeight(self, weight):
        return weight * PhysicsThings.GRAVITY

    def potentialEnergy(self, weight, height):
        return weight * height * PhysicsThings.GRAVITY

    def kineticEnergy(self, weight, speed):
        return weight * speed ** 2 / 2


print(PhysicsThings().getWeight(80))
print(PhysicsThings().kineticEnergy(80, 10))

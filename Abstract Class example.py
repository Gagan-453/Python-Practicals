# Example of Abstract Class
from abc import*
class Car(ABC):
    def __init__(self, regno):
        self.regno = regno
        
    def opentank(self):
        print('Fill the fuel into the tank')
        print('For the car with regno ', self.regno)
        
    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def braking(self):
        pass

print('---------MARUTI CAR---------')
class Maruti(Car):
    def steering(self):
        print('Maruti uses manual steering')
        print('Drive the car')
    def braking(self):
        print('Maruti uses hydraulic brakes')
        print('Apply brakes and stop the car')
        
m = Maruti(1001)
m.opentank()
m.steering()
m.braking()


print('---------SANTRO CAR---------')
class Santro(Car):
    def steering(self):
        print('Santro uses power steering')
        print('Drive the car')
    def braking(self):
        print('Maruti uses gas brakes')
        print('Apply brakes and stop the car')
        
s = Santro(7878)
s.opentank()
s.steering()
s.braking()
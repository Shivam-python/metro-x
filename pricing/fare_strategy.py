from abc import ABC, abstractmethod

class FareStrategy(ABC):
    @abstractmethod
    def get_fare(self, passenger_type, journey_type):
        pass

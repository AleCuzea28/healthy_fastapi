from abc import ABC

class Programator(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class SeniorProgramator(Programator):
    def calculate_salary(self):
        return 10000    
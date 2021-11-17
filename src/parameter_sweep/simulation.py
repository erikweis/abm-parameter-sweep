from abc import ABC
import abc

class Simulation(ABC):

    def __init__(self):
        pass

    @abc.abstractproperty
    def dirname(self):
        pass

    @abc.abstractmethod
    def run_simulation(self):
        pass

    @abc.abstractmethod
    def on_finish(self):
        pass
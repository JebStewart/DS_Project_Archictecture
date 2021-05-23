import pandas as pd

class SIM:
    def __init__(self, sim_type='time'):
        self._type_ = sim_type

    def RUN(self):
        if self._type_ == 'time':
            pass
        elif self._type_ == 'other':
            pass #todo add running chunks as needed.
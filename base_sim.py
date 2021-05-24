import pandas as pd

class SIM:
    def __init__(self, sim_type='time'):
        self._type_ = sim_type
        self.sim = pd.DataFrame()
        self.model_pipeline = None

    def populate_inputs(self, **kwargs):
        """Fills base dataframe with input portion of sim"""
        if self._type_ == 'time':
            header_tracker = ''
            try:
                for header, data in kwargs.items():
                    header_tracker = header
                    self.sim[header] = data
            except Exception as e:
                print(f'Failed to set "{header_tracker}" inputs.', e.args)
                return False
            return True

    def RUN(self):
        if self._type_ == 'time':
            try:
               self.sim['PREDICTION'] = self.sim.apply(lambda x: self.model_pipeline(x), axis=1)
            except Exception as e:
                print('Failed to run sim.', e.args)
        elif self._type_ == 'other':
            pass #todo add running chunks as needed.

if __name__ == '__main__':
    sim = SIM()
    sim.populate_inputs(one = [1, 2], two = [3, 4, 5])
    print(sim.sim.head())
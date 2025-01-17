from parameters import WaterLPParameter

from utilities.converter import convert

class node_MER_01_Headflow_Runoff(WaterLPParameter):
    """"""

    def _value(self, timestep, scenario_index):
        
        return self.read_csv("Scenarios/Livneh/runoff/tot_runoff_sb1.csv", squeeze=True)[timestep.datetime]
        
    def value(self, timestep, scenario_index):
        return convert(self._value(timestep, scenario_index), "m^3 s^-1", "m^3 day^-1", scale_in=1, scale_out=1000000.0)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)
        
node_MER_01_Headflow_Runoff.register()
print(" [*] node_MER_01_Headflow_Runoff successfully registered")

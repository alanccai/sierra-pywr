from parameters import WaterLPParameter

from utilities.converter import convert

class node_Big_Creek_2_PH_Turbine_Capacity(WaterLPParameter):
    """"""

    def _value(self, timestep, scenario_index):
        
        return 607 / 35.31  # cfs to cms
        
    def value(self, timestep, scenario_index):
        return convert(self._value(timestep, scenario_index), "m^3 s^-1", "m^3 day^-1", scale_in=1, scale_out=1000000.0)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)
        
node_Big_Creek_2_PH_Turbine_Capacity.register()
print(" [*] node_Big_Creek_2_PH_Turbine_Capacity successfully registered")

from parameters import WaterLPParameter

from utilities.converter import convert

class node_New_Melones_PH_Water_Demand(WaterLPParameter):
    """"""
    # TODO ADD A TURBINE CAPACITY
    def _value(self, timestep, scenario_index):
        TC = self.model.parameters["node/Donnells PH/Turbine Capacity"].value(timestep, scenario_index)
        qDemand = TC * 3600 * 6
        return qDemand

    def value(self, timestep, scenario_index):
        m3day_to_millionm3 = 0.000001
        return self._value(timestep, scenario_index) * m3day_to_millionm3

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)
        
node_New_Melones_PH_Water_Demand.register()
print(" [*] node_New_Melones_PH_Water_Demand successfully registered")
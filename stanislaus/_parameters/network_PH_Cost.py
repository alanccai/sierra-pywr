from parameters import WaterLPParameter


class network_PH_Cost(WaterLPParameter):
    """"""

    # path = "s3_imports/energy_netDemand.csv"

    baseline_median_daily_energy_demand = 768  # 768 GWh is median daily energy demand for 2009

    def _value(self, timestep, scenario_index, mode='scheduling'):

        totDemandP = self.model.parameters["Total Net Energy Demand"]
        maxDemandP = self.model.parameters["Max Net Energy Demand"]
        minDemandP = self.model.parameters["Min Net Energy Demand"]

        days_in_period = 1

        if self.mode == 'scheduling':
            totDemand = totDemandP.value(timestep, scenario_index)
            minDemand = maxDemandP.value(timestep, scenario_index)
            maxDemand = maxDemandP.value(timestep, scenario_index)

        else:
            planning_dates = self.dates_in_planning_month(timestep, month_offset=self.month_offset)
            days_in_period = len(planning_dates)
            totDemand = totDemandP.dataframe[planning_dates].sum()
            minDemand = minDemandP.dataframe[planning_dates].min()
            maxDemand = maxDemandP.dataframe[planning_dates].max()

        minVal = self.model.parameters[self.demand_constant_param].value(timestep, scenario_index) \
                 * (totDemand / (self.baseline_median_daily_energy_demand * days_in_period))
        maxVal = minVal * (maxDemand / minDemand)
        d = maxVal - minVal

        nblocks = self.model.parameters['Blocks'].value(timestep, scenario_index)
        return -(maxVal - ((self.block * 2 - 1) * d / 2) / nblocks)

    def value(self, timestep, scenario_index):
        return self._value(timestep, scenario_index, mode=self.mode)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)


network_PH_Cost.register()

print(" [*] PH_Cost successfully registered")

# -*- coding: utf-8 -*-
"""
Defines a death_risk class. There will only
"""

    def death_risk_update(self,state):
        initial_risk = 0.001 * 1.05 ** (self.age-18.0)
        if state == "OMT":
            state_shock = OMT.death_risk_shock
        elif state == "DrugFreeTreatment":
            state_shock = DrugFreeTreatment.death_risk_shock
        elif state == "NoTreatment":
            state_shock = NoTreatment.death_risk_shock
        self.death_other_risk = initial_risk * state_shock
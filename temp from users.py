# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 13:04:12 2015

@author: olejrogeberg
This file is a catchment file for functions removed from the User class. The
functions will be implemented in a different class of objects specifying the 
different kinds of risks faced.
"""

    def od_risk_update(self,state):
        """Calculates the risk of overdose, which is influenced by the state.
        To ensure that the probability stays between 0 and 1 I have used
        a logit-link function."""
        
        if state == "OMT":
            state_risk = OMT.use_risk
        elif state == "DrugFreeTreatment":
            state_risk = DrugFreeTreatment.use_risk
        elif state == "NoTreatment":
            state_risk = NoTreatment.use_risk
            
        own_use_risk_input = -1 + 0.5 * (self.use_current - 5) + \
            0.1 * (self.use_current - self.use_history[-1]) + state_risk
        own_use_risk = math.exp(own_use_risk_input)/ \
            (1+math.exp(own_use_risk_input))
        self.od_risk = own_use_risk
        
        
    def use_update(self,state):
        random_drift = self.use_current + \
            User.use_mean_reversion * (self.use_set_point - self.use_current) \
            + random.normalvariate(0,User.use_shock_sd)
        if state == "OMT":
            state_shock = OMT.use_shock
        elif state == "DrugFreeTreatment":
            state_shock = DrugFreeTreatment.use_shock
        elif state == "NoTreatment":
            state_shock = NoTreatment.use_shock
        self.use_current = min(10,max(0,random_drift + \
            random.normalvariate(state_shock[0],state_shock[1])))
        


    def risk_draw(self):
        draw = random.random()
        if draw < self.od_risk:
            self.alive = False
            self.od = True
        elif draw < self.od_risk + self.death_other_risk:
            self.alive = False



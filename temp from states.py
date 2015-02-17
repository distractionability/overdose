# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 13:10:57 2015

@author: olejrogeberg

This file is a catchment file for functions removed from the State classes. The
functions will be implemented in a different class of objects specifying the 
different kinds of risks faced, and in the society (the functions updating 
the list of living users, etc).

"""

    def update_members(self):
        for member in self.members:
            member.update(type(self).__name__)
            if member.alive==False:
                self.dead.add(member)
            if member.od==True:
                self.od.add(member)
        for corpse in self.dead:
            self.members.remove(corpse)
            
    def find_transitions(self,year):
        self.transition_omt=set([])
        self.transition_no_treatment=set([])
        self.transition_drug_free_treatment=set([])
        
        for individual in self.members:
            transfer_risks = \
                self.calculate_transfer_risks(individual,year)
            random_draw=random.random()
            if random_draw < transfer_risks["omt"]:
                self.transition_omt.add(individual)
            elif random_draw < (transfer_risks["omt"] + \
                transfer_risks["no_treatment"]):
                self.transition_no_treatment.add(individual)
            else:
                self.transition_drug_free_treatment.add(individual)

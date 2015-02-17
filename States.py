# -*- coding: utf-8 -*-
"""
This file defines the State class, along with its
three subclasses NoTreatment, DrugFreeTreatment and OMT.

The states describe the characteristics of the individuals currently belonging
to that state, and log the history of the state throughout a specific 
simulation run.
"""
import random

class State(object):
    
    def __init__(self):
        self.users_number_current = 0
        self.users_number_history=[]
        self.overdoses_lethal_current=0
        self.overdoses_lethal_history=[]
        self.overdoses_survived_current=0
        self.overdoses_survived_history=[]
        self.deaths_other_current=0
        self.deaths_other_history=[]
                
       

        

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 13:40:04 2015

@author: olejrogeberg

This file contains the Society class. An actual simulation will (in the end) be
specified and managed at this level. An instance of this class will contain
three instances of State, one for each state (no_treatment, drug_free_treatment,
omt). It also contains one instance of User for each individual alive,
and a set of methods for updating these, logging, summarizing and 
visualizing events.
"""

from States import State

class Society(object):
    def __init__(self):
        self.no_treatment=State()
        self.drug_free_treatment=State()
        self.omt=State()
        self.year = 0
        self.people=set([])
        
    def receive_users(self,users):
        for user in users:
            self.people.add(user)

    def do_recruitment(self):
        pass

    def do_use_level_changes(self):
        pass
    
    def do_state_transitions(self):
        for receiving_state in self.states:
            for giving_state in self.states:
                receiving_state.receive_members(\
                    giving_state.give_members(receiving_state.own_state))
                    
    def do_overdoses(self):
        pass
    
    def do_deaths(self):
        pass
    
    def do_cleaning(self):
        dead=0
        corpses=set([])
        od=0
        for person in self.people:
            if self.dead:
                dead += 1
                corpses.add(person)
            if self.overdose:
                od += 1
        for corpse in corpses:
            self.people.remove(corpse)
        print "Dead: " + str(dead) + " OD: " + str(od)
        
    def do_logging(self):
        pass
            
    def update_users(self):
        for state in self.states:
            state.update_members()
    
    def run_one_year(self):
        self.year += 1
        self.update_users()
        self.do_recruitment()
        self.do_use_level_changes()
        self.do_overdoses()
        self.do_deaths()
        self.do_logging()
        self.do_cleaning()
        self.do_state_transitions()
        
    def run_several_years(self,years):
        for i in range(years):
            self.run_one_year()
                
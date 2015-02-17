# -*- coding: utf-8 -*-
"""
This file sources and runs specific simulations.
"""

from User import User
from States import State, NoTreatment, DrugFreeTreatment, OMT
from Society import Society
import random

soc = Society(1000)

soc.run_several_years(20)

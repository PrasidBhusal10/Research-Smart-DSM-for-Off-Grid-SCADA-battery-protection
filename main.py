import numpy as np
import pandas as pd

class SCADABatterySystem:
    def __init__(self, capacity_kwh=10.0, initial_soc=0.8):
        self.capacity = capacity_kwh  # Total battery capacity
        self.soc = initial_soc        # State of Charge (0.0 to 1.0)
        self.efficiency = 0.98     # Charge/Discharge efficiency
        
    def apply_dsm_logic(self, solar_gen, loads):
        """
        Priority-based Demand Side Management Logic
        loads: dict { 'critical': float, 'essential': float, 'auxiliary': float }
        """
        active_load = 0
        shed_status = {"essential": False, "auxiliary": False}

        # 1. Critical Load (Always try to power)
        active_load += loads['critical']

        # 2. Essential Load (Shed if SoC < 50%)
        if self.soc > 0.50:
            active_load += loads['essential']
        else:
            shed_status["essential"] = True
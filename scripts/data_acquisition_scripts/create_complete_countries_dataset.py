from config.config import *
from functions.data_acquisition_functions.create_complete_countries_dataset import create_complete_countries_dataset
import sys

# 4/5/19 remember that countries only works with the oneeighty days date range

create_complete_countries_dataset()

print(f"one eighty countries complete dataset created")

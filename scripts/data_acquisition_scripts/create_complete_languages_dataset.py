from config.config import *
from functions.data_acquisition_functions.create_complete_languages_dataset import create_complete_languages_dataset
import sys

create_complete_languages_dataset()

print(f"one eighty complete languages dataset created")

import pandas as pd


import os

current_dir = os.path.abspath(os.path.dirname(__file__))
csv_name = os.path.join(current_dir, 'region.csv')

CITY_DF = pd.read_csv(csv_name, engine='python', encoding='utf-8')




'''
Authors: Struck and Tha
This script makes a figure with two subplots
'''
import pandas as pd

dats = pd.read_csv('DATA/gapminder-FiveYearData.csv')

afg_dats = dats[dats['country']=='Afghanistan']

#plot subfplot B
#bla
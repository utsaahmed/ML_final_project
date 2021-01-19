#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the required libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import yaml
import glob


# In[4]:


fieldnames = ['City', 'Dates', 'Gender', 'Match_Type', 'Overs', 'Team1', 'Team2', 'Toss', 'Choice', 'Winner', 'Outcome', 'Margin']

with open('international.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=fieldnames)
    csv_output.writeheader()

    for filename in glob.glob('*.yaml'):
        with open(filename) as f_input:
            data = yaml.safe_load(f_input)

        try:
            city = data['info']['city']
        except KeyError:
            city = None
        try:
            dates = data['info']['dates'][0]
        except KeyError:
            dates = None
        try:
            gender = data['info']['gender']
        except KeyError:
            gender = None
        try:
            match_type = data['info']['match_type']
        except KeyError:
            match_type = None
        try:
            overs = data['info']['overs']
        except KeyError:
            overs = None
        try:
            team1 = data['info']['teams'][0]
        except KeyError:
            team1 = None
        try:
            team2 = data['info']['teams'][1]
        except KeyError:
            team2 = None
        try:
            toss = data['info']['toss']['winner']
        except KeyError:
            toss = None
        try:
            choice = data['info']['toss']['decision']
        except KeyError:
            choice = None
        try:
            winner = data['info']['outcome']['winner']
        except KeyError:
            winner = 'draw'
        try:
            outcome = list(data['info']['outcome']['by'].keys())[0]
        except KeyError:
            outcome = 'draw'
        try:
            margin = list(data['info']['outcome']['by'].values())[0]
        except KeyError:
            margin = 0

        csvRow = [city, dates, gender, match_type, overs, team1, team2, toss, choice, winner, outcome, margin]
        
        wr = csv.writer(f_output, dialect='excel')
        wr.writerow(csvRow)

